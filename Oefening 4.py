# oefening 4
# onderstaande regels vragen 2 zaken op aan de gebruiker. deze worden bewaard in een variabele.
# int is voor niet komma getal. Float is voor kommagetal (zet string om in kommagetal)
hoogte = float(input("Geef de hoogte van de driehoek op:> "))
basis = float(input("Geef de basis van de driehoek op:> "))
opp = basis * hoogte / 2
print(f"De oppervlakte van de driehoek bedraagt {opp: .2f}")
# .2f is 2 cijfers na de komma