import json
directors = json.load(open("./PM/desafio_3/templates/directors_films.json"))
key_words_directors, key_words_films = [], []
for d in directors:
    for n in d.split("_"):
        key_words_directors.append(n)
        print(key_words_directors)
key_words_films += [" ".split(f) for d in directors for f in d]


print("david" in key_words_directors)