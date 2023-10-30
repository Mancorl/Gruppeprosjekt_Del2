# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:25:05 2023

@author: fhjak
"""

#døgn_nedbor = [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19]

def lengde(liste):
    nuller = 0
    mest_nuller = 0

    for n in range(1,len(liste)):
        if liste[n] == 0:
            for i in range(n, len(liste)):
                if liste[i] == 0:
                    nuller += 1
                else:
                    if nuller > mest_nuller:
                        mest_nuller = nuller
                    nuller = 0
                    break
    return mest_nuller
