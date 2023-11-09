#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:08:35 2023

@author: audun
"""

def differanse(listen, tall):
    nyliste = []
    for i in range(0, len(listen)):
        x = int(listen[i]) - tall
        if x >= 0:
            nyliste.append(x)
    return nyliste
