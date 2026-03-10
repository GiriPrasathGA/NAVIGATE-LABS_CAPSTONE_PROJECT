# FDIC Loan Regulatory Reasoning Assistant

An AI-powered regulatory compliance tool designed to interpret the **FDIC RMS Manual – Section 3.2 (Loans)**. This assistant helps users understand regulatory expectations, identify documentation gaps, and highlight areas requiring clarification under FDIC guidance.

## 🚀 Features

- **Grounded Reasoning**: System responses are strictly mapped to FDIC Section 3.2 policies.
- **OCR Integration**: Extract text from loan applications (images) for regulatory analysis.
- **Compliance Guardrails**: Explicitly avoids loan approval, rejection, or recommendations.
- **Automated Evaluation**: Built-in Judge-LLM pipeline to evaluate accuracy, faithfulness, and professional tone.
- **Interactive Dashboard**: Professional Gradio-based web interface.

## 🛠️ Installation

### 1. Prerequisites
- **Python 3.10+**
- **Tesseract OCR**: Required for image-to-text processing.
  - **Windows**: [Install Tesseract](https://github.com/UB-Mannheim/tesseract/wiki) and add it to your PATH.
  - **Linux**: `sudo apt-get install tesseract-ocr`

### 2. Setup Environment
Clone the repository and install the required Python libraries:

```bash
pip install -r requirements.txt
```

*Note: Ensure you have an OpenAI API Key or a compatible local model endpoint.*

## 📖 Usage

1. Open the `Loan_Regulatory_Reasoning_Assistant.ipynb` notebook.
2. Provide your API configuration in the `API Setup` cell.
3. Run all cells to launch the **Gradio Dashboard**.
4. **Upload** a loan application image or **Enter** a regulatory query to receive FDIC-aligned observations.

## 🏗️ Architecture

1. **Input Layer**: Text queries or Application form images (via OCR).
2. **Context Engine**: Injects FDIC Section 3.2 text as the primary source of truth.
3. **Logic Layer**: LLM applies system prompt constraints to generate neutral, examiner-style responses.
4. **Evaluation Layer**: Analyzes responses against ground truth rubrics and visualizes performance.

## ⚖️ Disclaimer

This tool is for educational and regulatory reasoning assistance only. It does not provide financial advice, nor does it approve or reject loan applications.
