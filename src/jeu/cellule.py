TYPE_EMPTY = "empty"
TYPE_WHITE = "Blanc"
TYPE_BLACK = "Noir"


def new_cellule(xPos, yPos, cType=TYPE_EMPTY):
    return {'x': xPos, 'y': yPos, 'type': cType}


def get_symbol(cellule):
    if cellule['type'] == TYPE_BLACK:
        return "○"
    if cellule['type'] == TYPE_WHITE:
        return "●"

    return " "


def get_types():
    return {TYPE_WHITE, TYPE_BLACK, TYPE_EMPTY}


def extract_positions(cellules):
    return list(map(lambda cellule: (cellule['x'], cellule['y']), cellules))
