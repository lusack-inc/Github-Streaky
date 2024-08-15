import os
from datetime import datetime
from dotenv import load_dotenv
from github import Github, GithubException


# Load environment variables
load_dotenv()
GITHUB_USERNAME = os.getenv("USERNAME")
REPO_NAME = os.getenv("REPO_NAME")
GITHUB_TOKEN = os.getenv("ACCESS_TOKEN")

g = Github(GITHUB_TOKEN)
user = g.get_user()
today = datetime.now().date()


# Fetch user and see contributions
def made_contribution() -> bool:
    repos = user.get_repos()
    for repo in repos:
        try:
            commits = repo.get_commits()
            for commit in commits:
                commit_date = commit.commit.author.date.date()
                if commit_date == today:
                    print(f"Repo: {repo.name}, Commit: {commit.sha}")
                    return True
        except GithubException as e:
            # 409 is an empty repository which throws an error.
            if e.status == 409:
                print(f"Skipping {repo.name}: Repository is empty.")
            else:
                print(f"Error: {e}")
    return False


def update_readme():
    readme_log = f"No contributions made on {today}."

    # Relevant Documentation: https://pygithub.readthedocs.io/en/stable/github_objects/Repository.html

    repo = user.get_repo(REPO_NAME)
    readme = repo.get_readme()
    decoded_readme = readme.decoded_content.decode("utf-8")
    new_content = f"{decoded_readme}\n{readme_log}"
    repo.update_file(
        readme.path, f"Updated README.md on {today}", new_content, readme.sha
    )

    print(readme)


if __name__ == "__main__":
    if made_contribution():
        print("Contributions made today!")
    else:
        print("No contributions made today.")
        update_readme()
        print("Updated README.md")
