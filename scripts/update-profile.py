import os
import re
import urllib.request
import json

USERNAME = "kadekgirendra"
README = "README.md"

# Ambil data profil GitHub
url = f"https://api.github.com/users/{USERNAME}"

request = urllib.request.Request(
    url,
    headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "github-profile-updater"
    }
)

with urllib.request.urlopen(request) as response:
    data = json.loads(response.read().decode())

repositories = data["public_repos"]
followers = data["followers"]
following = data["following"]
name = data["name"] or USERNAME

# Baca README
with open(README, "r", encoding="utf-8") as file:
    content = file.read()

# Bagian yang akan di-update otomatis
start_marker = "<!-- PROFILE-STATS:START -->"
end_marker = "<!-- PROFILE-STATS:END -->"

new_stats = f"""<!-- PROFILE-STATS:START -->
<pre>
◈  Name         →  {name}
◈  Repositories →  {repositories}
◈  Followers    →  {followers}
◈  Following    →  {following}
◈  Contact      →  kadekgirendra@gmail.com
</pre>
<!-- PROFILE-STATS:END -->"""

pattern = re.escape(start_marker) + r".*?" + re.escape(end_marker)

updated_content = re.sub(
    pattern,
    new_stats,
    content,
    flags=re.DOTALL
)

# Simpan README
with open(README, "w", encoding="utf-8") as file:
    file.write(updated_content)

print("Profile information updated successfully!")
