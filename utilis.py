import openai
import pdfkit
from jinja2 import Environment, FileSystemLoader

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_ai_content(name, education, experience, skills):
    prompt = f"""
    Create a professional resume summary for:
    Name: {name}
    Education: {education}
    Experience: {experience}
    Skills: {skills}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']

def generate_resume_pdf(template, name, email, phone, linkedin, github, education, experience, skills, summary):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(f"{template}.html")
    
    html_content = template.render(
        name=name, email=email, phone=phone,
        linkedin=linkedin, github=github,
        education=education, experience=experience,
        skills=skills, summary=summary
    )
    
    pdf_file = f"{name}_Resume.pdf"
    pdfkit.from_string(html_content, pdf_file)
    with open(pdf_file, "rb") as f:
        return f.read()
