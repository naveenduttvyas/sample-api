import google.generativeai as genai


def generate_code(prompt, config):
    genai.configure(api_key=config["gemini_api_key"])
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text
