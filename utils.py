from weasyprint import HTML
import tempfile
import os
from jinja2 import Template
import openai

# ✅ Generate AI content for resume sections
def generate_ai_content(prompt, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that creates professional resume text."},
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message["content"].strip()

# ✅ Generate a PDF resume using WeasyPrint (no wkhtmltopdf needed)
def generate_resume_pdf(html_content, output_path):
    try:
        HTML(string=html_content).write_pdf(output_path)
        return True
    except Exception as e:
        print("PDF generation failed:", e)
        return False

