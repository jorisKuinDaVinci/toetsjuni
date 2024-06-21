def hoe_vaak_tanken(kilometers_per_liter, tankinhoud, te_rijden_afstand):
    aantal_tankbeurten = 0
    while te_rijden_afstand > 0:
        te_rijden_afstand -= tankinhoud * kilometers_per_liter
        aantal_tankbeurten += 1
    return aantal_tankbeurten

#test 1
kilometers_per_liter = 12
tankinhoud = 60
te_rijden_afstand = 1689
print(hoe_vaak_tanken(kilometers_per_liter, tankinhoud, te_rijden_afstand))
#test 2
kilometers_per_liter = 13
tankinhoud = 70
te_rijden_afstand = 1689
print(hoe_vaak_tanken(kilometers_per_liter, tankinhoud, te_rijden_afstand))
#test 3
kilometers_per_liter = 15
tankinhoud = 75
te_rijden_afstand = 1689
print(hoe_vaak_tanken(kilometers_per_liter, tankinhoud, te_rijden_afstand))
#test 4
kilometers_per_liter = 14
tankinhoud = 80
te_rijden_afstand = 1689
print(hoe_vaak_tanken(kilometers_per_liter, tankinhoud, te_rijden_afstand))
#test 5
kilometers_per_liter = 19
tankinhoud = 65
te_rijden_afstand = 1689
print(hoe_vaak_tanken(kilometers_per_liter, tankinhoud, te_rijden_afstand))
#test 6
kilometers_per_liter = 16
tankinhoud = 85
te_rijden_afstand = 1689
print(hoe_vaak_tanken(kilometers_per_liter, tankinhoud, te_rijden_afstand))
#test 7
kilometers_per_liter = 17
tankinhoud = 90
te_rijden_afstand = 1689
print(hoe_vaak_tanken(kilometers_per_liter, tankinhoud, te_rijden_afstand))
#test 8
kilometers_per_liter = 18
tankinhoud = 95
te_rijden_afstand = 1689
print(hoe_vaak_tanken(kilometers_per_liter, tankinhoud, te_rijden_afstand))
#test 9
kilometers_per_liter = 20
tankinhoud = 55
te_rijden_afstand = 1689
print(hoe_vaak_tanken(kilometers_per_liter, tankinhoud, te_rijden_afstand))
#test 10
kilometers_per_liter = 21
tankinhoud = 50
te_rijden_afstand = 1689
print(hoe_vaak_tanken(kilometers_per_liter, tankinhoud, te_rijden_afstand))