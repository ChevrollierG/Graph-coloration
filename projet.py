# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 17:04:37 2020

@author: guill
"""
import pygame
import math

class point:
    
    def __init__(self,nom):
        self.nom=nom
        self.couleur=""
        self.coord=(0,0)
        
    def equal(self,valeur):#compare deux points
        if(self.nom==valeur.nom):
            return True
        else:
            return False
        

class graphe:
    
    def __init__(self,V,E,C):
        self.V=V
        self.E=E
        self.C=C

    def degre(self,valeur):#retourne le nb de segments du sommet "valeur"
        compteur=0
        for i in range (len(self.E)):
            for j in range (2):
                if(self.E[i][j].equal(valeur)):
                    compteur=compteur+1
        return compteur

    def couleur2(self):#colorie le graphe en 2 couleurs
        for i in range (len(self.E)):
            if(self.E[i][0].couleur=="" and self.E[i][1].couleur==""):
                self.E[i][0].couleur=self.C[0]
                self.E[i][1].couleur=self.C[1]
            elif(self.E[i][0].couleur==self.C[0] and self.E[i][1].couleur==""):
                self.E[i][1].couleur=self.C[1]
            elif(self.E[i][0].couleur==self.C[1] and self.E[i][1].couleur==""):
                self.E[i][1].couleur=self.C[0]
            elif(self.E[i][1].couleur==self.C[0] and self.E[i][0].couleur==""):
                self.E[i][0].couleur=self.C[1]
            elif(self.E[i][1].couleur==self.C[1] and self.E[i][0].couleur==""):
                self.E[i][0].couleur=self.C[0]
                
        for i in range(len(self.E)):
            if(self.E[i][0].couleur==self.E[i][1].couleur):
                return False
        return True
    
    def couleur3(self,i):#colorie le graphe en 3 couleurs
        if(self.complet() and self.verificateur()):
            return True
        for j in range(len(self.C)):
            self.V[i].couleur=self.C[j]
            if(self.verificateur()):
                if(self.couleur3(i+1)):
                    return True
                self.V[i].couleur=""
            else:
                self.V[i].couleur=""
        return False
    
    def verificateur(self):     #test si des point reliés sont de couleurs différentes
        for i in range(len(self.E)):
            if(self.E[i][0].couleur!="" and self.E[i][0].couleur==self.E[i][1].couleur):
                return False
        return True
    
    def complet(self):      #test si tous les points ont une couleur
        for i in range(len(self.V)):
            if(self.V[i].couleur==""):
                return False
        return True
    
    
def EquationCercle(x):
    memoire=200**2-(x-325)**2
    if(memoire<0):
        memoire=-memoire
    y=math.sqrt(memoire)+325
    return y

def AfficheGraphe(graphe):#affiche le graphe
    pygame.init()#initialise la fenetre pygame
    tailleSurface=(650,650)
    surface=pygame.display.set_mode(tailleSurface)
    Blanc=(255,255,255)
    Bleu=(0,0,255)
    Rouge=(255,0,0)
    Vert=(0,255,0)
    Noir=(0,0,0)
    Rose=(253,108,158)
    police=pygame.font.Font(None,30)
    
    surface.fill(Blanc)
    pygame.display.flip()
    x=124
    diametre=400
    while(diametre%((len(graphe.V)/2)+1)!=0):#commence l'affichage du graphe
        diametre=diametre+1
    memoire=diametre/((len(graphe.V)/2)+1)
    compteur=0
    while compteur!=len(graphe.V):#calcule des coordonnees de chaque point
        if(x==124):
            graphe.V[compteur].coord=(x,EquationCercle(x))
            compteur=compteur+1
        elif(compteur==len(graphe.V)-1):
            graphe.V[compteur].coord=(x,EquationCercle(x))
            compteur=compteur+1
        else:
            graphe.V[compteur].coord=(x,EquationCercle(x))
            compteur=compteur+1
            if compteur!=len(graphe.V):
                graphe.V[compteur].coord=(x,EquationCercle(x)-(EquationCercle(x)-324)*2)
                compteur=compteur+1
            else:
                break
        x=x+memoire
    for i in range (len(graphe.E)):#coloriage et affichage des points
        pygame.draw.line(surface,Noir,graphe.E[i][0].coord,graphe.E[i][1].coord,1)
    for i in range (len(graphe.V)):
        if(graphe.V[i].couleur=="rouge"):
            pygame.draw.circle(surface,Rouge,graphe.V[i].coord,20)
        elif(graphe.V[i].couleur=="vert"):
            pygame.draw.circle(surface,Vert,graphe.V[i].coord,20)
        elif(graphe.V[i].couleur=="bleu"):
            pygame.draw.circle(surface,Bleu,graphe.V[i].coord,20)
        else:
            pygame.draw.circle(surface, Rose, graphe.V[i].coord,20)
        texte=police.render(graphe.V[i].nom,True,Noir)
        surface.blit(texte,(graphe.V[i].coord[0]-6,graphe.V[i].coord[1]-8))
    pygame.display.flip()
    
    launched=True#boucle pour garder la fenetre pygame ouverte
    while launched:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                launched=False
    pygame.quit()
    
def AfficheErreur():#affiche un message d'erreur si le graphe n'est pas coloriable
    pygame.init()#initialise la fenetre pygame
    tailleSurface=(650,650)
    surface=pygame.display.set_mode(tailleSurface)
    Blanc=(255,255,255)
    Noir=(0,0,0)
    police=pygame.font.Font(None,30)
    surface.fill(Blanc)
    texte=police.render("Le graphe n'est pas valide",True,Noir)
    surface.blit(texte,(200,270))
    pygame.display.flip()
    
    launched=True#boucle pour garder la fenetre pygame ouverte
    while launched:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                launched=False
    pygame.quit()

#Main
if __name__ == '__main__':
    point1= point("0")
    point2= point("1")
    point3= point("2")
    point4= point("3")
    point5= point("4")
    point6= point("5")
    point7= point("6")
    point8= point("7")
    point9= point("8")
    point10= point("9")
    point11= point("10")
    point12= point("11")
    point13= point("12")
    point14= point("13")
    point15= point("14")
    couleur=["rouge","bleu","vert"]
    graphe1= graphe([point1,point2,point3,point4,point5,point6,point7,point8,point9,point10],[[point1,point2],[point2,point3],[point3,point4],[point4,point5],[point1,point5],[point1,point6],[point2,point7],[point3,point8],[point4,point9],[point5,point10],[point6,point8],[point6,point9],[point7,point9],[point7,point10],[point8,point10],[point9,point10],[point1,point3]],couleur)
    if(len(graphe1.C)==2 and graphe1.couleur2()):
        AfficheGraphe(graphe1)
    elif(len(graphe1.C)==3 and graphe1.couleur3(0)):
        AfficheGraphe(graphe1)
    else:
        AfficheErreur()