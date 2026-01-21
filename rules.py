# Rules for complaint classification

CATEGORIES = {
    "Infrastructure": ["road", "water", "electricity", "leakage", "building"],
    "Food": ["food", "mess", "quality", "hygiene", "stale"],
    "Safety": ["theft", "fight", "unsafe", "security", "harassment"]
}


def classify_complaint(text):
    """
    Classifies complaint text into a category using keyword matching
    """

    if not text.strip():
        return "Other"

    text = text.lower()

    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in text:
                return category

    return "Other"
