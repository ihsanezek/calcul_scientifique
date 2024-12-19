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

    
    while right - left >= precision : 
        middle = (right + left) / 2 #on prend la distance de notre courbe et on la sépare en deux parties 
        
        if f(middle) == 0 : 
            print(middle)
            break 
        
        elif f(left) * f(middle) < 0 :  #on vérifie que si la  
            right = middle 
            
        elif f(right) * f(middle) < 0 : 
            left = middle
    
    return middle  
        

  
if __name__ == "__main__" :
    x = numpy.array([1, 2, 3])
    y = f(x)
    middle = solve_equation(f, left=1, right=2)
    #y = [f(1), f(2), f(3)] voila ce qui se passe en backend 
    print (middle) #valeur à laquelle h -> 0.
    print(f(middle))

