# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 12:15:48 2023

@author: fhjak
"""

from del2a_lister import ny_skydekke_dict
import matplotlib.pyplot as plt

#Lager dictionary som viser antall dager med 3> skydekke per år.
skyfritt_dict = {key: 0 for key in ny_skydekke_dict.keys()}
penvaer_dict = {key: 0 for key in ny_skydekke_dict.keys()}
overskyet_dict = {key: 0 for key in ny_skydekke_dict.keys()}

#Legger til dager i penvaer_dict som har mindre enn 3 skydekke.
for i in ny_skydekke_dict:
    aaret = ny_skydekke_dict[i]
    for j in aaret:
        if isinstance(j, (int, float)) and j < 3.0:
            penvaer_dict[i] += 1
#print(penvaer_dict)

#Legger til dager i skyfritt_dict som har 0 skydekke.
for i in ny_skydekke_dict:
    aaret = ny_skydekke_dict[i]
    for j in aaret:
        if isinstance(j, (int, float)) and j == 0.0:
            skyfritt_dict[i] += 1
#print(skyfritt_dict)

#Legger til dager i overskyet_dict som har mer enn 6 skydekke.
for i in ny_skydekke_dict:
    aaret = ny_skydekke_dict[i]
    for j in aaret:
        if isinstance(j, (int, float)) and j > 6.0:
            overskyet_dict[i] += 1
#print(overskyet_dict)

#Lager plot av penvaer-dictionary
x = list(penvaer_dict.keys())
y = list(penvaer_dict.values())
plt.plot(x, y)
plt.xlabel("År")
plt.ylabel("Antall dager med penvær")
plt.title("Penværsdager per år")
plt.show()

#Lager plot av skyfritt-dictionary
x = list(skyfritt_dict.keys())
y = list(skyfritt_dict.values())
plt.plot(x, y)
plt.xlabel("År")
plt.ylabel("Antall dager med skyfritt vær")
plt.title("Skyfrie dager per år")
plt.show()

#Lager plot av overskyet-dictionary
x = list(overskyet_dict.keys())
y = list(overskyet_dict.values())
plt.plot(x, y)
plt.xlabel("År")
plt.ylabel("Antall dager med overskyet vær")
plt.title("Overskyete dager per år")
plt.show()

