# 📄 Resume Analyzer (AI-Powered)

An interactive web application that analyzes a resume against a job description and provides a **match score, skill gap analysis, and improvement suggestions**.

🔗 Live App: https://resume-analyser-bvklchceeitigpo62ekszr.streamlit.app

---

## 🚀 Features

- 📊 **Match Score Calculation**
  - Combines TF-IDF similarity and skill-based matching
- 🧠 **Skill Extraction**
  - Identifies relevant technical skills from resume and job description
- ✅ **Matched Skills**
  - Highlights skills aligned with the job requirements
- ❌ **Missing Skills**
  - Shows gaps that need improvement
- 💡 **Suggestions**
  - Provides actionable recommendations to improve job fit
- 🌐 **Interactive UI**
  - Built with Streamlit for real-time analysis

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (Frontend + Deployment)
- **Scikit-learn** (TF-IDF, similarity)
- **PyMuPDF (fitz)** (PDF text extraction)
- **RapidFuzz** (robust skill matching)

---

## ⚙️ How It Works

1. Upload a resume (PDF)
2. Paste a job description
3. The system:
   - Extracts and cleans text
   - Computes semantic similarity (TF-IDF)
   - Extracts and compares skills
4. Outputs:
   - Match score
   - Skill match breakdown
   - Suggestions for improvement

---

## 📊 Scoring Methodology

Final Score is calculated as:
Final Score = (0.4 × TF-IDF Similarity) + (0.6 × Skill Match Score)

- **TF-IDF Similarity** → Measures textual similarity
- **Skill Match Score** → Measures overlap of required skills

---

## ⚠️ Limitations

- PDF parsing may vary depending on formatting
- Skill extraction is keyword-based and may miss implicit skills
- Designed for demonstration and learning purposes

---

## 🔮 Future Improvements

- Improve skill extraction using NLP models (spaCy / transformers)
- Add support for multiple resumes comparison
- Enhance UI with advanced visualizations
- Deploy using Docker / cloud services

---

## 👤 Author

**Ujjawal Matolia**

- LinkedIn: https://linkedin.com/in/ujjawalmatolia  
- GitHub: https://github.com/ujjawalpr12007  
