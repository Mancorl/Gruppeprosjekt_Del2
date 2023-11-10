import del2a_lister as lister
import del1e_differanse as diff
from matplotlib import pyplot as plt

lister.tid.pop(0)
lister.temperatur.pop(0)
lister.temperatur.pop(-1)
lister.tid.pop(-1)
summen = 0
dager = 0
dag, maned, aar = lister.tid[0].split(".")
gjennomsnitt = []
dato = []

for x in range(len(lister.tid)):
    dag, nymaned, nyaar = lister.tid[x].split(".")
    if nymaned == maned and nyaar == aar:
        if not lister.temperatur[x] == "-":
            summen += float(lister.temperatur[x])
            dager += 1
    else:
        gjsnitt = summen/dager
        gjennomsnitt.append(gjsnitt)
        summen = 0
        if not lister.temperatur[x] == "-":
            summen += float(lister.temperatur[x])
            dager = 1
        dato.append(maned + "." + aar)
        maned = nymaned
        aar = nyaar
differanse = diff.finn_differanse(gjennomsnitt)
plt.plot(dato, gjennomsnitt, label="Gjennomsnittstemperatur")
#plt.plot(dato, differanse, label="differanse") fungerer ikke
plt.ylabel("temperatur")
plt.xlabel("Dato")
plt.show()