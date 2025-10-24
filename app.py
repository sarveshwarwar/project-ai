import streamlit as st
from utils import generate_resume_pdf, generate_ai_content

st.set_page_config(page_title="AI Resume Builder", layout="wide")

st.title("📝 AI-Powered Resume Builder")

# --- User Inputs ---
st.header("Personal Info")
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
linkedin = st.text_input("LinkedIn URL")
github = st.text_input("GitHub URL")

st.header("Education")
education = st.text_area("Enter your education details")

st.header("Work Experience")
experience = st.text_area("Enter your experience details")

st.header("Skills")
skills = st.text_area("Enter your skills (comma-separated)")

st.header("AI Resume Suggestions")
if st.button("Generate AI Summary"):
    summary = generate_ai_content(name, education, experience, skills)
    st.text_area("AI Generated Summary", summary, height=150)

# --- Template Selection ---
st.header("Choose Resume Template")
template_choice = st.selectbox("Template", ["template1", "template2"])

# --- Generate PDF ---
if st.button("Download Resume as PDF"):
    pdf_file = generate_resume_pdf(
        template_choice,
        name, email, phone, linkedin, github,
        education, experience, skills, summary
    )
    st.success("PDF Generated!")
    st.download_button(
        label="Download PDF",
        data=pdf_file,
        file_name=f"{name}_Resume.pdf",
        mime="application/pdf"
    )
