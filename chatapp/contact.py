import re

def extract_contact(chunks):

    text = " ".join(chunks)

    phone_match = re.findall(r"\+?\d{10,13}", text)
    email_match = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)

    phone = phone_match[0] if phone_match else None
    email = email_match[0] if email_match else None

    whatsapp = None
    if phone:
        whatsapp = f"https://wa.me/{phone.replace('+','')}"

    return phone, email, whatsapp


def contact_response(chunks):

    phone, email, whatsapp = extract_contact(chunks)

    buttons = []
    details = []

    if phone:
        buttons.append({
            "label": "📞 Call Now",
            "url": f"tel:{phone}"
        })
        details.append(f"Phone: {phone}")

    if whatsapp:
        buttons.append({
            "label": "💬 WhatsApp",
            "url": whatsapp
        })

    if email:
        buttons.append({
            "label": "📧 Email",
            "url": f"mailto:{email}"
        })
        details.append(f"Email: {email}")

    if not buttons:
        return {
            "text": "Sorry, contact information is not available at the moment.",
            "buttons": [],
            "details": ""
        }

    return {
        "text": "You can reach us using the following options:",
        "buttons": buttons,
        "details": "\n".join(details)
    }
