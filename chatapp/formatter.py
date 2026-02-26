import random


def clean_text(text):

    remove_titles = [
        "Company Name:",
        "Company Overview:",
        "Office Address:",
        "Services Provided:",
        "Work Environment:",
        "Career Opportunities:",
        "Working Hours:",
        "Clients and Industries:",
        "Mission:",
        "Vision:"
    ]

    for r in remove_titles:
        text = text.replace(r, "")

    return text.strip()


def format_answer(chunks, question):

    if not chunks:
        return "Sorry, I couldn’t find relevant information for that."

    greetings = [
        "Sure! Here's what I found:",
        "Absolutely 😊 Here's the information:",
        "Let me help you with that!",
        "Here’s the relevant information:",
        "Of course! Here you go:"
    ]

    intro = random.choice(greetings)

    cleaned_parts = []

    for chunk in chunks:
        cleaned = clean_text(chunk)
        if cleaned:
            cleaned_parts.append(cleaned)

    # Avoid too long replies (more human)
    cleaned_parts = cleaned_parts[:2]

    body = "\n".join(cleaned_parts)

    final_reply = f"{intro}\n\n{body}"

    return final_reply.strip()
