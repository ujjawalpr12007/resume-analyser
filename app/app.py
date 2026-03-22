import streamlit as st
import fitz  # PyMuPDF
import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.parser import (
    clean_text,
    compute_similarity,
    extract_skills,
    compare_skills,
    compute_skill_score
)

# -------------------------------
# 📄 PDF TEXT EXTRACTION (FIXED)
# -------------------------------
def extract_text_from_pdf(file):
    text = ""
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    
    for page in pdf:
        text += page.get_text()
    
    return text


# -------------------------------
# 🎨 PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Resume Analyzer", layout="centered")

st.title("📄 Resume Analyzer")
st.markdown("Analyze your resume against a job description and improve your chances 🚀")

# -------------------------------
# 📂 INPUTS
# -------------------------------
st.subheader("📂 Upload Resume")
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

st.subheader("📝 Paste Job Description")
job_desc = st.text_area("Enter job description here...")

# -------------------------------
# 🚀 MAIN LOGIC
# -------------------------------
if resume_file and job_desc:

    with st.spinner("Analyzing resume..."):

        # Extract + clean
        resume_text = extract_text_from_pdf(resume_file)
        resume_clean = clean_text(resume_text)
        job_clean = clean_text(job_desc)

        # TF-IDF score
        tfidf_score = compute_similarity(resume_clean, job_clean)

        # Skills
        resume_skills = extract_skills(resume_clean)
        job_skills = extract_skills(job_clean)

        matched, missing = compare_skills(resume_skills, job_skills)

        # Skill score
        skill_score = compute_skill_score(matched, job_skills)

        # Final score
        final_score = round((tfidf_score * 0.4) + (skill_score * 0.6), 2)

    # -------------------------------
    # 📊 SCORE
    # -------------------------------
    st.subheader(f"📊 Match Score: {final_score}%")
    st.progress(final_score / 100)

    if final_score >= 75:
        st.success("🔥 Excellent match! You're a strong candidate.")
    elif final_score >= 50:
        st.warning("⚠️ Moderate match. Improve a few key skills.")
    else:
        st.error("❌ Low match. Focus on missing skills.")

    # -------------------------------
    # 🔍 BREAKDOWN
    # -------------------------------
    st.markdown("### 🔍 Score Breakdown")
    st.write(f"• TF-IDF Similarity: {tfidf_score}%")
    st.write(f"• Skill Match Score: {skill_score}%")

    # -------------------------------
    # 🧠 SKILLS
    # -------------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ✅ Matched Skills")
        if matched:
            for skill in matched:
                st.success(skill.upper())
        else:
            st.info("No matched skills found")

    with col2:
        st.markdown("### ❌ Missing Skills")
        if missing:
            for skill in missing:
                st.error(skill.upper())
        else:
            st.success("No missing skills 🎉")

    # -------------------------------
    # 💡 SUGGESTIONS
    # -------------------------------
    if missing:
        st.markdown("### 💡 Suggestions to Improve")
        for skill in missing:
            st.write(f"👉 Learn **{skill}**")

    # -------------------------------
    # 📌 FINAL INSIGHT
    # -------------------------------
    st.markdown("### 📌 Final Insight")

    if final_score >= 75:
        st.write("You are well-aligned with this role. Start applying confidently.")
    elif final_score >= 50:
        st.write("You meet several requirements but can improve further.")
    else:
        st.write("You need to significantly improve your skill set for this role.")