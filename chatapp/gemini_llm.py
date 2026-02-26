import google.generativeai as genai
from companies.models import GeminiConfig


def get_active_gemini():

    config = GeminiConfig.objects.filter(active=True).first()

    if not config:
        raise Exception("No active Gemini configuration found in admin!")

    genai.configure(api_key=config.api_key)

    model = genai.GenerativeModel(config.model_name)

    return model


def generate_human_reply(context, user_message):

    model = get_active_gemini()

    prompt = f"""
You are a professional AI chatbot for a company.

Use the company information below to answer smartly and politely.

Company Information:
{context}

User Message:
{user_message}

Rules:
- Be friendly and human-like
- Keep answers clear and professional
- If user greets, greet back
- If working time missing, say 09:00 AM to 05:30 PM
- If contact missing, only mention available ones
"""

    response = model.generate_content(prompt)

    return response.text.strip()
