import requests
from bs4 import BeautifulSoup

def get_leetcode_stats(username):
    url = f"https://leetcode.com/{username}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    solved = soup.find('div', class_='solved-problems')
    solved_count = solved.find('span', class_='count').text if solved else '0'

    return {
        "solved_problems": solved_count,
    }

if __name__ == "__main__":
    username = "DominikHom"
    stats = get_leetcode_stats(username)
    with open("leetcode_stats.md", "w") as f:
        f.write(f"## LeetCode Stats for {username}\n")
        f.write(f"- Solved Problems: {stats['solved_problems']}\n")
    
    with open("README.md", "r") as f:
        readme_content = f.read()
    
    start_marker = "<!-- BEGIN LEETCODE STATS -->"
    end_marker = "<!-- END LEETCODE STATS -->"
    start_idx = readme_content.find(start_marker) + len(start_marker)
    end_idx = readme_content.find(end_marker)
    
    new_readme_content = (
        readme_content[:start_idx]
        + "\n" + open("leetcode_stats.md").read() + "\n"
        + readme_content[end_idx:]
    )
    
    with open("README.md", "w") as f:
        f.write(new_readme_content)
