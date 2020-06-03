from complementos import *
import time

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtGui import *

from multiprocessing import Pool

prevpath = "../Datos/04_words_data_s/"

#funcion que calcula la distancia de los json de palabras dada una funcion y un rango
def f(tup):
    (ini, fin, diclist, lemma_w, d1, fun_bn, it) = tup
    answer = {}
    for j in range (ini, fin):
        if j % 1000 == 0:
            #lblAlert.setText("Resultado: " + str(j) + " de " + str(len(diclist)))
            print(it, ": ",j, " out of ", fin)
        if diclist[j] != lemma_w:
            d2 = {}
            with open(prevpath + diclist[j] + ".json", "r") as dic2:
                d2 = json.load(dic2)
            d1d2l = join_dics_to_list(d1, d2)
            dist = fun_bn(d1,d2,d1d2l)
            answer[diclist[j]] = dist
    final_answer = [[k, v] for k,v in answer.items()]
    return final_answer

#Funcion que calcula la distancia de un modelo booleano uno contra todos
#Parametros: palabra a calcular,
#label de alert dado un imprevisto y
#la app para poder ofrecer una actualizacion
def get_rows_bool(word, lblAlert, app):
    p = Pool(11)
    dictionaryC = {}
    with open("../Datos/00_other/dictionaryC.json", "r") as jsfile:
        dictionaryC = json.load(jsfile)
    diclist = [key for key, value in dictionaryC.items()]
    lemma_w = str(lemmatize_this(word))
    #parameterss creation
    params = []
    ini = 0
    d1 = {}
    try:
        with open(prevpath + lemma_w + ".json", "r") as dic1:
            d1 = json.load(dic1)
    except:
        return False
    for i in range(0, 10):
        params.append((ini, ini + 7800, diclist, lemma_w, d1, calc_distance_bool, i))
        ini += 7800
    params.append((ini, len(diclist), diclist, lemma_w, d1, calc_distance_bool, 10))
    answers = p.map(f, params)
    list_words = []
    for i in answers:
        for j in i:
            list_words.append(j)
    answer = {list_words[i][0]: list_words[i][1] for i in range(len(list_words))}
    with open("../Resultados/App/Bool/distancias/" + lemma_w + ".json", "w") as outquery1:
        json.dump(answer, outquery1)
    list_words = [[k,v] for k,v in answer.items()]
    list_words.sort(key = lambda x: x[1])
    list_words.reverse()
    return list_words

#Funcion que calcula la distancia de un modelo normal uno contra todos
#Parametros: palabra a calcular,
#label de alert dado un imprevisto y
#la app para poder ofrecer una actualizacion
def get_rows_distance(word, lblAlert, app):
    p = Pool(11)
    dictionaryC = {}
    with open("../Datos/00_other/dictionaryC.json", "r") as jsfile:
        dictionaryC = json.load(jsfile)
    diclist = [key for key, value in dictionaryC.items()]
    lemma_w = str(lemmatize_this(word))
    #parameterss creation
    params = []
    ini = 0
    d1 = {}
    try:
        with open(prevpath + lemma_w + ".json", "r") as dic1:
            d1 = json.load(dic1)
    except:
        return False
    for i in range(0, 10):
        params.append((ini, ini + 7800, diclist, lemma_w, d1, calc_distance_normal, i))
        ini += 7800
    params.append((ini, len(diclist), diclist, lemma_w, d1, calc_distance_normal, 10))
    answers = p.map(f, params)
    list_words = []
    for i in answers:
        for j in i:
            list_words.append(j)
    answer = {list_words[i][0]: list_words[i][1] for i in range(len(list_words))}
    with open("../Resultados/App/Bool/distancias/" + lemma_w + ".json", "w") as outquery1:
        json.dump(answer, outquery1)
    list_words = [[k,v] for k,v in answer.items()]
    list_words.sort(key = lambda x: x[1])
    return list_words
