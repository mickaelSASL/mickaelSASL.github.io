# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:49:38 2019

@author: mickael
"""
from typing import List,  Dict
from copy import deepcopy
import csv

Attribut = str
Valeur = str
Ligne = Dict[Attribut, Valeur]
Table = List[Ligne]

def depuis_csv(nom_fichier_csv) -> list():
    """
    Crée une liste de dictionnaires, un par ligne.
    La 1ère ligne est considérée comme la ligne des noms de champs
    """
    lecteur = csv.DictReader(open(nom_fichier_csv,'r'))
    return [dict(ligne) for ligne in lecteur]

"""
exemple de critères
    "'fort' in ligne['monument_nom'] or 'Fort' in ligne['monument_nom']"
    "'5000' < ligne['Frequentation']"
    
"""
def select(nom_fichier_csv: str, critère: str) -> Table:
    table = depuis_csv(nom_fichier_csv)
    def test(ligne: Ligne) -> bool:
        return eval(critère)
    return [ligne for ligne in table if test(ligne)]


def projection(nom_fichier_csv: str, liste_clés:List[Attribut]) -> Table:
     table = depuis_csv(nom_fichier_csv)
     return [{clé:ligne[clé] for clé in ligne if clé in liste_clés} for ligne in table]


def tri(nom_fichier_csv: str, attribut: Attribut, decroit:bool =False) -> Table:
    table = depuis_csv(nom_fichier_csv)
    def critère(ligne: Ligne) -> str:
        return ligne[attribut]
    return sorted(table, key=critère, reverse=decroit)

def tri_numerique(nom_fichier_csv: str, attribut: Attribut, decroit:bool =False) -> Table:
    table = depuis_csv(nom_fichier_csv)
    def critère(ligne: Ligne) -> str:
        return int(ligne[attribut])
    return sorted(table, key=critère, reverse=decroit)

def union(nom_fichier_csv1: str, nom_fichier_csv2: str, cle1: Attribut, cle2: Attribut = None) -> Table:
    table1 = depuis_csv(nom_fichier_csv1)
    table2 = depuis_csv(nom_fichier_csv2)
    if cle2 is None: # Par défaut les clés de jointure portent le même nom
        cle2 = cle1
    new_table: Table = []  # La future table créée, vide au départ
    for ligne1 in table1: 
        for ligne2 in table2:
		    #  on ne  considère que  les lignes  où les  cellules de  l'attribut
		    # choisi sont identiques. 
            if ligne1[cle1] == ligne2[cle2]:
                new_line = deepcopy(ligne1) # on copie entièrement la ligne de table1 
                for cle in ligne2: # on copie la ligne de table2 sans répéter la
                                   # cellule de jointure
                    if cle != cle2:
                        new_line[cle] = ligne2[cle]
                new_table.append(new_line)
    return new_table


def longueur(nom_fichier_csv: str)->int:
    table = depuis_csv(nom_fichier_csv)
    return len(table)
