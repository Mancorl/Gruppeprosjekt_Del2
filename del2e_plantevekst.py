# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 14:02:41 2023

@author: fhjak
"""

"""
Beregn veksten for den tenkte planten for hvert år i datasettet med bruk av funksjonen fra
del 1 oppgave h). Plott dette for hvert år i datasettet. Inkluder bare år hvor det er
temperaturdata for mesteparten av året, det må være data for minst 300 dager for at et år
skal være gyldig. Dette vil kreve at dere lager separate lister for hvert år som kan brukes som
parameter til funksjonen fra del 1 oppgave h)
"""

from del1h_over_fem_v2 import vekst
from del2a_lister import temperatur
from del2a_lister import tid
import matplotlib.pyplot as plt

#Legger til temperaturverdier til en temperatur-dictionary.
temperatur_dict = {}
for i in range(1, len(tid)):
    aar = tid[i]
    if len(aar) > 1 and aar[6:10] not in temperatur_dict:
        temperatur_dict[aar[6:10]] = []
    elif aar[6:10] in temperatur_dict:
        temperatur_dict[aar[6:10]].append(temperatur[i])

#Legger til år med over 300 målinger i ny dictionary.
ny_temperatur_dict = {}
for i in temperatur_dict:
    length = len(temperatur_dict[i])
    if length > 300:
        ny_temperatur_dict[i] = temperatur_dict[i]

#Lager dictionary som viser verdien for vekst per år.
vekst_plante = {key: 0 for key in ny_temperatur_dict.keys()}

#Her kaller vi del1h-scriptets "vekst"-funksjon
#Måtte gjøre enkel modifisering av del1h-scriptet for at scriptet skulle sjekke
#for ikke-float verdier.
listen = []
for i in ny_temperatur_dict:
    listen = ny_temperatur_dict[i]
    vekst_plante[i] = vekst(listen)

#For å runde ned verdiene til en digit
for i in vekst_plante:
    vekst_plante[i] = round(vekst_plante[i], 1)

#print(vekst_plante)

#Lager plot av vekst_plante-dictionary
x = list(vekst_plante.keys())
y = list(vekst_plante.values())
plt.plot(x, y)
plt.xlabel("År")
plt.ylabel("Beregnet vekst")
plt.title("Vekst for den tenkte planten")
plt.show()


