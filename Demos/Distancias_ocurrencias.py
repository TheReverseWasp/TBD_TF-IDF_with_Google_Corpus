import json
import re
import spacy
import enchant
import copy as cp

sp = spacy.load('en_core_web_sm')

def lemmatize_this(str_word):
    return sp(str_word)[0]

def main():
    while True:
        print("Ingrese la Palabra: ")
        word = input()
        word = str(lemmatize_this(word))
        try:
            with open("../Datos/06_words_fixed/stg0/" + word + ".json", "r") as answerJson:
                wordDic = json.load(answerJson)
            elems = [[k, v] for k, v in wordDic.items()]
            elems.sort(key = lambda x: x[1])
            rank = len(elems)
            for i in elems:
                print(rank, i)
                rank -=1
        except:
            print("Palabra no encontrada")

if __name__ == "__main__":
    main()
