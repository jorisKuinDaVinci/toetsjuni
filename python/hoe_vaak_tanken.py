def hoe_vaak_tanken():
    kilometers_per_liter = 12
    tankinhoud = 60
    te_rijden_afstand = 1689
    aantal_tankbeurten = 0
    while te_rijden_afstand > 0:
        te_rijden_afstand -= tankinhoud * kilometers_per_liter
        aantal_tankbeurten += 1
    return aantal_tankbeurten

print(hoe_vaak_tanken())