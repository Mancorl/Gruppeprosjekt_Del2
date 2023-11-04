# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 18:19:56 2023

@author: fhjak
"""

"""
For hvert år finn høyeste middelvind samt medianen for vindstyrke. For å finne medianen,
lag ei liste over alle verdiene for det året, sorter lista, og plukk ut det midterste elementet i
den sorterte lista. Plott dette for hvert år. Inkluder bare år hvor det er data om vind for
mesteparten av året, det må være data for minst 300 dager for at et år skal være gyldig.
"""

from del2a_lister import ny_vind_dict
import matplotlib.pyplot as plt


#Lager dictionary som viser høyest vind og median-vind per år.
hoyest_vind_dict = {key: 0 for key in ny_vind_dict.keys()}
median_vind_dict = {key: 0 for key in ny_vind_dict.keys()}

#Legger til høyeste vind-verdier til hoyest_vind_dict
for i in ny_vind_dict:
    hoyest = 0
    aaret = ny_vind_dict[i]
    for j in aaret:
        if isinstance(j, (int, float)) and j > hoyest:
            hoyest = j
    hoyest_vind_dict[i] = hoyest

#Sortere liste og velg midterte verdi
for i in ny_vind_dict:
    vind_verdier = []
    median = 0
    median = 0
    aaret = ny_vind_dict[i]
    for j in aaret:
        if isinstance(j, (int, float)):
            vind_verdier.append(j)
    vind_verdier.sort()
    median = int(len(vind_verdier) / 2)
    median_vind_dict[i] = vind_verdier[median]

#Lager plot av hoyest_vind-dictionary
x = list(hoyest_vind_dict.keys())
y = list(hoyest_vind_dict.values())
plt.plot(x, y)
plt.xlabel("År")
plt.ylabel("Høyest middelvind")
plt.title("Høyest middelvind per år")
plt.show()

#Lager plot av median_vind-dictionary
x = list(median_vind_dict.keys())
y = list(median_vind_dict.values())
plt.plot(x, y)
plt.xlabel("År")
plt.ylabel("Median vind")
plt.title("Median vind per år")
plt.show()


