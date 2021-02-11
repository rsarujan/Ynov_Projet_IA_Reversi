#!/usr/bin/env python
from subprocess import call
from jeu import jeu
import time, os


  
def clear(): 
    return call('clear' if os.name =='posix' else 'cls') 
 
if __name__ == "__main__":
	clear()
	choix=0

	while choix!=5 :
		print("\t\t\t.:Reversi:.\n\t\t\t")
		print("  1. Jeu  a deux joueur Humain")
		print("  2. Joeur contre la machine")
		print("  3. Regle de jeu")
		print("  4. Quittez")
		choix = int(input("\t\t Choix : "))

		if choix < 1 or choix > 4:
			clear()
			print("Reversi")
			print("Option Invalide!")
			choix = 0
			continue
			  
			  
		if (choix==1):
			clear()
			print("\t\t\t.:Reversi:.\n\t\t\t")
			print( "  La Partir va commencer...")
			time.sleep(1)
			jeu.start()
			break
				
				
		if(choix==2) :
			clear()
			print("\t\t\t.:Reversi:.\n\t\t\t")
			print( "  La Partir va commencer...")
			time.sleep(1)
			jeu.startWithIA()
			break

		if(choix==3):
			clear()
			print("\thttps://www.regledujeu.fr/othello/")
			break


		if(choix==4):
			clear()
			print("A bientot pour de nouvelle partie avec REVERSI \n")
			break
	            