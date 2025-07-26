import os
from jira import JIRA


def fetch_jira_story(issue_key, config):
    # jira = JIRA(server=config["jira_url"], basic_auth=(config["jira_user"], config["jira_token"]))
    # issue = jira.issue(issue_key)
    print(f"[MOCK] Faking fetch for issue: {issue_key}")
    return {
        # "summary": issue.fields.summary,
        # "description": issue.fields.description,
        # "acceptance_criteria": issue.fields.customfield_12345  # Replace with actual field ID
        "summary": "Expose API to list all employees",
        "description": (
            "As a user, I want an API that returns all employees "
            "so that I can display them on the dashboard."
        ),
        "acceptance_criteria": (
            "API should return a list of employees in JSON. "
            "Endpoint should be GET /employees. "
            "Each employee should have id, name, email, department. "
            "Should return 200 OK with valid data. "
            "If no employees found, return empty list."
        ),
    }
