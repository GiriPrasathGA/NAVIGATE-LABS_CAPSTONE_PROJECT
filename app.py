import os
import json
import gradio as gr
import pytesseract
from PIL import Image
from openai import OpenAI
from dotenv import load_dotenv

# --- CONFIGURATION & SETUP ---

# Load environment variables from .env file
load_dotenv()

# If you are on Windows and Tesseract is not in your PATH, 
# uncomment the following line and point it to your tesseract.exe
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# OpenAI-compatible API Setup
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL", "https://apidev.navigatelabsai.com")
)

MODEL_NAME = "gpt-4.1-nano"

# --- DATA LOADING ---

def load_fdic_policy(file_path):
    """Loads the FDIC policy text from a file."""
    if not os.path.exists(file_path):
        print(f"Warning: {file_path} not found. Using empty string.")
        return ""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# Load the full text from the manually converted file
FDIC_SECTION_3_2 = load_fdic_policy("manualy_converted_text.txt")

SYSTEM_PROMPT_v1 = """
#SYSTEM/ROLE PROMPT
You are a regulatory loan examining assistant.
Your role is to analyze loan-related documents and questions strictly under FDIC RMS Manual Section 3.2 (Loans).

#CONTEXT PROMPT
The provided section 3.2 policy text is the one and only complete authoritative source of information. You must never rely on external knowledge, assumptions or general loan details. You must not refer any other website or external policy documents rather than section 3.2

#INSTRUCTION BASED PROMPT
You need to determine whether the given input is applicable to section 3.2
You need to indicate when the policy does not provide enough guidance.
You must map the input with its relevant subsections in the section 3.2 policy document if applicable.
You must flag missing information or policy deviation

#CONSTRAINT PROMPT
You must never approve or reject the loan.
You must never recommend actions,pricing and terms.
You must never change the policies sections,terms and conditions.
You must never give any kind of advice.
You must never assume facts which is not in the input.
You must never create requirement or conclusions which is not in the section 3.2 policy.

You should clearly mention out of scope response if the input falls outside the section 3.2 policy in kind and professional tone.

#OUTPUT CONTROL PROMPT
Your response must be neutral,objective and professional.Avoid friendy,instructional,advisory language.Avoid long paragraphs.
Acknowledge uncertainty where regulatory guidance is insufficient.
"""

# --- CORE LOGIC ---

def chatbot_response(user_query, application_form_data):
    """Interacts with the LLM to provide regulatory reasoning."""
    messages = [
        {
            "role": "system",
            "content": f"FDIC RMS Manual Section 3.2:\n{FDIC_SECTION_3_2}"
        },
        {
            "role": "system",
            "content": SYSTEM_PROMPT_v1
        },
    ]

    if application_form_data.strip():
        messages.append({
            "role": "system",
            "content": f"Applicant Loan Form (use only if relevant):\n{application_form_data}"
        })

    messages.append({
        "role": "user",
        "content": user_query
    })

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0,
            max_tokens=800
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error during API call: {str(e)}"

def gradio_handler(application_file, user_query):
    """Handles Gradio inputs, processes OCR, and calls the chatbot."""
    application_text = ""

    if application_file is not None:
        try:
            image = Image.open(application_file)
            application_text = pytesseract.image_to_string(image)
        except Exception as e:
            return f"Error during OCR processing: {str(e)}. Please ensure Tesseract is installed."

    return chatbot_response(user_query, application_text)

# --- UI DESIGN ---

custom_css = """
.gradio-container {
    background-color: #111827;
    color: #e5e7eb;
}

.gradio-container {
    font-family: Inter, Segoe UI, sans-serif;
}

/* GENERAL CARD */
.card {
    background: #1f2937;
    border: 1px solid #374151;
    border-radius: 14px;
    padding: 12px;
    box-shadow: 0 10px 28px rgba(0,0,0,0.4);
    margin-bottom: 8px;
    color: #e5e7eb;
}

/* TOP HEADER CARD (SPECIAL) */
.header-card {
    background: #1f2937;
    border: 1px solid #374151;
    border-radius: 14px;
    padding: 22px;
    box-shadow: 0 10px 28px rgba(0,0,0,0.4);
    margin-bottom: 16px;
    color: #e5e7eb;
}

/* HEADER TEXT */
.header {
    font-size: 28px;
    font-weight: 700;
    color: #e5e7eb;
}

/* SUBHEADER TEXT */
.subheader {
    font-size: 14px;
    color: #e5e7eb;
    margin-top: 6px;
}
"""

with gr.Blocks() as demo:

    # HEADER
    gr.HTML("""
<div class="header-card">
    <div class="header">FDIC Loan Regulatory Reasoning Assistant</div>
    <div class="subheader">
        Regulatory-aligned observations based strictly on FDIC RMS Manual Section 3.2.<br>
        <b>This system does not approve or reject loans.</b>
    </div>
</div>
""")

    with gr.Row():

        # INPUT PANEL
        with gr.Column(scale=1):
            gr.HTML("<div class='card'><h3>📄 Inputs</h3>")

            application_file = gr.File(
                label="Loan Application Form (Image Upload)",
                file_types=[".png", ".jpg", ".jpeg"]
            )

            user_query = gr.Textbox(
                label="Regulatory Question",
                placeholder="e.g., Identify documentation gaps under FDIC Section 3.2",
                lines=4
            )

            submit_btn = gr.Button(
                "Run Regulatory Analysis",
                variant="primary"
            )

            gr.HTML("</div>")

        # OUTPUT PANEL
        with gr.Column(scale=2):
            gr.HTML("<div class='card'><h3>📊 FDIC Section 3.2 Regulatory Analysis</h3>")

            output = gr.Textbox(
                lines=20,
                placeholder="Regulatory observations will appear here..."
            )

            gr.HTML("</div>")

    submit_btn.click(
        fn=gradio_handler,
        inputs=[application_file, user_query],
        outputs=output
    )

# --- MAIN BLOCK ---

if __name__ == "__main__":
    print("Starting FDIC Regulatory Assistant...")
    demo.launch(debug=True, share=False, css=custom_css, theme=gr.themes.Soft())
