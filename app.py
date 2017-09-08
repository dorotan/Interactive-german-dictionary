import json

data = json.load(open("vocabulary.json"))

def dictionary(w):
    return data[w]

word = input("Wpisz słowo: ")

print(dictionary(word))