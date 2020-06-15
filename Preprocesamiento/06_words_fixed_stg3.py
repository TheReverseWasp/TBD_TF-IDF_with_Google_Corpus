import json
import math

def main():
    #read all words in 04_words_data_s and store in memory
    with open("../Datos/00_other/dictionaryC.json", "r") as wordsFile:
        wordListDic = json.load(wordsFile)
    print("Carga de diccionario de lemmas finalizada")
    #process Stage 3
    #New vector jsons
    it = 0
    for key, val in wordListDic.items():
        if it % 1000 == 0:
            print("it:", it)
        it += 1
        with open("../Datos/06_words_fixed/stg1/" + key + ".json", "r") as wordJson:
            wordDic = json.load(wordJson)
        with open("../Datos/06_words_fixed/stg2/" + key + ".json", "r") as wordStatsJson:
            wordStatsDic = json.load(wordStatsJson)
        wordDic = {x: wordDic[x] * wordStatsDic["LOG"] for x in wordDic}
        with open("../Datos/06_words_fixed/stg3/" + key + ".json", "w") as answerJson:
            json.dump(wordDic, answerJson)
    print("Finalizado")

if __name__ == "__main__":
    main()
