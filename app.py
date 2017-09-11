# -*- coding: utf-8 -*-
import json
from difflib import get_close_matches

data = json.load(open("vocabulary.json"))

def dictionary(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        return "Czy chodziło Tobie o %s?" % get_close_matches(w, data.keys())[0]
    else:
        return "Słowo nie istnieje w słowniku. Spróbuj z innym słowem."

word = input("Wpisz słowo: ")

print(dictionary(word))