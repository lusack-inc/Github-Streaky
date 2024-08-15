# Github-Streaky

Github Streaky is a Python script that helps you maintain your GitHub contribution streak. It checks if you've made any commits for the day and, if not, automatically updates a specified repository's README file to record the date you missed. This ensures you never miss a day in your contribution streak. It's cheeky, so we call it Github Streaky 🤦‍♂️

## Features

Daily Check: Automatically checks your GitHub account for commits made on the current day.

Auto Update: If no commits are found, it updates a specified repository's README with the date you missed.

GitHub Actions Integration: Runs daily using GitHub Actions, ensuring the script executes even when your computer is off.

Secure: Sensitive information like your GitHub token is securely stored using GitHub Secrets

## Getting Started
### Prerequisites

    - Python 3.x
    - GitHub account
    - A GitHub repository where the script will record missed contribution dates

### Installation

1. Clone the Repository:
    
```bash
    git clone https://github.com/Ajit-Mehrotra/Github-Streaky.git
    cd Github-Streaky
```

2. Set Up Virtual Environment (Optional but Recommended):

```bash
    python -m venv venv
    venv\Scripts\activate # On Mac use `source venv/bin/activate`
```
3. Install Dependencies:

```bash
       pip install -r requirements.txt
 ```
4. Create a .env File:
    
Create a .env file in the root directory and add the following:

```sh
        USERNAME=your_github_username
        REPO_NAME=your_repository_name
        ACCESS_TOKEN=your_github_access_token
```
> Note: The .env file should be gitignored for security reasons. It's added by default when you clone, but you should always double check.   

### Usage

1. Run the Script Locally:

You can manually run the script using:
```bash
python main.py
```
This will check if you've made any commits today and update the README file if no commits are found.

2. Automate with GitHub Actions

To run the script daily at 11:50 PM, follow these steps:

- Set Up GitHub Secrets:

    - Go to your repository's Settings > Secrets and variables > Actions, and add the following secrets:
        - USERNAME
        - REPO_NAME
        - ACCESS_TOKEN

- Create a GitHub Actions Workflow:
    - In your repository, create the file .github/workflows/schedule.yml with the following content:
    ```yaml
    name: Daily Contribution Check

    on:
    schedule:
        - cron: '50 23 * * *'  # Runs every day at 11:50 PM UTC

    jobs:
    check-contributions:
        runs-on: ubuntu-latest
        
        steps:
        - name: Checkout code
        uses: actions/checkout@v3

        - name: Set up Python
        uses: actions/setup-python@v4
        with:
            python-version: '3.x'
        
        - name: Install dependencies
        run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt

        - name: Run contribution check script
        env:
            GITHUB_USERNAME: ${{ secrets.GITHUB_USERNAME }}
            REPO_NAME: ${{ secrets.REPO_NAME }}
            GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
            python main.py
    ```
### Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to discuss improvements or bugs.
   
### Acknowledgements

[PyGithub](https://github.com/PyGithub/PyGithub)  - Used for interacting with the GitHub API.