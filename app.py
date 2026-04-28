import os
import json
import re

from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__, template_folder='.')

DEFAULT_GEMINI_API_KEY = "api key"
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', DEFAULT_GEMINI_API_KEY)

genai.configure(api_key=GEMINI_API_KEY)

SYSTEM_PROMPT = """You are an expert fact-checker and news authenticity analyst. Your job is to analyze news articles or claims and determine their authenticity, credibility, and potential bias.

When analyzing news, you must respond with a valid JSON object (and nothing else) in the following format:
{
  "verdict": "REAL" | "FAKE" | "MISLEADING" | "UNVERIFIABLE",
  "confidence": <number between 0 and 100>,
  "summary": "<2-3 sentence summary of the news claim>",
  "analysis": "<detailed analysis explaining your verdict>",
  "red_flags": ["<flag1>", "<flag2>", ...],
  "credibility_factors": ["<factor1>", "<factor2>", ...],
  "bias_indicators": ["<bias1>", "<bias2>", ...],
  "fact_check_points": [
    {"claim": "<specific claim>", "assessment": "TRUE" | "FALSE" | "PARTIALLY TRUE" | "UNVERIFIABLE", "explanation": "<brief explanation>"}
  ],
  "recommendation": "<what the reader should do with this information>"
}

Be thorough, objective, and base your analysis on:
1. Internal consistency of the claims
2. Known facts up to your knowledge cutoff
3. Common misinformation patterns
4. Emotional manipulation tactics
5. Source credibility signals
6. Logical fallacies
7. Statistical misrepresentation

If you cannot verify something, say so clearly. Always be balanced and non-partisan."""


def analyze_news(news_text):
    prompt = f"{SYSTEM_PROMPT}\n\nAnalyze this news/claim:\n\n{news_text}"
    model = genai.GenerativeModel(model_name="models/gemini-2.5-flash")
    response = model.generate_content(prompt)
    raw = (response.text or "").strip()
    if not raw:
        raise ValueError("No text returned from Gemini.")
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)
    result = json.loads(raw.strip())
    return result


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    news_text = data.get("news", "").strip()

    if not news_text:
        return jsonify({"error": "No news text provided"}), 400
    if len(news_text) < 20:
        return jsonify({"error": "Please provide more detailed news content"}), 400

    try:
        result = analyze_news(news_text)
        return jsonify({"success": True, "result": result})
    except json.JSONDecodeError as e:
        return jsonify({"error": f"Failed to parse AI response: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
