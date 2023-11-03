# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:25:46 2023

@author: fhjak
"""


#Har oppdatert funksjonen, slik at den nå sjekker om verdien i listen faktisk
#er et tall eller ikke. Dette var nødvendig for denne oppgaven, ettersom flere
#av listeverdiene er strenger ("-")
def vekst(listen):
    planten_vokser = 0
    for n in range(1, len(listen)):
        if isinstance(listen[n], (int, float)) and listen[n] > 5.0:
            planten_vokser += listen[n]-5
    return planten_vokser
        



