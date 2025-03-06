from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key="AIzaSyAksCU3soBMfqJ4CYcpSrtSXG6svQEm9do")
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")

    if not user_message:
        return jsonify({"reply": "I didn't understand that. Can you rephrase?"})

    print(f"User: {user_message}")  # Debugging

    try:
        response = model.generate_content(user_message)
        ai_reply = response.text if response else "Sorry, I couldn't fetch a response."
        print(f"AI: {ai_reply}")  # Debugging
        return jsonify({"reply": ai_reply})

    except Exception as e:
        print("Error:", str(e))  # Debugging
        return jsonify({"reply": "Error: Unable to connect to Gemini API"})

if __name__ == "__main__":
    app.run(debug=True)
