import pygame
from pygame.locals import *
import random as r
import re
#importation de tout les modules nécessaires

pygame.display.init()
pygame.font.init()
#On initialise pygame
pygame.display.set_caption('2048')

fenetre = pygame.display.set_mode((1000, 720))
#creation de la fenetre
fond = pygame.image.load("pics/fond.jpg").convert()
#mise en place du fond de l'image
icone = pygame.image.load("pics/icon.jpg").convert_alpha()
pygame.display.set_icon(icone)
fenetre.blit(fond,(0,0))
#positionnement du fond
pygame.display.flip()
#actualisation

xa=30
ya=30

grille=\
[".",".",".","."],[".",".",".","."],[".",".",".","."],[".",".",".","."]

grillesav=[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."]

grillesav2=\
[".",".",".","."],[".",".",".","."],[".",".",".","."],[".",".",".","."]

def normal():
	for x in range(4):
		for y in range(4):
			if grille[x][y]!=".":
				grille[x][y]=re.sub("[^0-9]", "", grille[x][y])
				#permet d'enlever les lettres des chiffres

def checkdead():
	#regarde si un mouvement est toujours possible
	for x in range(1,4):
		for y in range(4):
			if grille[y][x-1]==grille[y][x]!=".":
				return True
	for x in range(3,0,-1):
		for y in range(4):
			if grille[y][x-1]==grille[y][x]!=".":
				return True
	for x in range(4):
		for y in range(1,4):
			if grille[y-1][x]==grille[y][x]!=".":
				return True
	for x in range(4):
		for y in range(3,0,-1):
			if grille[y-1][x]==grille[y][x]!=".":
				return True
	return False

def pos():
	if r.randrange(1,10)==1:
		grille[posy][posx]="4"
	else:
		grille[posy][posx]="2"

def traitement():
	#Permet de réunir les blocs vers la direction souhaitée
	global trait
	trait=0
	#trait permet de savoir si ce mouvement a été bien effectué
	if choix=="4":
		for bc in range(3):
			for x in range(1,4):
				for y in range(4):
					#Cette boucle permet de gerer toute les cases possibles
					#3 fois de suite (car 3 déplacements max possible)
					if grille[y][x-1]=="." and grille[y][x]!=".":
						grille[y][x-1]=grille[y][x]
						grille[y][x]="."
						#Mouvement effectué, trait=1
						trait=1
	if choix=="6":
		for bc in range(3):
			for x in range(3):
				for y in range(4):
					if grille[y][x+1]=="." and grille[y][x]!=".":
						grille[y][x+1]=grille[y][x]
						grille[y][x]="."
						trait=1
	if choix=="8":
		for bc in range(3):
			for x in range(4):
				for y in range(1,4):
					if grille[y-1][x]=="." and grille[y][x]!=".":
						grille[y-1][x]=grille[y][x]
						grille[y][x]="."
						trait=1
	if choix=="2":
		for bc in range(3):
			for x in range(4):
				for y in range(3):
					if grille[y+1][x]=="." and grille[y][x]!=".":
						grille[y+1][x]=grille[y][x]
						grille[y][x]="."
						trait=1

def assemblage():
	#¨Permet de rassembler les blocs identiques
	global assem
	global score
	assem=0
	#assem permet de savoir si l'action a été faite
	if choix=="4":
		for x in range(1,4):
			for y in range(4):
				#Check toutes les cases dans un ordre gauche droite
				if grille[y][x-1]==grille[y][x]!=".":
					score+=int(grille[y][x])*2
					#On multiplie par 2 la case et on rajoute une lettre, 
					#la lettre permet de savoir quel case a été modifiée
					grille[y][x-1]=str(int(grille[y][x-1])*2)+"a"
					#On remplace la case d'avant par un point
					grille[y][x]="."
					#Effectué, on met assem à 1
					assem=1
	if choix=="6":
		for x in range(3,0,-1):
			for y in range(4):
				#Check toutes les cases dans un ordre droite gauche
				if grille[y][x-1]==grille[y][x]!=".":
					score+=int(grille[y][x])*2
					grille[y][x-1]=str(int(grille[y][x])*2)+"a"
					grille[y][x]="."
					assem=1
	if choix=="8":
		for x in range(4):
			for y in range(1,4):
				if grille[y-1][x]==grille[y][x]!=".":
					score+=int(grille[y][x])*2
					grille[y-1][x]=str(int(grille[y-1][x])*2)+"a"
					grille[y][x]="."
					assem=1
	if choix=="2":
		for x in range(4):
			for y in range(3,0,-1):
				if grille[y-1][x]==grille[y][x]!=".":
					score+=int(grille[y][x])*2
					grille[y-1][x]=str(int(grille[y][x])*2)+"a"
					grille[y][x]="."
					assem=1

def fin():
	global finn
	#Fin du jeu lorsqu'on perd
	fin=pygame.image.load("pics/end.png").convert_alpha()
	fenetre.blit(fin,(0,0))
	pygame.display.flip()
	s=False
	while s==False:
		for event in pygame.event.get():
			if event.type==KEYDOWN:
				if event.key==K_RETURN:
					s=True
				if event.key==K_RSHIFT:
					for a in range(4):
						for b in range(4):
							grille[a][b]=grillesav2[a][b]
					nbrmvt=coupsav
					score=scoresav
					finn=False
					s=True

def aff(xa,ya):
	xa=30
	ya=30
	for x in range(4):
		for y in range(4):
			if grille[x][y]!=".":
				bc=grille[x][y]
				block = pygame.image.load(f"pics/{bc}.jpg").convert()
				#bc est la valeur du block
			else:
				block = pygame.image.load("pics/vide.jpg").convert()

			fenetre.blit(block,(xa,ya))
			#on actualise les blocks
			xa+=170
			#on regarde de gauche a droite et de haut en bas
			if xa==710:
				ya+=170
				xa=30

def scorecoups():
	coup = font.render(str(nbrmvt), 1, (255, 255, 255))
	scorea = font.render(str(score), 1, (255, 255, 255))
	if nbrmvt<10:
		fenetre.blit(coup, (847,223))
	elif nbrmvt>=10 and nbrmvt<100:
		fenetre.blit(coup, (840,223))
	elif nbrmvt>=10 and nbrmvt<1000:
		fenetre.blit(coup, (833,223))
	elif nbrmvt>=1000 and nbrmvt<10000:
		fenetre.blit(coup, (826,223))
	elif nbrmvt>=10000 and nbrmvt<100000:
		fenetre.blit(coup, (819,223))
	else:
		fenetre.blit(coup, (812,223))

	if score<10:
		fenetre.blit(scorea, (847,355))
	elif score>=10 and score<100:
		fenetre.blit(scorea, (840,355))
	elif score>=100 and score<1000:
		fenetre.blit(scorea, (833,355))
	elif score>=1000 and score<10000:
		fenetre.blit(scorea, (826,355))
	elif score>=10000 and score<100000:
		fenetre.blit(scorea, (819,355))
	elif score>=100000 and score<1000000:
		fenetre.blit(scorea, (812,355))
	else:
		fenetre.blit(scorea, (805,355))


checkmvt=1

if not "." in str(grille):
	checkmvt=0

#checkmvt permet de savoir si le mouvement d'avant était correct
nbrmvt=0
#nbrmvt permet de savoir le nombre de mouvements effectués
continuer=1

score=0
check2048=False
font = pygame.font.SysFont("arial", 35)
finn=False
scoresav=0
aff(xa,ya)
scorecoups()
while continuer==1:
	#Condition de victoire
	c=0
	for a in range(4):
		for b in range(4):
			grillesav2[a][b]=grillesav[c]
			c+=1	
	coupsav=nbrmvt-1
	posx=r.randrange(0,4)
	posy=r.randrange(0,4)
	#On genere l'emplacement de la nouvelle case
	test=0
	while grille[posy][posx]!=".":
		#Tant que l'emplacement est pas trouvé, on continu
		posx=r.randrange(0,4)
		posy=r.randrange(0,4)
		test+=1
		if test>100:
			#Si l'emplacement n'est pas trouvé depuis longtemps,
			#fin du jeu
			if not checkdead():
				fin()
				exit()
			else:
				break
	if checkmvt:
		#Si le mouvement d'avant était correct
		pos()
		#On place le nouveau bloc
	if "2048" in str(grille) and check2048==False:
		fin2048=pygame.image.load("pics/win2048.png").convert_alpha()
		normal()
		aff(xa,ya)
		fenetre.blit(fin2048,(0,0))
		pygame.display.flip()
		s=False
		while s==False:
			for event in pygame.event.get():
				if event.type==KEYDOWN:
					if event.key==K_RETURN:
						s=True
						check2048=True
	normal()
	s=False
	retour=False
	while s==False:
		#boucle permettant l'affichage
		for event in pygame.event.get():
			if event.type==QUIT:
				exit()
			#Si on veut quitter par la croix
			if event.type==KEYDOWN:
				#tout les evenement de clavier
				if event.key==K_UP:
					choix="8"
					#Choix=8 => référence au premier script
					s=True
					#On sort de la boucle
				if event.key==K_DOWN:
					choix="2"
					s=True
				if event.key==K_RIGHT:
					choix="6"
					s=True
				if event.key==K_LEFT:
					choix="4"
					s=True
				if event.key==K_RSHIFT:
					for a in range(4):
						for b in range(4):
							grille[a][b]=grillesav2[a][b]
					nbrmvt=coupsav
					score=scoresav
					retour=True

		if finn==True:
			break
		fenetre.blit(fond,(0,0))
		#mise a jour du fond
		aff(xa,ya)
		#mise a jour de l'emplacement des blocks#
		scorecoups()
		if retour==True:
			undo=pygame.image.load("pics/undo.png").convert_alpha()
			fenetre.blit(undo,(744,414))

		pygame.display.flip()
	#mise a jour de l'écran
	grillesav=list(str(grille).replace("[", "").replace("]", "").replace("'", "").replace("(", "").replace(")", "").split(","))
	grillesav = [parcour.replace(" ","") for parcour in grillesav]
	#Demande de swipe
	traitement()
	#traitement, rassemble toute les cases d'un coté
	scoresav=score
	assemblage()
	#assemble si possible
	if assem or trait:
		checkmvt=1
		nbrmvt+=1
		#checkmvt à 1, le mouvement est correct
	else:
		grillesav=list(str(grillesav2).replace("[", "").replace("]", "").replace("'", "").replace("(", "").replace(")", "").split(","))
		grillesav = [parcour.replace(" ","") for parcour in grillesav]
		checkmvt=0
		#checkmvt à 1, le mouvement est incorrect on a pas de nouveau bloc
	traitement()
	#On traite de nouveau, permet de rassembler les cases flottantes
	#a cause de l'assemblage (ex 8|.|4|.)
	#Fin de la boucle
#On est hors de la boucle, condition remplie=2048
if not finn:
	normal()
	aff(xa,ya)
	fin=pygame.image.load("pics/win.png").convert_alpha()
	fenetre.blit(fin,(0,0))
	pygame.display.flip()
	s=False
	while s==False:
		for event in pygame.event.get():
			if event.type==KEYDOWN:
				if event.key==K_RETURN:
					s=True
	#On sort du programme