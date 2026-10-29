"""Rewrite the OSS-PRS block in README.md with the latest pull requests to repos I don't own."""

import json
import os
import re
import sys
import urllib.parse
import urllib.request

USER = "vinirib"
LIMIT = 6
BLOCK = re.compile(r"(<!-- OSS-PRS:START -->\n).*?(<!-- OSS-PRS:END -->)", re.DOTALL)
STATE_ICON = {"merged": "🟣", "open": "🟢", "closed": "⚪"}


def fetch_prs():
    query = urllib.parse.quote(f"author:{USER} type:pr -user:{USER}")
    url = f"https://api.github.com/search/issues?q={query}&sort=updated&order=desc&per_page={LIMIT}"
    request = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)["items"]


def render(prs):
    lines = []
    for pr in prs:
        state = "merged" if pr["pull_request"].get("merged_at") else pr["state"]
        repo = pr["repository_url"].removeprefix("https://api.github.com/repos/")
        title = pr["title"].replace("|", "\\|")
        lines.append(f"- {STATE_ICON[state]} **{repo}** [#{pr['number']}]({pr['html_url']}) {title}")
    return "\n".join(lines) + "\n"


def main(path):
    with open(path, encoding="utf-8") as f:
        readme = f.read()
    if not BLOCK.search(readme):
        sys.exit(f"OSS-PRS markers not found in {path}")
    updated = BLOCK.sub(lambda m: m.group(1) + render(fetch_prs()) + m.group(2), readme)
    if updated != readme:
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "README.md")
