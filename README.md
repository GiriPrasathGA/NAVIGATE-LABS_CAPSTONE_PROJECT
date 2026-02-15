# AI-Powered Regulatory Loan Evaluation Assistant (FDIC Section 3.2)

## Overview
This project is a prompt-engineering–driven regulatory reasoning assistant designed to support **bank loan officers** in interpreting supervisory expectations under the **FDIC RMS Manual of Examination Policies – Section 3.2 (Loans)**.

The system is now a **standalone Python application** with a polished **Gradio web interface**, designed for secure and efficient regulatory analysis.

---

## Key Features
- **Standalone Application**: Transitioned from Jupyter notebook to a high-performance Python script (`app.py`).
- **Secure Configuration**: Uses `.env` for API key and base URL management, ensuring credentials are never exposed in source control.
- **Intelligent File Handling**: 
  - Direct text extraction for **PDF** and **TXT** files for maximum accuracy.
  - Integrated **Tesseract OCR** for image-based documents and scans.
- **Gradio Web Interface**: Modern, responsive UI with real-time analysis and regulatory observation outputs.
- **Regulatory Grounding**: Enforces strict adherence to the **FDIC RMS Manual – Section 3.2** to prevent hallucinations.

---

## Technical Objectives
- Demonstrate how **prompt engineering alone** can control LLM behavior in regulated banking environments.
- Enforce **single-source regulatory grounding** using the extracted FDIC Section 3.2 text.
- Provide **document-grounded analysis** suitable for audit and compliance review.

---

## Scope and Constraints
The assistant is explicitly designed to:
- Analyze loan-related inputs under FDIC Section 3.2.
- Explain regulatory concepts and identify applicable subsections.
- Flag missing information or potential policy deviations.

The assistant explicitly does **not**:
- Approve or reject loans or provide financial advice.
- Use external knowledge beyond the provided FDIC source.

---

## Regulatory Source of Truth
- **FDIC RMS Manual of Examination Policies – Section 3.2 (Loans)**  
  Grounding is provided via `manualy_converted_text.txt`, which contains the full extracted regulatory text.

---

## Setup and Installation

### Prerequisites
- Python 3.8+
- Tesseract OCR (Optional, for image processing)

### Installation
1. Clone the repository and navigate to the project folder.
2. Initialize and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
   *(Note: Ensure `gradio`, `openai`, `pdfplumber`, `pytesseract`, and `python-dotenv` are installed)*

4. Create a `.env` file in the root directory:
   ```env
   API_KEY=your_api_key_here
   BASE_URL=your_api_base_url_here
   ```

---

## Running the Application
To launch the assistant, run:
```powershell
python app.py
```
Access the web interface at `http://127.0.0.1:7860`.

---

## Project Structure
- `app.py`: Main application script (Gradio UI + LLM Logic).
- `manualy_converted_text.txt`: Extracted regulatory reference text.
- `.env`: (Local only) Secure credentials.

---

## Disclaimer
This project is for **educational and demonstrative purposes only**. It does not constitute legal or financial advice.

---

## Author
Capstone Project – Navigate Labs  
Prompt Engineering for Regulated Financial Systems

