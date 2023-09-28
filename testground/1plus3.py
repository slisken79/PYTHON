def ett_plus_tre(nummer):
    total = nummer
    for i in range(1, 4):
        total += nummer + i
    return total


# Testa funktionen med exempel
#resultat = ett_plus_tre(5)
#print(resultat)  # Förväntat utresultat: 26 (5 + 6 + 7 + 8)


def ett_plus_tre(nummer=0):
    """
    Funktionen summerar ett givet nummer med dess tre följande nummer.

    :param nummer: Det startnummer som ska användas för summeringen (defaultvärde är 0 om inget nummer anges).
    :return: Summan av det givna numret och dess tre följande nummer.
    """
    total = nummer
    for i in range(1, 4):
        total += nummer + i
    return total


# Testa funktionen med exempel
resultat = ett_plus_tre(5)
print(resultat)  # Förväntat utresultat: 26 (5 + 6 + 7 + 8)
