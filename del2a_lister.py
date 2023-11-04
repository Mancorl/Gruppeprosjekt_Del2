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

#Del2e: Tilpasser listen "temperatur"
for i in range(1, len(temperatur)):
    if "," in temperatur[i]:
        temperatur[i] = nedbor[i].replace(",", ".")
    if temperatur[i] != "-" and temperatur[i] != "":
        temperatur[i] = float(temperatur[i])

#Del2f: Tilpasser listen "nedbor"
for i in range(1, len(nedbor)):
    if "," in nedbor[i]:
        nedbor[i] = nedbor[i].replace(",", ".")
    if nedbor[i] != "-" and nedbor[i] != "":
        nedbor[i] = float(nedbor[i])


#Del2e: Legger til temperaturverdier til en temperatur-dictionary.
temperatur_dict = {}
for i in range(1, len(tid)):
    aar = tid[i]
    if len(aar) > 1 and aar[6:10] not in temperatur_dict:
        temperatur_dict[aar[6:10]] = []
    elif aar[6:10] in temperatur_dict:
        temperatur_dict[aar[6:10]].append(temperatur[i])

#Del2e: Legger til år med over 300 målinger i ny dictionary.
ny_temperatur_dict = {}
for i in temperatur_dict:
    length = len(temperatur_dict[i])
    if length > 300:
        ny_temperatur_dict[i] = temperatur_dict[i]


#Del2f: Legger til nedbørsverdier til en nedbørs-dictionary.
nedbor_dict = {}
for i in range(1, len(tid)):
    aar = tid[i]
    if len(aar) > 1 and aar[6:10] not in nedbor_dict:
        nedbor_dict[aar[6:10]] = []
    elif aar[6:10] in nedbor_dict:
        nedbor_dict[aar[6:10]].append(nedbor[i])

#Del2f: Legger til år med over 300 målinger i ny dictionary.
ny_nedbor_dict = {}
for i in nedbor_dict:
    length = len(nedbor_dict[i])
    if length > 300:
        ny_nedbor_dict[i] = nedbor_dict[i]
