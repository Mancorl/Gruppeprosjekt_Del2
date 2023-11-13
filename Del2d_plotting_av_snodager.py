#Trenden i snodager
import csv
from datetime import datetime
import numpy as np
import del1d_returner_liste_av_storre_tall
import matplotlib.pyplot as plt
csv_file = "snoedybder_vaer_en_stasjon_dogn.csv"

navn = []
stasjon = []
tid = []
snodybde = []
nedbor = []
temperatur = []
skydekke = []
vind = []
maanedslister = []
maanedsliste = []
snadagtemp = []
snodager = []
aarsliste = []
aar = []
Snoliste = []

with open(csv_file, mode = "r", newline = "") as file:
    next(file)
    data = csv.reader(file, delimiter = ";")
    for i in data:
        if i[2] == "":
            continue
        tid.append(i[2])
        snodybde.append(i[3])

    snodager = [x for _, x in sorted(zip(tid, snodybde), key = lambda date: datetime.strptime(date[0], "%d.%m.%Y"))]
    maanedslister = sorted(tid, key=lambda date: datetime.strptime(date, "%d.%m.%Y"))
    #print (maanedslister)
    #print(snodager)

    for maaned in maanedslister:
        maanedsliste.append(maaned.split(".")[1])
        aarsliste.append(maaned.split(".")[2])
    sesongdybde = [[]]
    snosesong = [[]]
    acc = 0
    nysesong = False

    for i in range(len(maanedsliste)):
        #print(i)
        if int(maanedsliste[i]) > 9 or int(maanedsliste[i]) < 6:
            if snodager[i] == "-":
                continue
            snosesong[acc].append(maanedsliste[i])
            sesongdybde[acc].append(snodager[i])

            nysesong = False
        elif nysesong == False:
            #print(maanedsliste[i])
            if len(sesongdybde[acc]) > 200:
                snosesong.append([])
                sesongdybde.append([])
                aar.append(int(aarsliste[i]))
                nysesong = True
                acc += 1
            else:
                print(aarsliste[i])
            """else:
                print(aarsliste[i])
                sesongdybde.pop(acc)
                snosesong.pop(acc)
                snosesong.append([])
                sesongdybde.append([])
                
                nysesong = True"""

                
    #snosesong.pop(0)
    snosesong.pop()
    #sesongdybde.pop(0)
    sesongdybde.pop()
    #print(len(snosesong))
    #print(len(sesongdybde))
    #print(sesongdybde)
    for i in range(len(sesongdybde)):
        Snoliste.append(int(len(del1d_returner_liste_av_storre_tall.differanse(sesongdybde[i], 20))))
    print(aar)
    print(Snoliste)
    plt.plot(aar, Snoliste)
    plt.show()
    