# 📖 Book-Bite Action Agent

> **Turn procrastination and mental friction into zero-fluff, 1-minute action plans powered by world-class thinkers.**

[![AWS](https://img.shields.io/badge/AWS-Serverless-orange.svg)](https://aws.amazon.com/)
[![Bedrock](https://img.shields.io/badge/Amazon%20Bedrock-Claude%20Haiku-purple.svg)](https://aws.amazon.com/bedrock/)
[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen.svg)](https://book-bite-frontend-2026.s3.us-east-1.amazonaws.com/index.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## 🚀 Live Demo

Experience the agent in production:  
🔗 **[Book-Bite Action Agent Web App](https://book-bite-frontend-2026.s3.us-east-1.amazonaws.com/index.html)**

---

## 💡 Overview

Standard chatbots often provide verbose, generic, or passive advice that increases cognitive fatigue. **Book-Bite** takes a different approach:
- **Zero Fluff:** Delivers concise, high-impact tactical advice readable in under 60 seconds.
- **Dynamic Persona Injection:** Adopts the specific vocabulary, philosophy, and tone of selected authors (e.g., James Clear, Robert Greene, Mark Manson) or a generalized best-practice advisor.
- **Frictionless Onboarding:** Pre-configured suggestion chips let users test scenarios like tech paralysis or low motivation with a single click.

---
1. **Frontend:** Glassmorphism UI hosted on **Amazon S3** static website hosting, utilizing **Marked.js** to render clean typography and structured bullet points.
2. **API Layer:** **Amazon API Gateway** (REST API) with CORS configured for cross-origin client requests.
3. **Compute:** **AWS Lambda** (Python 3.12 runtime) parsing input parameters and assembling author-specific system prompts.
4. **Intelligence:** **Amazon Bedrock** invoking Anthropic Claude 3 Haiku for sub-second, cost-effective inference.

---

## 🛠️ Tech Stack

- **Cloud Platform:** Amazon Web Services (AWS Free Tier compatible)
- **AI / LLM:** Amazon Bedrock (`us.anthropic.claude-haiku-4-5-20251001-v1:0`)
- **Backend:** Python 3.12, `boto3`
- **Frontend:** Vanilla HTML5, CSS3, JavaScript (ES6+), Marked.js

---

## 📂 Project Structure

```text
├── frontend/
│   └── index.html          # Frontend web app with suggestion chips & marked parser
├── backend/
│   └── lambda_function.py  # Lambda function handling prompt injection & Bedrock call
└── README.md               # Documentation
