import streamlit as st
from PyPDF2 import PdfReader
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

st.sidebar.title("AI Resume Analyzer")

st.sidebar.write(
    "Upload your resume and get ATS analysis"
)

st.title("📄 AI Resume Analyzer")

st.write("Analyze your resume instantly")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file:

    st.success("✅ Resume uploaded successfully!")

    pdf = PdfReader(uploaded_file)

    text = ""

    for page in pdf.pages:
        text += page.extract_text()

    st.subheader("📑 Resume Content")

    st.write(text)

    skills = [
        "Python",
        "Java",
        "C",
        "C++",
        "HTML",
        "CSS",
        "JavaScript",
        "SQL",
        "Machine Learning",
        "Communication"
    ]

    found_skills = []

    for skill in skills:

        if skill.lower() in text.lower():

            found_skills.append(skill)

    st.subheader("💡 Skills Detected")

    st.write(found_skills)

    score = len(found_skills) * 10

    if score > 100:
        score = 100

    st.subheader("🎯 ATS Score")

    st.progress(score)

    st.metric(
        label="Resume Score",
        value=f"{score}%"
    )

    suggestions = []

    if "project" not in text.lower():
        suggestions.append("Add Projects Section")

    if "github" not in text.lower():
        suggestions.append("Add GitHub Profile")

    if "skill" not in text.lower():
        suggestions.append("Add Skills Section")

    if "internship" not in text.lower():
        suggestions.append("Add Internship Experience")

    st.subheader("🚀 Suggestions to Improve Resume")

    for suggestion in suggestions:
        st.write("✔", suggestion)
        st.subheader("📊 Skill Analysis Chart")

    skill_count = [1] * len(found_skills)

    fig, ax = plt.subplots()

    ax.bar(found_skills, skill_count)

    ax.set_xlabel("Skills")

    ax.set_ylabel("Detected")

    ax.set_title("Detected Skills")

    st.pyplot(fig)
    st.subheader("💼 Recommended Job Role")

    if "Python" in found_skills and "SQL" in found_skills:
        st.success("Python Developer")

    elif "HTML" in found_skills and "CSS" in found_skills:
        st.success("Frontend Developer")

    elif "Machine Learning" in found_skills:
        st.success("Machine Learning Engineer")

    elif "Java" in found_skills:
        st.success("Java Developer")

    else:
        st.warning("Skill data insufficient for role prediction")



