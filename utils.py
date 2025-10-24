import openai
import pdfkit
from jinja2 import Environment, FileSystemLoader

# ⚡ Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Generate AI Resume Summary
def generate_ai_content(name, education, experience, skills):
    prompt = f"""
    Create a professional resume summary for:
    Name: {name}
    Education: {education}
    Experience: {experience}
    Skills: {skills}
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error generating AI content: {e}"

# Generate PDF from HTML template
def generate_resume_pdf(template_name, context):
    try:
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template(f"{template_name}.html")
        html_content = template.render(context)

        # PDF file name
        pdf_file = f"{context['name'].replace(' ', '_')}_Resume.pdf"

        # Generate PDF (wkhtmltopdf must be installed)
        pdfkit.from_string(html_content, pdf_file)

        # Return PDF bytes for Streamlit download
        with open(pdf_file, "rb") as f:
            return f.read()
    except Exception as e:
        return None
