from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate_lesson_plan", methods=["POST"])
def generate_lesson_plan():
    data = request.json

    # Exemplo simples de chamada à IA
    prompt = f"""
    Crie um plano de aula com:
    Título: {data['lessonTitle']}
    Descrição: {data['lessonDescription']}
    Objetivos: {data['learningObjectives']}
    Disciplina: {data['subject']}
    Nível: {data['gradeLevel']}
    Duração: {data['duration']} minutos
    Recursos: {data['resources']}
    """

    # Chamada ao modelo (troque pela sua API correta)
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    plan = response.choices[0].message.content
    return jsonify({"lesson_plan": plan})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
