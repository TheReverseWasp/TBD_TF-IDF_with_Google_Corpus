import json
import math

def main():
    #read all words in 06_words_fixed/stg1 and store in memory
    with open("../Datos/00_other/dictionaryC.json", "r") as wordsFile:
        wordListDic = json.load(wordsFile)
    print("Carga de diccionario de lemmas finalizada")
    #process Stage 2
    #Process TF and IDF
    wordNum = 0
    for k, v in wordListDic.items():
        wordNum += 1
    it = 0
    for key, val in wordListDic.items():
        if it % 1000 == 0:
            print("it:", it)
        it += 1
        with open("../Datos/06_words_fixed/stg1/" + key + ".json", "r") as stg1Json:
            wordDic = json.load(stg1Json)
        counter = 0
        for k, v in wordDic.items():
            counter += 1
        tempDic = {}
        tempDic["TF"] = counter
        if counter == 0:
            tempDic["IDF"] = wordNum / 0.9
        else:
            tempDic["IDF"] = wordNum / counter
        tempDic["LOG"] = math.log(tempDic["IDF"])
        with open("../Datos/06_words_fixed/stg2/" + key + ".json", "w") as outputFile:
            json.dump(tempDic, outputFile)
    print("Finalizado")

if __name__ == "__main__":
    main()
