
from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv # type: ignore
from google import genai

app = Flask(__name__)

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Initialize Gemini client

client = genai.Client(api_key=api_key)



@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question", "").strip()

    if not question:
        return jsonify({"response": "Please enter a question."}), 400

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=question,
            config={
                 "system_instruction": (
        "You are a helpful AI personal assistant. "
        "Give detailed, clear, and well-explained answers. "
        "For educational questions, explain concepts step by step "
        "with examples. Avoid overly short answers unless requested."
    ),
                "temperature": 0.7,
                "max_output_tokens": 1024
            }
        )

        answer = response.text.strip()
        return jsonify({"response": answer}), 200

    except Exception as e:
        print("Ask API error:", e)
        return jsonify({
            "response": "Sorry, something went wrong. Please try again."
        }), 500


@app.route("/summarize", methods=["POST"])
def summarize():
    email_text = request.form.get("email", "").strip()

    if not email_text:
        return jsonify({"response": "Please enter an email to summarize."}), 400

    prompt = (
        "Summarize the following email in 2-3 sentences. "
        "Include the main purpose and any important action items.\n\n"
        f"Email:\n{email_text}"
    )

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt,
            config={
                "system_instruction": "Act like an expert email assistant.",
                "temperature": 0.3,
                "max_output_tokens": 512
            }
        )

        summary = response.text.strip()
        return jsonify({"response": summary}), 200

    except Exception as e:
        print("Summarize API error:", e)
        return jsonify({
            "response": "Sorry, the email could not be summarized."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
