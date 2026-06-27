# 🛡️ TruthLens — AI-Powered News Authenticity & Misinformation Detection Platform

> **"Verify before you amplify."**

TruthLens is an AI-powered digital forensics platform built to combat misinformation, fake news, and manipulated media in real time. Leveraging the multimodal reasoning capabilities of **Google Gemini 2.0 Flash**, it performs deep semantic analysis of news articles, headlines, social media posts, and public claims to determine their credibility within seconds.

Unlike traditional fact-checking tools that simply classify content, TruthLens produces a comprehensive forensic report—including confidence scores, logical fallacies, misinformation indicators, source credibility analysis, sentiment detection, and actionable recommendations—helping users make informed decisions before sharing information.

Developed as part of **Google Solution Challenge 2026**, TruthLens aims to make trustworthy information accessible to everyone.

---

# ✨ Core Features

### 🔍 AI Authenticity Verification

Instantly classifies submitted content into one of four categories:

* ✅ REAL
* ❌ FAKE
* ⚠️ MISLEADING
* ❓ UNVERIFIABLE

---

### 📊 AI Confidence Score

Each verification includes a confidence score (**0–100%**) indicating the AI's certainty based on contextual reasoning and evidence analysis.

Example:

```
Verdict: MISLEADING
Confidence: 92%
```

---

### 🧠 Claim-by-Claim Fact Verification

Rather than evaluating an article as a whole, TruthLens decomposes it into individual factual claims and verifies each independently.

Example Output:

| Claim                   | Status            |
| ----------------------- | ----------------- |
| Inflation reached 3%    | ✅ True            |
| GDP doubled in one year | ❌ False           |
| WHO issued a warning    | ⚠️ Partially True |

---

### 🚩 Forensic Red Flag Detection

Automatically identifies common misinformation techniques such as:

* Emotional manipulation
* Clickbait headlines
* Cherry-picked statistics
* Missing context
* Unsupported claims
* Conspiracy framing
* False authority references
* AI-generated misinformation patterns

---

### ⚖️ Bias & Sentiment Analysis

TruthLens evaluates whether content exhibits:

* Political bias
* Ideological framing
* Emotional persuasion
* Polarizing language
* Neutral journalistic tone

This helps users distinguish objective reporting from opinion-driven narratives.

---

### 📚 Source Reliability Assessment

Analyzes references and citation quality by examining:

* Source credibility
* Citation completeness
* Evidence quality
* Context preservation

---

### 💡 Actionable Recommendations

Instead of merely flagging questionable content, TruthLens provides practical guidance, including:

* Verify with trusted sources
* Look for primary evidence
* Compare multiple publications
* Avoid sharing until confirmed
* Read beyond the headline

---

# ⚡ Why TruthLens?

Millions of misleading articles circulate online every day. Manual verification is slow and often inaccessible.

TruthLens delivers:

* ⚡ Near real-time analysis
* 🧠 AI-powered reasoning
* 📈 Transparent confidence scoring
* 🔍 Explainable verification reports
* 🌍 User-friendly interface
* 🔒 Privacy-first architecture

---

# 🛠️ Technology Stack

## Frontend

* HTML5
* CSS3
* Vanilla JavaScript
* Responsive UI
* Fetch API

---

## Backend

* Python 3
* Flask
* RESTful API Architecture

---

## AI Engine

* Google Gemini 2.0 Flash
* Google Generative AI SDK
* Prompt Engineering
* Structured JSON Responses

---

## Security

* Environment Variables (.env)
* Secure API Key Management
* JSON Response Sanitization
* Markdown Injection Protection

---

# 🏗️ System Architecture

```
                User
                  │
                  ▼
        Browser Interface
                  │
                  ▼
           Flask Backend
                  │
     Input Validation & Prompt Engineering
                  │
                  ▼
      Google Gemini 2.0 Flash
                  │
      AI Reasoning & Verification
                  │
                  ▼
     JSON Sanitization & Processing
                  │
                  ▼
      Interactive Verification Report
```

---

# 📦 Installation

## Prerequisites

* Python 3.8+
* Google Gemini API Key

---

## Clone Repository

```bash
git clone https://github.com/yourusername/truthlens.git
cd truthlens
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create an environment variable:

### Linux / macOS

```bash
export GEMINI_API_KEY="your_api_key"
```

### Windows

```cmd
set GEMINI_API_KEY=your_api_key
```

---

## Run

```bash
python app.py
```

Visit:

```
http://localhost:5000
```

---

# 🔄 Workflow

```
User submits article
        │
        ▼
Input Validation
        │
        ▼
Prompt Engineering
        │
        ▼
Gemini Analysis
        │
        ▼
JSON Sanitization
        │
        ▼
Forensic Report Generation
        │
        ▼
Interactive Dashboard
```

---

# 📈 Future Roadmap

## 🔗 Blockchain Verification

Generate a unique cryptographic hash for every verification, creating a tamper-proof digital fingerprint.

---

## ⛓ Immutable Truth Ledger

Store verification results on decentralized blockchain networks such as **Polygon**, ensuring analyses remain transparent and cannot be altered retroactively.

---

## 🖼 Media Fingerprinting

Detect image or video manipulation through cryptographic fingerprinting, identifying even single-pixel modifications.

---

## 🌐 Browser Extensions

Real-time misinformation alerts and authenticity badges for:

* X (Twitter)
* Reddit
* Facebook
* LinkedIn
* YouTube
* News Websites

---

## 📦 Decentralized Storage

Archive verification reports on **IPFS** to guarantee long-term accessibility and transparency.

---

## 🤖 AI Assistant

Enable conversational verification where users can ask follow-up questions about any report and receive evidence-backed explanations.

---

## 🌍 Multilingual Verification

Support verification in multiple languages, making TruthLens accessible to a global audience.

---

# 🎯 Potential Use Cases

* Journalists
* Fact-checking organizations
* Students & Researchers
* News Consumers
* Government Agencies
* Educational Institutions
* Social Media Platforms
* NGOs combating misinformation

---

# ⚠️ Disclaimer

TruthLens is designed to assist—not replace—professional journalists, researchers, and certified fact-checking organizations.

AI-generated analyses are based on probabilistic reasoning and available contextual knowledge. Users should always consult trusted primary sources before making critical decisions.

---

# 👨‍💻 Developer

**Astitva Bhardwaj**

Google Solution Challenge 2026

Building trustworthy AI systems for a more informed digital world.

---

## ⭐ Support the Project

If you found TruthLens useful, consider giving the repository a ⭐ on GitHub and contributing to the fight against misinformation.
