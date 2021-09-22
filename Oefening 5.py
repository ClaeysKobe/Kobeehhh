dagen = int(input("Geef het aantal dagen: "))
uren = int(input("Geef het aantal uren op: "))
minuten = int(input("Geef het aantal minuten op: "))
seconden= int(input("Geef het aantal seconden op: "))

totaal_seconden = seconden + minuten * 60 + uren * 3600 + dagen * 86400

print(f"Het totale aantal seconden bedraagt {totaal_seconden}")