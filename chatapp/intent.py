def detect_intent(msg):

    m = msg.lower()

    # ---- Services ----
    if any(word in m for word in [
        "service", "services", "offer", "provide", "solution", "solutions"
    ]):
        return "services"

    # ---- About Company ----
    if any(word in m for word in [
        "about", "company", "who are you", "your company", "tell me about"
    ]):
        return "about"

    # ---- Working Hours ----
    if any(word in m for word in [
        "time", "working time", "hours", "office time", "working hours"
    ]):
        return "hours"

    # ---- Contact ----
    if any(word in m for word in [
        "contact", "reach", "call", "phone", "email", "whatsapp"
    ]):
        return "contact"

    # ---- Default ----
    return "general"
