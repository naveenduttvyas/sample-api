import yaml
from agents import (
    jira_fetcher,
    prompt_generator,
    gemini_codegen,
    repo_writer,
    test_writer,
    linter_agent,
    github_committer,
    jira_updater,
)


def run_pipeline(issue_key):
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)

    story = jira_fetcher.fetch_jira_story(issue_key, config)
    prompt = prompt_generator.generate_prompt(story)
    code = gemini_codegen.generate_code(prompt, config)

    code_path = "src/api/employees.py"
    repo_writer.write_code_to_repo(code, code_path)

    test_code = test_writer.generate_unit_tests("/employees")
    repo_writer.write_code_to_repo(test_code, "tests/test_employees.py")

    linter_agent.run_linters(".")

    github_committer.commit_and_push(".", f"Implemented: {story['summary']}")
    jira_updater.update_jira_ticket(
        issue_key, "Code pushed with tests. Closing story.", config
    )
