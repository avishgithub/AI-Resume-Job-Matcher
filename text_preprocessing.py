import re


def clean_text(text):
    """
    CLean and standardize resume text.
    """

    text = text.lower()
    text = re.sub(r"[^a-z0-9+#./\s-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = text.strip()

    return text


def tokenize_text(text):
    """
    Split clean text into individual words.
    """

    tokens = text.split()
    return tokens
