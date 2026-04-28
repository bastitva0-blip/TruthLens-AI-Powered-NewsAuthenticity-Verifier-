🛡️ TruthLens — AI News Authenticity Verifier
TruthLens is a high-speed, forensic-grade verification tool designed to restore integrity to digital media. By leveraging the multimodal reasoning capabilities of Google Gemini 2.0 Flash, it analyzes news articles, headlines, and social media claims to detect deepfakes, misinformation patterns, and logical fallacies in seconds.
🚀 Key Features
Instant Authenticity Verdict: Categorizes content as REAL, FAKE, MISLEADING, or UNVERIFIABLE.
AI Confidence Scoring: Provides a clear percentage-based reliability indicator (0–100%) for every analysis.
Forensic Red Flags: Automatically detects emotional manipulation, statistical misrepresentation, and source credibility signals.
Claim-by-Claim Fact Check: Breaks down complex reports into individual claims with specific truth assessments (True/False/Partially True).
Bias & Sentiment Analysis: Identifies potential political or social slants and agendas hidden within the text.
Actionable Recommendations: Offers guided steps on how the user should handle or further verify the flagged information.
🛠️ Tech Stack
Frontend: Vanilla HTML5, CSS3, and JavaScript (Zero-framework, high-performance UI).
Backend: Python + Flask.
AI Engine: Google Gemini 2.0 Flash (via google-genai SDK).
Environment: Secure API management via environment variables.
📦 Setup & Installation
1. Prerequisites
Ensure you have Python 3.8+ installed.
2. Install Dependencies
pip install -r requirements.txt
3. Configure API Key
Set your Google Gemini API key as an environment variable to keep it secure:
# For Linux/Mac
export GEMINI_API_KEY="your_api_key_here"

# For Windows
set GEMINI_API_KEY="your_api_key_here"

Run the Application
python app.py
The app will be accessible at http://localhost:5000.
🗺️ System Architecture
User Input: User submits a news claim or article via the browser interface.
Flask Orchestrator: The backend validates the input length and formats a specialized "System Prompt" for the AI.
Gemini Reasoning: The AI performs multimodal analysis, cross-referencing claims against known misinformation patterns and logical structures.
Sanitization: The Python backend cleans the AI's JSON output (removing markdown backticks) for secure transmission.
Dynamic Rendering: The frontend renders the final forensic report instantly without a page refresh.
🔮 Future Roadmap
🔗 Blockchain Notarization: Generate unique, personalized Hash IDs for every analysis to create a permanent, tamper-proof record of truth on a public ledger.
🔒 Immutable Notarization: Store "Truth Scores" on a decentralized ledger (e.g., Polygon) to prevent retroactive tampering with verification results.
🖼️ Content Fingerprinting: Implement cryptographic signatures to detect if even a single pixel of media has been altered.
🌐 Browser Extensions: Real-time authenticity badges for X (Twitter), Reddit, and news sites.
📦 Decentralized Storage: Move verification logs to IPFS to ensure data remains accessible and transparent.
📝 Notes
TruthLens is a supplement to professional fact-checking, not a total replacement.
AI results are based on the model's reasoning capabilities and real-time analysis.
Developed by Astitva Bhardwaj — Solution Challenge 2026
