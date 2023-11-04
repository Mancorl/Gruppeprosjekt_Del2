# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:25:46 2023

@author: fhjak
"""

from del1f_lengde import lengde
from del2a_lister import ny_nedbor_dict
import matplotlib.pyplot as plt

#(Lengste sammenhengende tørke-sesong er 23.04.1990-20.05.1990, og varer 28 dager)
#Lager nytt dictionary med lengde uten nedbør for hvert år.
lengde_nedbor = {}
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
