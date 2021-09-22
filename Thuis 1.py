prijs_bouwgrond = int(input("Prijs van de bouwgrond? "))
prijs_gebouw = int(input("Prijs van het gebouw? "))
totale_prijs_e = prijs_bouwgrond * prijs_gebouw
totale_prijs_i = totale_prijs_e + totale_prijs_e * 0.21
print(f"De totale kostrpijs bedraagt {totale_prijs_i: .0f}")
