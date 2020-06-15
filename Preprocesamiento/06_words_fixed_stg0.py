import json
import math

def main():
    #read all words in 04_words_data_s and store in memory
    with open("../Datos/00_other/dictionaryC.json", "r") as wordsFile:
        wordListDic = json.load(wordsFile)
    print("Carga de diccionario de lemmas finalizada")
    wordsDic = {}
    it = 0
    for key, val in wordListDic.items():
        if it % 1000 == 0:
            print("it:", it)
        it += 1
        word = key
        with open("../Datos/04_words_data_s/" + word + ".json", "r") as wordFile:
            tempDic = json.load(wordFile)
        wordsDic[word] = {}
        for k, v in tempDic.items():
            wordsDic[word][k] = v[0]
    print("Carga de jsons a cache finalizada")
    #process Stage 1
    #f = freqij / maxfreq|,i
    #return True
    it = 0
    for key, val in wordsDic.items():
        if it % 1000 == 0:
            print("it:", it)
        it += 1
        tempDic = {}
        for k, v in wordsDic.items():
            if key in v:
                tempDic[k] = v[key]
        with open("../Datos/06_words_fixed/stg0/" + key + ".json", "w") as outputFile:
            json.dump(tempDic, outputFile)
    print("Proceso Finalizado")

if __name__ == "__main__":
    main()
