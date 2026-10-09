# 📖 Book-Bite Action Agent

> **Turn procrastination and mental friction into zero-fluff, 1-minute action plans powered by world-class thinkers.**

[![AWS](https://img.shields.io/badge/AWS-Serverless-orange.svg)](https://aws.amazon.com/)
[![Amazon S3](https://img.shields.io/badge/Frontend-Amazon%20S3-569A31.svg)](https://aws.amazon.com/s3/)
[![AWS Lambda](https://img.shields.io/badge/Backend-AWS%20Lambda-FF9900.svg)](https://aws.amazon.com/lambda/)
[![Amazon Bedrock](https://img.shields.io/badge/AI-Amazon%20Bedrock-0073BB.svg)](https://aws.amazon.com/bedrock/)
[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen.svg)](https://book-bite-frontend-2026.s3.us-east-1.amazonaws.com/index.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## 🚀 Live Demo

Experience the agent running live in production:  
🔗 **[Book-Bite Action Agent Web App](https://book-bite-frontend-2026.s3.us-east-1.amazonaws.com/index.html)**

---

## 💡 Overview

Standard chatbots often provide verbose, generic, or passive advice that increases cognitive fatigue. **Book-Bite** was built for the **AWS Build an Agent Weekend Challenge** to deliver an immediate, delightful experience:

- **Zero Fluff:** Tactical, concise advice designed to be read in under 60 seconds.
- **Dynamic Persona Injection:** Adopts the exact voice, philosophy, and framework of chosen authors (e.g., James Clear, Robert Greene, Mark Manson) or a generalized best-practice advisor.
- **Frictionless Testing:** Interactive Quick-Fill chips allow users to test challenges like *Tech Overwhelm*, *Procrastination*, and *Perfectionism* with one click.

---

## 🏗️ AWS Services Used
The application is built 100% serverless using AWS Free Tier services:

1. **Frontend Hosting (Amazon S3):**  
   The single-page web interface (`index.html`) is hosted directly on an **Amazon S3** bucket configured for static website hosting, providing high availability with zero server management.
2. **API Layer (Amazon API Gateway):**  
   Serves as the secure public REST API gateway with CORS enabled (`OPTIONS` and `POST` methods) to receive frontend queries.
3. **Compute Engine (AWS Lambda):**  
   A serverless **Python 3.12** Lambda function handles input validation, dynamic prompt engineering based on the selected author persona, and model invocation.
4. **Foundational Model (Amazon Bedrock):**  
   Powers the intelligence layer via Anthropic Claude 3 Haiku (`us.anthropic.claude-haiku-4-5-20251001-v1:0`), chosen for ultra-fast response times and high instruction compliance.

---

## 📂 Repository Structure

```text
book-bite-action-agent/
│
├── frontend/
│   └── index.html          # Glassmorphism UI, suggestion chips & Marked.js parser
│
├── backend/
│   └── lambda_function.py  # Python backend with dynamic author prompt engineering
└── README.md
