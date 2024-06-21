#Je bent eruit. Nadat je thuis bent gekomen ga je op vakantie naar Zuid-Spanje.
#Hoe vaak moet je tanken om op je bestemming te komen? 
#Je vertrekt met een volle tank, je rijdt de tank precies leeg en vult deze dan volledig. (je kunt dus overal tanken!)

#Schrijf een functie in Python die een integer teruggeeft met het aantal tankbeurten.
#De functie heeft als parameters: kilometers_per_liter, tankinhoud, te_rijden_afstand.
#Schrijf minimaal 10 testen voor de functie!
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