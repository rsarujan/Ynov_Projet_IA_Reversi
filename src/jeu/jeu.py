from .plateau import new_plateau, render, get_cellule_distribution, get_changement_autorisee_cellule, est_rempli
from .plateau import appliquer_changement_cellule, peut_changer_de_couleur, get_meneur_jeu_type, get_score_ForMinMax
from .cellule import TYPE_WHITE, TYPE_BLACK, extract_positions, new_cellule
from .color import colorize, BOLD
from .tab import new_tab, draw_cellules, draw_cellule
import random
import time
from math import inf
from reversi import clear

def startWithIA():
    print("\n######### GAME STARTED ############\n")

    try:
        plateau = new_plateau(8, 8)
        #On commence par le noir
        type_courrant = TYPE_BLACK

        print(render(plateau))

        while not est_rempli(plateau):

            print_score(get_cellule_distribution(plateau))
            print_plateau_avec_poss(plateau, type_courrant)

            while not changement_couleur_depuis_departIA(plateau, type_courrant):
                print("Position incorrect, Reessayer ")

            if not est_rempli(plateau):
                inverser_type_joueur = get_inverser_type_joueur(type_courrant)
                if peut_changer_de_couleur(plateau, inverser_type_joueur):
                    type_courrant = inverser_type_joueur
                elif not peut_changer_de_couleur(plateau, type_courrant):
                    print("\nDésolé, plus de possibilite\n")
                    break
                else:
                    print("\nLe joueur opposé ne peut rejouer, rejouer !\n")

        print(render(plateau))
        gagnant = get_meneur_jeu_type(plateau)
        print("\n#### {0} Joueur gagnant !! ####\n".format(colorize(gagnant.upper(), BOLD)))

    except KeyplateauInterrupt:
        print("\n\nFin du jeu, Aurevoir!\n\n")

    except Exception as e:
        print("An unexpected error occured, sorry.\nMessage: {0}\n".format(str(e)))



def start():
    print("\n######### GAME STARTED ############\n")

    try:
        plateau = new_plateau(8, 8)
        #On commence par le noir
        type_courrant = TYPE_BLACK

        print(render(plateau))

        while not est_rempli(plateau):

            print_score(get_cellule_distribution(plateau))
            print_plateau_avec_poss(plateau, type_courrant)

            while not changement_couleur_depuis_depart(plateau, type_courrant):
                print("Position incorrect, Reessayer ")

            if not est_rempli(plateau):
                inverser_type_joueur = get_inverser_type_joueur(type_courrant)
                if peut_changer_de_couleur(plateau, inverser_type_joueur):
                    type_courrant = inverser_type_joueur
                elif not peut_changer_de_couleur(plateau, type_courrant):
                    print("\nDésolé, plus de possibilite\n")
                    break
                else:
                    print("\nLe joueur opposé ne peut rejouer, rejouer !\n")

        print(render(plateau))
        gagnant = get_meneur_jeu_type(plateau)
        print("\n#### {0} Joueur gagnant !! ####\n".format(colorize(gagnant.upper(), BOLD)))

    except KeyplateauInterrupt:
        print("\n\nFin du jeu, Aurevoir!\n\n")

    except Exception as e:
        print("An unexpected error occured, sorry.\nMessage: {0}\n".format(str(e)))

def changement_couleur_depuis_depart(plateau, cType):
    try:
        position = int(input("Joueur ({0}), quelle position ? ".format(colorize(cType.upper(), BOLD))))
        changement_autorisee = get_changement_autorisee_cellule(plateau, cType)
        return appliquer_changement_cellule(plateau, changement_autorisee[cType][position])
    except ValueError:
        return False
    except IndexError:
        return False

def changement_couleur_depuis_departIA(plateau, cType):
    try:
        changement_autorisee = get_changement_autorisee_cellule(plateau, cType)
        if cType == TYPE_BLACK:
            position = int(input("Joueur NOIR (Humain), quelle position ? ".format(colorize(cType.upper(), BOLD))))
            return appliquer_changement_cellule(plateau, changement_autorisee[cType][position])
        else:
            print("Joueur Blanc (IA) va jouer")
            depth = len(changement_autorisee[cType])
            if depth > 4:
                depth = 4

            coup = minimax(plateau, depth, cType)
            #time.sleep(2)
            return appliquer_changement_cellule(plateau, coup[0])
    except ValueError:
        return False
    except IndexError:
        return False

def get_inverser_type_joueur(cType):
    if cType == TYPE_WHITE:
        return TYPE_BLACK

    return TYPE_WHITE


def print_plateau_avec_poss(plateau, cType):
    changement_autorisee = get_changement_autorisee_cellule(plateau, cType)
    print(render(plateau, extract_positions(changement_autorisee[cType])))


def print_score(cell_distribution):
    print("\n#### SCORE (BLANC: {0}, NOIR: {1}) ####\n".format(
        cell_distribution[TYPE_WHITE],
        cell_distribution[TYPE_BLACK]
    ))

def minimax(plateau, depth, player):

    if player == TYPE_BLACK:
        best = [new_cellule(-1, -1), inf]
    else:
        best = [new_cellule(-1, -1), -inf]

    if depth == 0 or est_rempli(plateau):
        score = get_score_ForMinMax(plateau)
        return [new_cellule(-1, -1), score]
    posibility = get_changement_autorisee_cellule(plateau, player)
    for position in posibility[player]:
        cel_replaces = appliquer_changement_cellule(plateau, position)

        score = minimax(plateau, depth - 1, get_inverser_type_joueur(player))
        draw_cellule(plateau, new_cellule(position['x'], position['y']))
        for cel in cel_replaces:
            cel['type'] = get_inverser_type_joueur(cel['type'])
        draw_cellules(plateau, cel_replaces)

        score[0] = position

        if player == TYPE_BLACK:
            if score[1] < best[1]:
                best = score
        else:
            if score[1] > best[1]:
                best = score
    return best


