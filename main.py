# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 12:03:18 2024

@author: 33785
"""

"""
Dans ce code on suppose qu'on à une courbe qui intialement est posistive puis elle devient négative.
on essaye de trouevr le "middle" qui nous permet de savoir à quel moment notre fonction tend le plus vers 0 
Par conséquent l moment ou notre courbe passe par l'axe des abscisses

on prend notre courbe et on sépare notre distance en 2 parties. 
Puis on lance une boucle pour voir ou se trouve la transition du positif au négatif dans chacune des parties 
"""
import numpy


def f(x) : 
    return x**2 - 8 * numpy.log(x) #affiche une liste 

def solve_equation (f, left, right, precision = 10**(-3)) : 

    while right - left >= precision : #tant qu'on atteint pas notre seuil de précision 
        middle = (right + left) / 2 #on prend la distance de notre courbe et on la sépare en deux parties 
        
        if f(middle) == 0 : 
            print(middle)
            break 
        
        elif f(left) * f(middle) < 0 :
            right = middle 
            
        elif f(right) * f(middle) < 0 : 
            left = middle
    
    return middle 

    
import matplotlib.pyplot as plt 
from config_file import *  #récuperation des données présents dans ma feuille config_file

def plot_function (f, start, end, step=0.01) : #fonction pour créer un graphique avec une courbe 
    x = numpy.arange(start, end, step)
    y = f(x)
    
    plt.figure(figsize=(length, hight))#definit la taille du graph en utilisant les variables présent dans ma feuille config_file
    plt.plot(x, y, ":", color = "green") #definit les valeurs en abscisses et en ordinnées, les : permettent d'afficher la courbe sous forme de pointillés
    plt.show()
    



if __name__ == "__main__" : 
    
    plot_function(f, start=0.01, end=5, step = 0.01)
    
    """
    x = numpy.array([1, 2, 3])
    y = f(x)
    middle = solve_equation(f, left=1, right=2)
    #y = [f(1), f(2), f(3)] voila ce qui se passe en backend 
    print (middle) #valeur à laquelle h -> 0.
    print(f(middle))
    """
    

