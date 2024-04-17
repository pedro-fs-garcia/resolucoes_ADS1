import json
perguntas = json.load(open("./PM/desafio_3/templates/questions.json", encoding="UTF-8"))

for key, value in perguntas.items():
    print(f"questão{key}")


