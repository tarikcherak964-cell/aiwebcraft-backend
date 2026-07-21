from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # لتسمح بالاتصال من لوحة التحكم وباقي المواقع

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "online", "message": "AIWebCraft Backend is running 24/7!"})

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get("prompt", "")
    
    # هنا يتم الربط مع الـ AI لمعالجة الطلب
    return jsonify({
        "status": "success",
        "result": f"Generated store components for prompt: {prompt}"
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
