
from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    tool = data['tool']
    area = data['area']
    tone = data['tone']
    objective = data['objective']

    if tool == "generate":
        prompt = f"Crie um prompt poderoso para o tópico: '{area}'\nTom: {tone}\nObjetivo: {objective}\nUse clareza, estrutura e estratégia.\n(Also provide English version.)"
    elif tool == "refine":
        prompt = "Refine o seguinte prompt para clareza, especificidade e estrutura: [INSERIR PROMPT AQUI] (Refine this prompt in English and Portuguese)"
    elif tool == "translate":
        prompt = "Traduza o seguinte prompt entre Português e Inglês: [INSERIR PROMPT AQUI]"
    else:
        prompt = "Converta o seguinte prompt em um formato de post (ex: carrossel no Instagram, roteiro de vídeo): [INSERIR PROMPT AQUI]"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é o PromptMaster 360. Use o MÉTODO CERTO. Seja bilíngue, estratégico e claro."},
            {"role": "user", "content": prompt}
        ]
    )
    return jsonify({'response': response['choices'][0]['message']['content']})

if __name__ == "__main__":
    app.run(debug=True)
