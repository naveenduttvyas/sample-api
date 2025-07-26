from core.agent_executor import run_pipeline

if __name__ == "__main__":
    issue_key = input("Enter Jira issue key: ")
    run_pipeline(issue_key)
