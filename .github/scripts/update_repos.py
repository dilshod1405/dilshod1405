import requests

USERNAME = "dilshod1405"
README_PATH = "README.md"
START = "START_SECTION:repos"
END = "END_SECTION:repos"
MAX_REPOS = 5

def get_repos():
    url = f"https://api.github.com/users/{USERNAME}/repos?sort=updated&per_page={MAX_REPOS}"
    res = requests.get(url)
    res.raise_for_status()
    repos = res.json()
    return [
        f"- [{repo['name']}]({repo['html_url']}) - ⭐ {repo['stargazers_count']} | {repo['description'] or 'No description'}"
        for repo in repos
    ]

def update_readme(repos_md):
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    start_idx = content.find(START)
    end_idx = content.find(END)

    if start_idx == -1 or end_idx == -1:
        print("START or END section not found in README.md")
        return

    before = content[:start_idx + len(START)]
    after = content[end_idx:]
    new_content = f"{before}\n{chr(10).join(repos_md)}\n{after}"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    repos_md = get_repos()
    update_readme(repos_md)
