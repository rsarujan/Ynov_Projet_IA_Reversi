from .cellule import new_cellule, get_symbol, get_types, TYPE_WHITE, TYPE_BLACK, TYPE_EMPTY, extract_positions
from .tab import new_tab, draw_cellules, get_taille as get_tab_taille, get_cellule as get_tab_cellule, render as tab_render
from .vecteur import get_direction_vecteurs, get_generateur_vecteur


def new_plateau(xTaille, yTaille):
    """ Creation du plateau  """

    validation_plateau_taille(xTaille, yTaille)

    tab = new_tab(xTaille, yTaille)
    draw_cellules(tab, get_cellule_vide(xTaille, yTaille) + get_cellule_depart(tab))

    return tab


def identique(x):
    return x % 2 == 0


def validation_plateau_taille(xTaille, yTaille):
    """ validation plateau taille """

    if not identique(xTaille) or not identique(yTaille):
        raise ValueError("Le plateau x/y taille doivent être identique")
    if yTaille < 4 or xTaille < 4:
        raise ValueError("Le plateau doit avoir 4 lignes/colonnes")


def get_cellule_vide(xTaille, yTaille):
    """ Retourner cellule vide """

    cellule_vide = []

    for yPos in range(0, yTaille):
        for xPos in range(0, xTaille):
            cellule_vide.append(new_cellule(xPos, yPos, TYPE_EMPTY))

    return cellule_vide


def get_cellule_depart(tab):
    """ Retourner case de départ """

    xTaille, yTaille = get_tab_taille(tab)

    x_milieu = int(xTaille/2)
    y_milieu = int(yTaille/2)

    return [
        new_cellule(x_milieu, y_milieu, TYPE_WHITE),
        new_cellule(x_milieu - 1, y_milieu - 1, TYPE_WHITE),
        new_cellule(x_milieu - 1, y_milieu, TYPE_BLACK),
        new_cellule(x_milieu, y_milieu - 1, TYPE_BLACK)
    ]


def get_cellule_distribution(tab):
    """ Retourner cellule distribue par type """

    distribution = {TYPE_WHITE: 0, TYPE_BLACK: 0, TYPE_EMPTY: 0}

    for ligne in tab:
        for cellule in ligne:
            distribution[cellule['type']] += 1

    return distribution


def get_meneur_jeu_type(tab):

    distribution = get_cellule_distribution(tab)

    if(distribution[TYPE_WHITE] > distribution[TYPE_BLACK]):
        return TYPE_WHITE

    return TYPE_BLACK

def get_score_ForMinMax(tab):

    distribution = get_cellule_distribution(tab)

    return distribution[TYPE_WHITE] - distribution[TYPE_BLACK]


    
def est_rempli(tab):
    return get_cellule_distribution(tab)[TYPE_EMPTY] == 0


def render(tab, position_proposee=[]):
    """ Print Plateau (str) """

    view_tab = []
    type_connu = get_types()
    charactere = ""

    for ligne_idx, ligne in enumerate(tab):
        view_tab.append([])
        for cellule in ligne:
            cellule_position = extract_positions([cellule])[0]
            if cellule_position in position_proposee:
                charactere = str(position_proposee.index(cellule_position))
            elif cellule['type'] in type_connu:
                charactere = get_symbol(cellule)
            view_tab[ligne_idx].append(charactere)

    return tab_render(view_tab)


def get_changement_cell_apres_changement_effectuee(tab, cellule):
    """ Retourner tous les cellules modifiés après modification """

    cellules_retournees = []
    empty_cellule = new_cellule(0, 0, TYPE_EMPTY)
    xPos, yPos, cType = cellule['x'], cellule['y'], cellule['type']

    if not get_tab_cellule(tab, xPos, yPos, empty_cellule)['type'] is TYPE_EMPTY:
        return []

    # Affiche toutes les possibilites avec vecteurs (hors vecteurs null)
    for vecteur in get_direction_vecteurs():
        generateur_vecteur = get_generateur_vecteur((xPos, yPos), vecteur)
        vecteur_retournant_cellules = []

        # On continue tant que la cellule n'est pas vide ayant la meme couleur
        for (x, y) in generateur_vecteur:
            if get_tab_cellule(tab, x, y, empty_cellule)['type'] in [TYPE_EMPTY, cType]:
                break
            vecteur_retournant_cellules.append(new_cellule(x, y, cType))

        # Vérification si pion retournés et identique à la dernière cellule du même type
        derniere_cellule = get_tab_cellule(tab, x, y, empty_cellule)
        if len(vecteur_retournant_cellules) > 0 and derniere_cellule['type'] is cType:
            cellules_retournees += vecteur_retournant_cellules

    return cellules_retournees


def est_legal_changement_couleur(tab, cellule):
    return len(get_changement_cell_apres_changement_effectuee(tab, cellule)) > 0


def peut_changer_de_couleur(tab, cType):
    return len(get_changement_autorisee_cellule(tab, cType)[cType]) > 0


def get_changement_autorisee_cellule(tab, cType):
    changement_autorisee_cellule = {TYPE_WHITE: [], TYPE_BLACK: []}

    for ligne_idx, ligne in enumerate(tab):
        for col_idx, col in enumerate(ligne):
            cellule_change = new_cellule(col_idx, ligne_idx, cType)
            if est_legal_changement_couleur(tab, cellule_change):
                changement_autorisee_cellule[cType].append(cellule_change)
    return changement_autorisee_cellule


def appliquer_changement_cellule(tab, cellule):
    """ Appliquer le changement de cellule """

    if not est_legal_changement_couleur(tab, cellule):
        return False

    cellules_retournees = get_changement_cell_apres_changement_effectuee(tab, cellule)
    draw_cellules(tab, [cellule] + cellules_retournees)

    return cellules_retournees
