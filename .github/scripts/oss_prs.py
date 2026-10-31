"""Rewrite the OSS-PROJECTS table and the OSS-PRS list in README.md from my pull requests to repos I don't own.

The table texts come from .github/oss-projects.json (file order). A repo with PRs but no entry there is
appended with its GitHub description until it gets curated. Merged counts always come from the API.
"""

import json
import os
import re
import sys
import urllib.parse
import urllib.request

USER = "vinirib"
LIMIT = 6
PROJECTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "oss-projects.json")
PRS_BLOCK = re.compile(r"(<!-- OSS-PRS:START -->\n).*?(<!-- OSS-PRS:END -->)", re.DOTALL)
TABLE_BLOCK = re.compile(r"(<!-- OSS-PROJECTS:START -->\n).*?(<!-- OSS-PROJECTS:END -->)", re.DOTALL)
STATE_ICON = {"merged": "🟣", "open": "🟢", "closed": "⚪"}


def api(path):
    request = urllib.request.Request(f"https://api.github.com/{path}", headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def fetch_prs():
    """All my PRs to other people's repos, most recently updated first."""
    query = urllib.parse.quote(f"author:{USER} type:pr -user:{USER}")
    prs, page = [], 1
    while True:
        items = api(f"search/issues?q={query}&sort=updated&order=desc&per_page=100&page={page}")["items"]
        prs += items
        if len(items) < 100 or page == 10:
            return prs
        page += 1


def repo_of(pr):
    return pr["repository_url"].removeprefix("https://api.github.com/repos/")


def state_of(pr):
    return "merged" if pr["pull_request"].get("merged_at") else pr["state"]


def cell(text):
    return (text or "").replace("|", "\\|").strip()


def plural(count, word):
    return f"{count} {word}{'' if count == 1 else 's'}"


def render_prs(prs):
    lines = []
    for pr in prs[:LIMIT]:
        lines.append(f"- {STATE_ICON[state_of(pr)]} **{repo_of(pr)}** [#{pr['number']}]({pr['html_url']}) {cell(pr['title'])}")
    return "\n".join(lines) + "\n"


def render_table(prs, projects):
    merged, active = {}, []
    for pr in prs:
        repo, state = repo_of(pr), state_of(pr)
        merged[repo] = merged.get(repo, 0) + (state == "merged")
        if state != "closed" and repo not in active:
            active.append(repo)
    # curated repos in file order, then new ones by latest activity; repos with only closed PRs are left out
    repos = [r for r in projects if r in active] + [r for r in active if r not in projects]

    lines = ["| Project | What it is | What I'm doing |", "|---------|------------|----------------|"]
    for repo in repos:
        entry = projects.get(repo) or {"what": api(f"repos/{repo}").get("description"), "doing": ""}
        doing = [cell(entry.get("doing"))]
        if merged[repo]:
            doing.append(f"{plural(merged[repo], 'PR')} merged")
        elif repo not in projects:
            doing.append("First PRs in review")
        name = repo.split("/")[1]
        lines.append(f"| **[{name}](https://github.com/{repo})** | {cell(entry.get('what'))} | "
                     f"{'. '.join(d for d in doing if d)} |")
    return "\n".join(lines) + "\n"


def main(path):
    with open(path, encoding="utf-8") as f:
        readme = f.read()
    for name, block in (("OSS-PRS", PRS_BLOCK), ("OSS-PROJECTS", TABLE_BLOCK)):
        if not block.search(readme):
            sys.exit(f"{name} markers not found in {path}")
    with open(PROJECTS, encoding="utf-8") as f:
        projects = json.load(f)
    prs = fetch_prs()
    updated = PRS_BLOCK.sub(lambda m: m.group(1) + render_prs(prs) + m.group(2), readme)
    updated = TABLE_BLOCK.sub(lambda m: m.group(1) + render_table(prs, projects) + m.group(2), updated)
    if updated != readme:
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "README.md")
