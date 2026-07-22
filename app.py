import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
import threading

app = Flask(__name__)
# 🌐 تفعيل CORS كاملاً لمنع أي حظر من المتصفح
CORS(app, resources={r"/*": {"origins": "*"}})

# 🤖 رابط Ollama المحلي داخل Colab
OLLAMA_URL = "http://localhost:11434/api/generate"

# 🎯 System Instruction محايد لتفادي رفض السلامة (Safety Refusal)
SYSTEM_PROMPT = """
You are an expert frontend UI designer. Your task is to generate complete HTML5 source code for a web UI demo based on the user prompt.
Requirements:
1. Always output complete, self-contained HTML5 code.
2. Include Tailwind CSS CDN and Alpine.js CDN.
3. If requested, include a toggle tab between a storefront and a mock configuration dashboard.
4. Output standard double quotes (\") for attributes.
5. Do NOT include markdown wrappers like ```html. Return ONLY raw HTML code.
"""

@app.route('/api/generate', methods=['POST'])
def generate_store():
    try:
        data = request.json or {}
        user_prompt = data.get("prompt", "Create a smartphone e-commerce UI demo")

        print(f"📥 استقبال الطلب: {user_prompt}")

        # ⚡ إرسال الطلب لـ Ollama
        payload = {
            "model": "llama3",  # 👈 حط اسم الموديل لي محمل عندك فـ Ollama (مثلاً llama3, qwen2, deepseek-r1)
            "prompt": f"{SYSTEM_PROMPT}\n\nUser Request: {user_prompt}",
            "stream": False
        }

        # الاتصال بـ Ollama Local Engine
        response = requests.post(OLLAMA_URL, json=payload, timeout=120)
        
        if response.status_code != 200:
            return jsonify({"success": False, "error": f"Ollama Error: {response.text}"}), 500

        result = response.json()
        generated_code = result.get("response", "")

        # تنقية الكود من علامات Markdown
        clean_code = generated_code.replace("```html", "").replace("```", "").strip()

        return jsonify({"success": True, "code": clean_code})

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500

def run_server():
    app.run(host='0.0.0.0', port=5001)

# تشغيل السيرفر فـ Thread خفي
threading.Thread(target=run_server, daemon=True).start()
print("🚀 السيرفر شغال ومستعد لاستقبال الطلبات على البورت 5001!")
