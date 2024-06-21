def hoe_vaak_tanken(kilometers_per_liter):
    tankinhoud = 60
    te_rijden_afstand = 1689
    aantal_tankbeurten = 0
    while te_rijden_afstand > 0:
        te_rijden_afstand -= tankinhoud * kilometers_per_liter
        aantal_tankbeurten += 1
    return aantal_tankbeurten

#test 1
kilometers_per_liter = 12
print(hoe_vaak_tanken(kilometers_per_liter))
#test 2
kilometers_per_liter = 13
print(hoe_vaak_tanken(kilometers_per_liter))
#test 3
kilometers_per_liter = 15
print(hoe_vaak_tanken(kilometers_per_liter))
#test 4
kilometers_per_liter = 14
print(hoe_vaak_tanken(kilometers_per_liter))
#test 5
kilometers_per_liter = 19
print(hoe_vaak_tanken(kilometers_per_liter))
#test 6
kilometers_per_liter = 16
print(hoe_vaak_tanken(kilometers_per_liter))
#test 7
kilometers_per_liter = 17
print(hoe_vaak_tanken(kilometers_per_liter))
#test 8
kilometers_per_liter = 18
print(hoe_vaak_tanken(kilometers_per_liter))
#test 9
kilometers_per_liter = 20
print(hoe_vaak_tanken(kilometers_per_liter))
#test 10
kilometers_per_liter = 21
print(hoe_vaak_tanken(kilometers_per_liter))