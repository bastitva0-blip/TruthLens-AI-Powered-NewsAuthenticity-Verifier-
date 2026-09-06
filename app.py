import os
import json
import re
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__, template_folder='.')

DEFAULT_GEMINI_API_KEY = "api key"
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', DEFAULT_GEMINI_API_KEY)
genai.configure(api_key=GEMINI_API_KEY)

SYSTEM_PROMPT = """You are an expert fact-checker, news authenticity analyst, and investigative journalist assistant. Your job is to analyze news articles or claims and determine their authenticity, credibility, and potential bias.
you main idea is to classify information in various categories such as
When analyzing news, you must respond with a valid JSON object (and nothing else) in the following format:
{
  "verdict": "REAL" | "FAKE" | "MISLEADING" | "UNVERIFIABLE" | "SATIRE",
  "confidence": <number between 0 and 100>,
  "severity": "LOW" | "MEDIUM" | "HIGH" | "CRITICAL",
  "summary": "<2-3 sentence summary of the news claim>",
  "analysis": "<detailed analysis explaining your verdict>",
  "red_flags": ["<flag1>", "<flag2>", ...],
  "credibility_factors": ["<factor1>", "<factor2>", ...],
  "bias_indicators": ["<bias1>", "<bias2>", ...],
  "fact_check_points": [
    {"claim": "<specific claim>", "assessment": "TRUE" | "FALSE" | "PARTIALLY TRUE" | "UNVERIFIABLE", "explanation": "<brief explanation>"}
  ],
  "emotional_manipulation_score": <number 0-10>,
  "emotional_tactics": ["<tactic1>", "<tactic2>", ...],
  "logical_fallacies": ["<fallacy1>", "<fallacy2>", ...],
  "missing_context": "<what important context is missing from this news>",
  "alternative_perspectives": ["<perspective1>", "<perspective2>", ...],
  "suggested_sources": ["<credible source to verify this>", ...],
  "timeline_consistency": "<analysis of whether dates and sequence of events make sense>",
  "statistical_analysis": "<analysis of any statistics or numbers used>",
  "quote_verification": "<assessment of any direct quotes used>",
  "virality_risk": "LOW" | "MEDIUM" | "HIGH",
  "target_audience": "<who this content appears targeted at>",
  "potential_motive": "<possible reason this was published/shared>",
  "recommendation": "<what the reader should do with this information>",
  "counter_narratives": ["<counter-claim or alternative explanation>", ...]
}

Be thorough, objective, and base your analysis on:
1. Internal consistency of the claims
2. Known facts up to your knowledge cutoff
3. Common misinformation patterns
4. Emotional manipulation tactics (fear, outrage, urgency)
5. Source credibility signals
6. Logical fallacies
7. Statistical misrepresentation
8. Missing context or selective framing
9. Historical patterns of similar claims
10. Cross-referencing with established facts

If you cannot verify something, say so clearly. Always be balanced and non-partisan."""

COMPARE_PROMPT = """You are an expert media analyst. Compare these two versions of the same news story and identify differences in framing, bias, and completeness.

Respond with a valid JSON object only:
{
  "story1_bias": "LEFT" | "RIGHT" | "CENTER" | "UNKNOWN",
  "story2_bias": "LEFT" | "RIGHT" | "CENTER" | "UNKNOWN",
  "key_differences": ["<difference1>", "<difference2>", ...],
  "omissions_story1": ["<what story 1 omits>", ...],
  "omissions_story2": ["<what story 2 omits>", ...],
  "common_facts": ["<fact both agree on>", ...],
  "contradictions": ["<direct contradiction>", ...],
  "more_complete": "STORY1" | "STORY2" | "EQUAL",
  "overall_analysis": "<comprehensive comparison analysis>",
  "recommendation": "<which provides more balanced coverage and why>"
}"""

HEADLINE_PROMPT = """You are a clickbait and sensationalism detector. Analyze this headline and article body.

Respond with a valid JSON object only:
{
  "clickbait_score": <0-10>,
  "sensationalism_score": <0-10>,
  "headline_accuracy": <0-100>,
  "misleading_elements": ["<element1>", ...],
  "emotional_words": ["<word1>", ...],
  "headline_vs_content": "<how the headline differs from the actual content>",
  "improved_headline": "<a more accurate, less sensational headline>",
  "verdict": "ACCURATE" | "MISLEADING" | "CLICKBAIT" | "OUTRIGHT_FALSE"
}"""

DEEPFAKE_TEXT_PROMPT = """You are an AI-generated text detector. Analyze if this content may have been AI-generated or heavily manipulated.

Respond with a valid JSON object only:
{
  "ai_generated_probability": <0-100>,
  "indicators": ["<indicator1>", ...],
  "writing_style_analysis": "<analysis of writing patterns>",
  "inconsistencies": ["<inconsistency1>", ...],
  "verdict": "LIKELY_HUMAN" | "POSSIBLY_AI" | "LIKELY_AI" | "UNCERTAIN"
}"""

SOCIAL_MEDIA_PROMPT = """You are a social media misinformation expert. Analyze this viral social media post or chain message.

Respond with a valid JSON object only:
{
  "verdict": "REAL" | "FAKE" | "MISLEADING" | "SATIRE" | "UNVERIFIABLE",
  "confidence": <0-100>,
  "viral_misinformation_patterns": ["<pattern1>", ...],
  "chain_message_indicators": ["<indicator1>", ...],
  "urgency_tactics": ["<tactic1>", ...],
  "previous_versions": "<if this resembles known hoaxes or chain messages>",
  "fact_check_points": [
    {"claim": "<claim>", "assessment": "TRUE" | "FALSE" | "PARTIALLY TRUE" | "UNVERIFIABLE", "explanation": "<explanation>"}
  ],
  "red_flags": ["<flag1>", ...],
  "recommendation": "<what to do>",
  "share_advice": "SHARE" | "DO_NOT_SHARE" | "SHARE_WITH_CAUTION"
}"""


def call_gemini(prompt, system=""):
    full_prompt = f"{system}\n\n{prompt}" if system else prompt
    model = genai.GenerativeModel(model_name="models/gemini-2.5-flash")
    response = model.generate_content(full_prompt)
    raw = (response.text or "").strip()
    if not raw:
        raise ValueError("No text returned from Gemini.")
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)
    return json.loads(raw.strip())


def analyze_news(news_text):
    prompt = f"Analyze this news/claim:\n\n{news_text}"
    return call_gemini(prompt, SYSTEM_PROMPT)


def compare_stories(story1, story2):
    prompt = f"Story 1:\n{story1}\n\nStory 2:\n{story2}"
    return call_gemini(prompt, COMPARE_PROMPT)


def analyze_headline(headline, body=""):
    prompt = f"Headline: {headline}\n\nArticle body:\n{body}" if body else f"Headline: {headline}"
    return call_gemini(prompt, HEADLINE_PROMPT)


def detect_ai_text(text):
    prompt = f"Analyze this content:\n\n{text}"
    return call_gemini(prompt, DEEPFAKE_TEXT_PROMPT)


def analyze_social_media(post):
    prompt = f"Analyze this social media post/chain message:\n\n{post}"
    return call_gemini(prompt, SOCIAL_MEDIA_PROMPT)


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


@app.route("/compare", methods=["POST"])
def compare():
    data = request.get_json()
    story1 = data.get("story1", "").strip()
    story2 = data.get("story2", "").strip()
    if not story1 or not story2:
        return jsonify({"error": "Two stories are required for comparison"}), 400
    try:
        result = compare_stories(story1, story2)
        return jsonify({"success": True, "result": result})
    except json.JSONDecodeError as e:
        return jsonify({"error": f"Failed to parse AI response: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/headline", methods=["POST"])
def headline():
    data = request.get_json()
    headline_text = data.get("headline", "").strip()
    body_text = data.get("body", "").strip()
    if not headline_text:
        return jsonify({"error": "No headline provided"}), 400
    try:
        result = analyze_headline(headline_text, body_text)
        return jsonify({"success": True, "result": result})
    except json.JSONDecodeError as e:
        return jsonify({"error": f"Failed to parse AI response: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/detect-ai", methods=["POST"])
def detect_ai():
    data = request.get_json()
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"error": "No text provided"}), 400
    if len(text) < 50:
        return jsonify({"error": "Please provide more text for accurate AI detection"}), 400
    try:
        result = detect_ai_text(text)
        return jsonify({"success": True, "result": result})
    except json.JSONDecodeError as e:
        return jsonify({"error": f"Failed to parse AI response: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/social-media", methods=["POST"])
def social_media():
    data = request.get_json()
    post = data.get("post", "").strip()
    if not post:
        return jsonify({"error": "No social media post provided"}), 400
    try:
        result = analyze_social_media(post)
        return jsonify({"success": True, "result": result})
    except json.JSONDecodeError as e:
        return jsonify({"error": f"Failed to parse AI response: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
