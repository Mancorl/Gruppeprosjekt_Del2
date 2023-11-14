"""
En måte å sjekke trender i temperatur gjennom året er å ta gjennomsnittet av temperaturen
for en tidsperiode (for eksempel ei uke eller en måned) og så sjekke om snittet endrer seg.
Ved å ta gjennomsnittet så fjerner man at temperaturen går opp og ned fra en dag til den
neste. Regn ut gjennomsnittstemperaturen for hver måned (for eksempel april 2007) og legg
disse gjennomsnittene i ei ny liste. Bruk funksjonen fra del 1 deloppgave e) for å regne ut ei
liste med differanser. Plott både lista over gjennomsnittstemperaturer og lista over
differanser med måned og år på x-aksen.
"""

from del1e_differanse import finn_differanse
from del2a_lister import temperatur
from del2a_lister import tid
import matplotlib.pyplot as plt

#Legger til temperaturverdier til en temperatur-dictionary.
#Lager også gj_temperatur_dict for å legge til gjennomsnittsverdi per måned.
maaneder = []
temperatur_dict = {}
gj_temperatur_dict = {}
for i in range(1, len(tid)):
    maaned = tid[i]
    if len(maaned) > 1 and maaned[3:10] not in temperatur_dict:
        maaneder.append(maaned[3:10])
        temperatur_dict[maaned[3:10]] = []
        gj_temperatur_dict[maaned[3:10]] = 0
    elif maaned[3:10] in temperatur_dict and temperatur[i] != "":
        temperatur_dict[maaned[3:10]].append(temperatur[i])

#Legger til verdier til gj_temperatur_dict
for i in temperatur_dict:
    if len(temperatur_dict[i]) != 0:
        gj_snitt = round(sum(temperatur_dict[i]) / len(temperatur_dict[i]))
    gj_temperatur_dict[i] = gj_snitt

#Oppretter liste med gjennomsnittsverdiene for seg selv
gj_temperatur = []
for i in gj_temperatur_dict:
    gj_temperatur.append(gj_temperatur_dict[i])

#Oppretter liste med temperaturdifferanse ved bruk av finn_differanse funksjonen
diff_temperatur = finn_differanse(gj_temperatur)

#Legger til verdi til differanse-liste, slik at den samsvarer med måneds-liste
diff_temperatur.append(0)

"""
#Differanse uten bruk av funksjon:
diff_temperatur = []
for i in gj_temperatur:
    differanse = gj_temperatur[i] - gj_temperatur[i+1]
    diff_temperatur.append(differanse)
"""

plt.plot(maaneder, gj_temperatur, label="Gjennomsnittstemperatur")
plt.ylabel("temperatur")
plt.xlabel("Dato")
plt.show()

plt.plot(maaneder, diff_temperatur, label="Gjennomsnittsdifferanse")
plt.ylabel("temperatur")
plt.xlabel("Dato")
plt.show()
