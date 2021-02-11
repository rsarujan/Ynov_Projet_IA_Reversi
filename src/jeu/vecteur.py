from itertools import product
import operator


def get_direction_vecteurs():
    """ Retouner les différents vecteurs 
    		N
		 NO |  NE
		   \|/ 
    	O --●--	E
    	   /|\
		 SO | SE
    		S
    """

    direction_vecteurs = product((-1, 0, 1), (-1, 0, 1))
    return (vecteurs for vecteurs in direction_vecteurs if not vecteurs == (0, 0))


def add_vecteur(v1, v2):
    return tuple(map(operator.add, v1, v2))


def get_generateur_vecteur(vecteur_base, vecteur):
    vecteur_modifie = vecteur_base
    while True:
        vecteur_modifie = add_vecteur(vecteur_modifie, vecteur)
        yield vecteur_modifie
