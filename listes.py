#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lo
#
# Created:     16/01/2020
# Copyright:   (c) Lo 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# pour le commentaire et 3*" pour les choses à faire
# importer pandas,random et numpy (car c'est un tableau numpy)
import pandas as pd
from random import randint
import numpy as np

def informations () :
    # permet de charger la liste chien dans un tableau colonne_1 : indice, colonn_2 : ligne de donnée du csv (nom;image;wiki)
    """il faut trouver comment lier le bouton du thème choisi à "chien.csv" pris pour l'exemple et le test)"""
    data = pd.read_csv('chien.csv',header=None)
    print(data)

    # stock au hasard l'indice d'une ligne
    a=np.random.randint(0,data.shape[0]-1)

    # stock les données associés à l'indice (nom;image;wiki)
    donnees=data.iloc[a,0]
    print(donnees)

    # stock dans la liste les informations ("nom","image","wiki")
    infos=donnees.split(";")
    print (infos)

    # stock chaque info dans une variable
    mot=infos[0]
    adresse_image =infos[1]
    """info à passer à ceux qui vont intégrer l'image en page 4"""
    adresse_wiki=infos[2]
    """info à passer à ceux qui vont intégrer l'adresse wiki en page 4"""
    print("mot :", mot, "\nimage :",adresse_image,"\nwiki :",adresse_wiki)

    return()
informations()
