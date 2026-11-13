"""Write the follower count shown on the profile page into the Follow badge in README.md.

The REST API (and shields.io, which reads it) leaves out followers GitHub hides from it,
so its count is lower than the one on the profile page.
"""

import re
import sys
import urllib.request

USER = "vinirib"
PAGE_COUNT = re.compile(r'<span class="text-bold color-fg-default">(\d+)</span>\s*followers')
BADGE = re.compile(r"https://img\.shields\.io/(?:github/followers/" + USER + r"|badge/Follow-\d+-4F46E5)\?[^\"]*")


def profile_followers():
    request = urllib.request.Request(f"https://github.com/{USER}", headers={"User-Agent": "profile-readme"})
    with urllib.request.urlopen(request, timeout=30) as response:
        match = PAGE_COUNT.search(response.read().decode("utf-8"))
    if not match:
        sys.exit("follower count not found on the profile page")
    return int(match.group(1))


def main(path):
    with open(path, encoding="utf-8") as f:
        readme = f.read()
    if not BADGE.search(readme):
        sys.exit(f"Follow badge not found in {path}")
    badge = f"https://img.shields.io/badge/Follow-{profile_followers()}-4F46E5?style=for-the-badge&logo=github"
    updated = BADGE.sub(badge, readme)
    if updated != readme:
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "README.md")
