import math
getal1 = int(input("Geef een getal op: "))
getal2 = int(input("Geef een getal op: "))

# totaal = (getal1 + getal2) * (getal1 + getal2)
# of totaaal = (getal1 + getal2) ** x
totaal = math.pow(getal1 + getal2, 2)
# de 2 (x in #) is telkens voor de macht
# totaal = math.pow(getal1 + getal2, x)

print(f"{getal1} + {getal2} ^2 = {totaal: .0f}")