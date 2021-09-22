totaal_aantal_seconden = int(input("Geef het aantal seconden op: "))
aantal_dagen = totaal_aantal_seconden // 86400
# een gehele deling (//) geeft een quotient zonder gedeelt na de komma
# een gewone deling (/) geeft een quotient met komma terug

# hoeveel sec schieten er nog over
rest = totaal_aantal_seconden % 86400
# we gebruiken de modulo-operator (%) --> dit geeft de rest van eeen deling terug

aantal_uren = rest // 3600

rest = rest % 3600

aantal_minuten = rest // 60
# niet nodig voor 2de variable want waarde wordt vervangen

aantal_seconden = rest % 60
print(f"d:h:m:s -> {aantal_dagen}:{aantal_uren}:{aantal_minuten}:{aantal_seconden}")