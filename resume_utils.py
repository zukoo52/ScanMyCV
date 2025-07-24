import re
import textstat
from pdfminer.high_level import extract_text as extract_pdf

def extract_text(filepath):
    if filepath.endswith(".pdf"):
        return extract_pdf(filepath)
    elif filepath.endswith(".txt"):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    else:
        return ""

def analyze_resume(text):
    score = 0
    tips = []
    breakdown = {}

    # Length Score
    words = len(text.split())
    if 500 <= words <= 1000:
        score += 20
        breakdown["Length"] = 20
    else:
        tips.append("Keep resume between 500–1000 words.")
        breakdown["Length"] = 10

    # Skills Score
    keywords = ["python", "sql", "flask", "leadership", "communication"]
    match_count = sum(1 for k in keywords if k.lower() in text.lower())
    if match_count >= 3:
        score += 20
        breakdown["Skills"] = 20
    else:
        tips.append("Add more relevant skills.")
        breakdown["Skills"] = 10

    # Readability
    readability = textstat.flesch_reading_ease(text)
    if readability >= 60:
        score += 20
        breakdown["Readability"] = 20
    else:
        tips.append("Simplify wording for better readability.")
        breakdown["Readability"] = 10

    # Formatting (Section check)
    if all(x in text.lower() for x in ["education", "experience", "skills"]):
        score += 20
        breakdown["Sections"] = 20
    else:
        tips.append("Include standard sections: Education, Experience, Skills.")
        breakdown["Sections"] = 10

# Bullet point usage check
    if text.count("•") + text.count("- ") < 3:
        tips.append("Use bullet points to list accomplishments clearly.")

    # Important section presence
    important_sections = ["education", "experience", "skills", "projects", "certifications"]
    for section in important_sections:
        if section not in text.lower():
            tips.append(f"Consider adding a '{section.capitalize()}' section.")

    # Buzzword repetition warning
    buzzwords = ["responsible", "managed", "developed", "worked"]
    for word in buzzwords:
        if text.lower().count(word) > 5:
            tips.append(f"'{word}' appears too frequently — vary your word choice to keep it impactful.")

    # Passive voice flag (very basic)
    if "was " in text.lower() or "were " in text.lower():
        tips.append("Avoid passive phrases like 'was' or 'were' — use active voice to show ownership.")

    # Email address check
    if not re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text):
        tips.append("Include a professional email address.")

    # Resume too short
    if words < 300:
        tips.append("Your resume is too short. Try to provide more content, especially achievements.")


    # Contact Info
    if re.search(r"[0-9]{10}", text) and "linkedin" in text.lower():
        score += 20
        breakdown["Contact Info"] = 20
    else:
        tips.append("Add phone number and LinkedIn profile.")
        breakdown["Contact Info"] = 10

    return score, breakdown, tips


