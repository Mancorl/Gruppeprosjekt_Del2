# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 15:09:28 2023

@author: fhjak
"""

"""
Navn; Stasjonsid; Dato på formen DD.MM.ÅÅÅÅ; snødybde i centimeter; nedbør i millimeter;
middeltemperatur; gjennomsnittlig skydekke i en skala fra 0 (skyfritt) til 8 (helt
overskyet);høyeste middelvind i meter pr. sekund.
"""

import csv

csv_file = "snoedybder_vaer_en_stasjon_dogn.csv"

navn = []
stasjon = []
tid = []
snodybde = []
nedbor = []
temperatur = []
skydekke = []
vind = []

with open(csv_file, mode = "r", newline = "") as file:
    data = csv.reader(file, delimiter = ";")
    for i in data:
        navn.append(i[0])
        stasjon.append(i[1])
        tid.append(i[2])
        snodybde.append(i[3])
        nedbor.append(i[4])
        temperatur.append(i[5])
        skydekke.append(i[6])
        vind.append(i[7])


for i in range(1, len(nedbor)):
    if "," in nedbor[i]:
        nedbor[i] = nedbor[i].replace(",", ".")
    if nedbor[i] != "-" and nedbor[i] != "":
        nedbor[i] = float(nedbor[i])

