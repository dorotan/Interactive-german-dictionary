# -*- coding: utf-8 -*-
import json
from difflib import get_close_matches

data = json.load(open("vocabulary.json"))

def dictionary(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Czy chodziło Tobie o %s? Wpisz 't' jeśli tak lub wpisz 'n' jeśli nie: " % get_close_matches(w, data.keys())[0])
        if yn == "t":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "Słowo nie istnieje w słowniku. Spróbuj z innym słowem."
        else:
            return "Nie wiem czego szukasz. Może spóbujesz jeszcze raz?"
    else:
        return "Słowo nie istnieje w słowniku. Spróbuj z innym słowem."

if __name__ == "__main__":
    word = input("Wpisz słowo: ")

output = dictionary(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
