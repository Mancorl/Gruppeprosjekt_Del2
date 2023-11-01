# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:25:46 2023

@author: fhjak
"""

from del1f_lengde import lengde
from del2a_lister import nedbor
from del2a_lister import tid
import matplotlib.pyplot as plt

#Legger til nedbørsverdier til en nedbørs-dictionary.
nedbor_dict = {}
for i in range(1, len(tid)):
    aar = tid[i]
    if len(aar) > 1 and aar[6:10] not in nedbor_dict:
        nedbor_dict[aar[6:10]] = []
    elif aar[6:10] in nedbor_dict:
        nedbor_dict[aar[6:10]].append(nedbor[i])

#Legger til år med over 300 målinger i ny dictionary.
ny_nedbor_dict = {}
for i in nedbor_dict:
    length = len(nedbor_dict[i])
    if length > 300:
        ny_nedbor_dict[i] = nedbor_dict[i]

#(Lengste sammenhengende tørke-sesong er 23.04.1990-20.05.1990, og varer 28 dager)
#Lager nytt dictionary med lengde uten nedbør for hvert år.
lengde_nedbor = {}
print("Dager uten nedbør per år:")
for i in ny_nedbor_dict:
    lengde_nedbor[i] = lengde(ny_nedbor_dict[i])

#Lager plot av lengde_nedbor-dictionary
x = list(lengde_nedbor.keys())
y = list(lengde_nedbor.values())
plt.plot(x, y)
plt.xlabel("År")
plt.ylabel("Sammenhengende antall dager uten nedbør")
plt.title("Lengste antall dager uten nedbør")
plt.show()
