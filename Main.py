# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

from Configuration import Configuration
from Section import Section
from Wall import Wall
from Door import Door
from Window import Window
from House import House
from Opening import Opening
import copy

import pygame
import OpenGL.GL as gl
import OpenGL.GLU as glu


def Q1a():
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

    # Sets the screen color (white)
    gl.glClearColor(1, 1, 1, 1)
    # Clears the buffers and sets DEPTH_TEST to remove hidden surfaces
    #gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    #gl.glEnable(gl.GL_DEPTH_TEST)

    # Placer ici l'utilisation de gluPerspective
    glu.gluPerspective(45, (display[0] / display[1]), 0.1, 50)
    gl.glTranslate(0.0, 2, -5)
    gl.glRotate(-90, 1, 0, 0)
    gl.glBegin(gl.GL_LINES)  # Indique que l'on va commencer un trace en mode lignes (segments)
    gl.glColor3fv([125, 0, 0])  # Indique la couleur ici rouge
    gl.glVertex3fv((0, 0, -2))  # Premier vertice : dÃ©part de la ligne
    gl.glVertex3fv((0.5, 0, -2))  # DeuxiÃ¨me vertice : fin de la ligne
    gl.glColor3fv([0, 125, 0])  # Indique la couleur ici vert
    gl.glVertex3fv((0, 0, -2))  # Premier vertice : dÃ©part de la ligne
    gl.glVertex3fv((0,0.5 , -2))  # DeuxiÃ¨me vertice : fin de la ligne
    gl.glColor3fv([0, 0, 125])  # Indique la couleur ici bleu
    gl.glVertex3fv((0, 0, -2))  # Premier vertice : dÃ©part de la ligne
    gl.glVertex3fv((0, 0, -1.5))  # DeuxiÃ¨me vertice : fin de la ligne
    gl.glEnd()  # Find du tracÃ©
    pygame.display.flip()  # Met Ã  jour l'affichage de la fenÃªtre graphique

    CONTINUER=True
    while CONTINUER:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                pygame.quit()
                CONTINUER=False
                
    
def Q1b_f():
    return Configuration({'screenPosition': -5, 'xAxisColor': [1, 1, 0]}). \
        setParameter('xAxisColor', [1, 1, 0]). \
        setParameter('yAxisCo lor', [0,1,1]). \
        display()
        
def Q2b():
    # Ecriture en utilisant le chaînage
    return Configuration().add(
            Section({'position': [1, 1, 0], 'width':7, 'height':2.6})
            ) 

def Q2c():
    # Ecriture en utilisant le chaînage
    return Configuration().add(
            Section({'position': [1, 1, 0], 'width':7, 'height':2.6, 'edges': True})
            )

def Q3a():
    return(Configuration().add(Wall({'position':[1,0,1],'width':5, 'height':5,'orientation':90})))

def Q4a():
    # Ecriture en utilisant des variables : A compléter
    wall1 = Wall({'position':[0,0,0],'width':5,'height':2,'orientation':0,'thickness':0.2})
    wall2 = Wall({'position':[0,0,0],'width':5,'height':2,'orientation':90,'thickness':0.2})
    wall3 = Wall({'position':[0,-5,0],'width':5,'height':2,'orientation':90,'thickness':0.2})
    wall4 = Wall({'position':[0,5,0],'width':5,'height':2,'orientation':0,'thickness':0.2})  
    house = House({'position': [-3, 1, 0], 'orientation':0})
    house.add(wall1).add(wall3).add(wall4).add(wall2)
    return Configuration().add(house)   
    
def Q5a():  
    # Ecriture avec mélange de variable et de chaînage    
    opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
    opening2 = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})    
    return Configuration().add(opening1).add(opening2)
    
def Q5b():  
    # Ecriture avec mélange de variable et de chaînage   
    section = Section({'width':7, 'height':2.6})
    opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
    opening2 = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
    opening3 = Opening({'position': [4, 0, 1.7], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
    
    print(section.canCreateOpening(opening1))
    print(section.canCreateOpening(opening2))    
    print(section.canCreateOpening(opening3))
    return Configuration()    
    
def Q5c1():      
    section = Section({'width':7, 'height':2.6})
    opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
    sections = section.createNewOpening(opening1)
    configuration = Configuration()
    for x in sections:
        configuration.add(x)    
    return configuration     
    
def Q5c2():      
    section = Section({'width':7, 'height':2.6})
    opening2 = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
    sections = section.createNewSections(opening2)
    configuration = Configuration()
    for section in sections:
        configuration.add(section)    
    return configuration    

def Q5d():      
    pass
    
def Q6():  
    pass  
 
def main():
    # Enlever un des commentaires pour la question traitée
    
    #configuration = Q1a()
    #configuration = Q1b_f()
    #configuration = Q2b()
    #configuration = Q2c()
    #configuration = Q3a()
    #configuration = Q4a()
    configuration = Q5a()
    # configuration = Q5b()
    # configuration = Q5c1()
    # configuration = Q5c2() 
    # configuration = Q5d()
    # configuration = Q6()
    configuration.display()     
         
# Calls the main function
if __name__ == "__main__":
    main()    