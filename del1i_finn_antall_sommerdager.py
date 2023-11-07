#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:20:29 2023

@author: audun
"""
import lister_for_del_1
import del1d_returner_liste_av_storre_tall

temperaturer = lister_for_del_1.temperaturer
    
def Sommerdager():
    sommerdag = d_returner_liste_av_storre_tall.differanse(temperaturer, 20)
    hoysommerdag = d_returner_liste_av_storre_tall.differanse(temperaturer, 25)
    tropedag = d_returner_liste_av_storre_tall.differanse(temperaturer, 30)
   
    print("Det er:", len(sommerdag),"sommerdag(er)," 
          ,len(hoysommerdag), "Hoysommerdag(er) og", len(tropedag),
          "tropedag(er) i det gitte tidsintervallet")
    

