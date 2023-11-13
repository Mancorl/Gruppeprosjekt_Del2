# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 14:44:22 2023

@author: fhjak
"""

import math
import statistics
import random

#Funksjonen trend bruker to lister som x- og y-verdi
def trend(x,y):
    a1 = 0
    a2 = 0
    a = 0
    b = 0

#Regner ut a, hvis a1 er overdelen og a2 er underdelen av brøkstreken
    for n in range(1,len(x)):
        a1 += (x[n-1] - statistics.mean(x)) * (y[n-1] - statistics.mean(y))
        a2 += (x[n-1] - statistics.mean(x))**2
    a = a1 / a2
#Kan også printe a-verdien ved behov
    #print(f"a:", "%.2f" % a)

#Regner ut b
    b = statistics.mean(y) - a * statistics.mean(x)
#Kan også printe b-verdien ved behov
    #print(f"b:", "%.2f" % b)

#Tolker trenden som stigende eller synkende, avhengig av a
    if a > 0:
        print("Trenden er stigende.")
    elif a < 0:
        print("Trenden er synkende.")
    else:
        print("Det er ingen trend.")

