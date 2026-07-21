from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests

app = Flask(__name__)
CORS(app)

HF_TOKEN = os.environ.get("HF_TOKEN")
# استخدام نموذج Llama 3 8B Instruct عبر Hugging Face Inference API
MODEL_ID = "meta-llama/Meta-Llama-3-8B-Instruct"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "online", "message": "AIWebCraft Backend with Llama-3 is ready!"})

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json or {}
    user_prompt = data.get("prompt", "قم بإنشاء متجر إلكتروني احترافي")
    
    system_prompt = (
        "You are an expert AI system for building e-commerce websites. "
        "Generate a complete, modern HTML/CSS layout structure and copy for an online store based on the user request."
    )
    
    formatted_prompt = f"<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>\n{user_prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n"

    payload = {
        "inputs": formatted_prompt,
        "parameters": {
            "max_new_tokens": 1024,
            "temperature": 0.7,
            "return_full_text": False
        }
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        res_data = response.json()
        
        if isinstance(res_data, list) and len(res_data) > 0:
            generated_text = res_data[0].get("generated_text", "")
        elif "generated_text" in res_data:
            generated_text = res_data["generated_text"]
        else:
            generated_text = str(res_data)

        return jsonify({
            "status": "success",
            "result": generated_text
        })
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
