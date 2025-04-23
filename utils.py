import re
import spacy

nlp = spacy.load("en_core_web_sm")

def mask_pii(text):
    entities = []
    masked_text = text
    replacements = []

    # Step 1: Named Entity Recognition (spaCy)
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            replacements.append((ent.start_char, ent.end_char, "[full_name]", "full_name", ent.text))

    # Step 2: Regex Patterns
    patterns = {
        "email": r"[a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+",
        "phone_number": r"\b\d{10}\b",
        "dob": r"\b\d{2}[-/]\d{2}[-/]\d{4}\b",
        "aadhar_num": r"\b\d{4}\s\d{4}\s\d{4}\b",
        "credit_debit_no": r"\b(?:\d[ -]*?){13,16}\b",
        "cvv_no": r"\b\d{3}\b",
        "expiry_no": r"\b(0[1-9]|1[0-2])\/?([0-9]{2}|[0-9]{4})\b"
    }

    for key, pattern in patterns.items():
        for match in re.finditer(pattern, text):
            start, end = match.start(), match.end()
            tag = f"[{key}]"
            replacements.append((start, end, tag, key, match.group()))

    # Step 3: Apply replacements in reverse
    replacements.sort(reverse=True)
    for start, end, tag, label, original in replacements:
        masked_text = masked_text[:start] + tag + masked_text[end:]
        entities.append({
            "position": [start, end],
            "classification": label,
            "entity": original
        })

    return masked_text, entities
