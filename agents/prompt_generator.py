def generate_prompt(story):
    return f"""
You are an expert Python developer. Write a FastAPI endpoint based on the story:

Summary: {story['summary']}

Description:
{story['description']}

Acceptance Criteria:
{story['acceptance_criteria']}

Ensure:
- RESTful design
- Typing hints
- Unit tests
- Clean code practices
"""
