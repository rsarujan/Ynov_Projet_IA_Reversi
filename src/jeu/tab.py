from .color import UNDERLINE, colorize


def new_tab(xTaille, yTaille, value=None):
    return [[value for x in range(xTaille)] for y in range(yTaille)]


def draw_cellule(tab, cellule):
    tab[cellule['y']][cellule['x']] = cellule


def draw_cellules(tab, cellules=[]):
    for cellule in cellules:
        draw_cellule(tab, cellule)


def get_taille(tab):
    lignes_cmpt = len(tab)

    if lignes_cmpt is 0:
        return (0, 0)

    return (len(tab[0]), lignes_cmpt)


def get_cellule(tab, xPos, yPos, default=None):
    """ Retourner la valeur de la cellule sinon elle renvoie le cellule par defaut """

    try:
        # On enlève les index négatives
        if yPos < 0 or xPos < 0:
            raise IndexError
        return tab[yPos][xPos]
    except LookupError:
        return default


def render(tab):

    xTaille, yTaille = get_taille(tab)
    render_str = "_" * (xTaille * 2 + 1) + "\n"

    for ligne in tab:
        render_str += "|"
        for val in ligne:
            render_str += '%5s' % colorize(val, UNDERLINE) + "|"
        render_str += "\n"

    return render_str
