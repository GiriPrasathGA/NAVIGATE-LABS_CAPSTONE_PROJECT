# AI-Powered Regulatory Loan Evaluation Assistant (FDIC Section 3.2)

## Overview
This project is a prompt-engineering–driven regulatory reasoning assistant designed to support **bank loan officers** in interpreting supervisory expectations under the **FDIC RMS Manual of Examination Policies – Section 3.2 (Loans)**.

The system does **not** automate loan approvals, rejections, pricing, or credit decisions. Instead, it provides **document-grounded, examiner-focused regulatory analysis** suitable for audit and compliance review.

---

## Key Objectives
- Demonstrate how **prompt engineering alone** can control LLM behavior in regulated banking environments
- Enforce **single-source regulatory grounding** using FDIC Section 3.2
- Prevent hallucinations, unsupported assumptions, and automated credit decisions
- Support **loan officer regulatory interpretation**, not underwriting or advisory tasks

---

## Scope and Constraints
The assistant is explicitly designed to:
- Analyze loan-related questions and inputs under FDIC Section 3.2
- Explain regulatory concepts defined in the policy
- Identify applicable sections and subsections
- Flag missing information or potential policy deviations
- Acknowledge when regulatory guidance is insufficient or out of scope

The assistant explicitly does **not**:
- Approve or reject loans
- Assign credit scores, risk ratings, or pricing
- Provide financial, business, or operational advice
- Use external knowledge or non-FDIC sources

---

## Regulatory Source of Truth
- **FDIC RMS Manual of Examination Policies – Section 3.2 (Loans)**  
  This document is treated as the **single and exclusive authoritative source** for all responses.

---

## Evaluation Methodology
The project includes an automated evaluation notebook that:
- Assesses **system prompt quality** (task clarity, constraint enforcement, document grounding)
- Assesses **response quality** against regulatory ground truth
- Uses lightweight judge models to validate prompt effectiveness rather than model intelligence

This ensures behavior is driven by **prompt design**, not model capability.

---

## Project Files
- `Loan_Regulatory_Reasoning_Assistant.ipynb`  
  Main notebook containing prompt definitions, evaluation logic, and scoring
- `manualy_converted_text.txt`  
  Extracted regulatory reference text used for grounding
- `section3-2.pdf`  
  FDIC RMS Manual – Section 3.2 (Loans)

---

## Intended Users
- Bank loan officers
- Compliance and risk teams
- Regulatory and supervisory review contexts
- Academic and training environments focused on regulated AI systems

---

## Disclaimer
This project is for **educational and demonstrative purposes only**.  
It does not constitute legal, regulatory, financial, or lending advice.

---

## Author
Capstone Project – Navigate Labs  
Prompt Engineering for Regulated Financial Systems
