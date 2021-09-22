print("*** Welkom bij het kassasysteem ***")
broeken = int(input("Hoeveel broeken werden er verkocht? "))
tshirts = int(input("Hoeveel T-shirts werden er verkocht? "))
vesten = int(input("Hoeveel vesten werden er verkocht? "))
prijs_broeken = broeken * 70.5
prijs_tshirts = tshirts * 20.89
prijs_vesten = vesten * 100.3
totaal = prijs_broeken + prijs_tshirts + prijs_vesten 
print(f"U Kocht: \n\tBroeken: {broeken} stuk(s) \n\tT-Shirts: {tshirts} stuk(s) \n\tVesten: {vesten} stuk(s) \nTotaal te betalen: {totaal: .2f}")