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
education = st.text_area("Education details")

st.header("Work Experience")
experience = st.text_area("Experience details")

st.header("Skills")
skills = st.text_area("Skills (comma-separated)")

# --- AI Summary ---
summary = ""
if st.button("Generate AI Summary"):
    summary = generate_ai_content(name, education, experience, skills)
    st.text_area("AI Generated Summary", summary, height=150)

# --- Template Selection ---
st.header("Choose Resume Template")
template_choice = st.selectbox("Template", ["template1", "template2"])

# --- Generate PDF ---
if st.button("Download Resume as PDF"):
    context = {
        "name": name, "email": email, "phone": phone,
        "linkedin": linkedin, "github": github,
        "education": education, "experience": experience,
        "skills": skills, "summary": summary
    }
    pdf_bytes = generate_resume_pdf(template_choice, context)
    if pdf_bytes:
        st.download_button(
            label="Download PDF",
            data=pdf_bytes,
            file_name=f"{name.replace(' ', '_')}_Resume.pdf",
            mime="application/pdf"
        )
    else:
        st.error("PDF generation failed. Make sure wkhtmltopdf is installed.")
