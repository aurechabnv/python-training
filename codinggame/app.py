matrice_a = [
    [1, 2, 3],
    [3, 7, 3]
]

matrice_b = [
    [6, 4, 2],
    [3, 1, 0]
]

def addition_matrices(matrice_a, matrice_b):
    nb_lignes_a = len(matrice_a)
    nb_colonnes_a = len(matrice_a[0])
    nb_lignes_b = len(matrice_b)
    nb_colonnes_b = len(matrice_b[0])

    if not (nb_lignes_a == nb_lignes_b and nb_colonnes_a == nb_colonnes_b):
        raise ValueError

    nouvelle_matrice = [list(range(nb_colonnes_a)) for _ in range(nb_lignes_a)]

    for i in range(nb_lignes_a):
        for j in range(nb_colonnes_a):
            nouvelle_matrice[i][j] = matrice_a[i][j] + matrice_b[i][j]

    return nouvelle_matrice


print(addition_matrices(matrice_a, matrice_b))


matrice_a = [
    [-9, 2],
    [4, 0]
]
matrice_b = [
    [6, 4, 2],
    [3, 10, 0]
]
addition_matrices(matrice_a, matrice_b)