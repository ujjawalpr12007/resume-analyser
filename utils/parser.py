import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Extract text from PDF
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# Clean text
def clean_text(text):
    text = text.lower()
    return text

# Compute similarity score
def compute_similarity(resume, job_desc):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume, job_desc])
    similarity = cosine_similarity(vectors[0], vectors[1])
    return round(similarity[0][0] * 100, 2)

# Skill list
skills_list = {
    "python": ["python"],
    "sql": ["sql"],
    "machine learning": ["machine learning", "ml"],
    "data analysis": ["data analysis", "data analytics"],
    "numpy": ["numpy"],
    "pandas": ["pandas"],
    "tableau": ["tableau"],
    "deep learning": ["deep learning", "dl"],
}

# Extract skills
import re

from rapidfuzz import fuzz

def extract_skills(text):
    found = []
    text = text.lower()

    for skill, variations in skills_list.items():
        for variant in variations:
            variant = variant.lower()

            # fuzzy match score
            score = fuzz.partial_ratio(variant, text)

            if score > 80:  # threshold
                found.append(skill)
                break

    return list(set(found))

# Compare skills
def compare_skills(resume_skills, job_skills):
    matched = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))
    return matched, missing

def compute_skill_score(matched, job_skills):
    if not job_skills:
        return 0
    return round((len(matched) / len(job_skills)) * 100, 2)
