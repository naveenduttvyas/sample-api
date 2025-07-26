from jira import JIRA


def update_jira_ticket(issue_key, comment, config):
    jira = JIRA(
        server=config["jira_url"],
        basic_auth=(config["jira_user"], config["jira_token"]),
    )
    jira.add_comment(issue_key, comment)
    jira.transition_issue(issue_key, "Done")  # Use correct transition ID
