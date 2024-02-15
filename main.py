from utils import (CAPACITY, NUMBER_OF_VALUES, TUPLES, VALUES, WEIGHTS,
                   items_to_indexes, profit, real_profit, to_items, weight)

gegenstände = to_items(TUPLES)
leichter_rucksack = [0, 1, 2]
schwerer_rucksack = [96, 97, 98, 99]

for gegenstand in gegenstände[NUMBER_OF_VALUES - 3:]:  # Ausgabe der letzten 3 Einträge der Liste mit Wert und Gewicht
    print("Gegenstand Nr.", gegenstand.index + 1)
    print("Wert:", str(gegenstand.value) + "€")
    print("Gewicht:", str(gegenstand.weight) + "g")
    print()  # Leerzeile

print(weight(leichter_rucksack))  # 3311g < 25000g (Gesamtgewicht des Rucksacks)
print(real_profit(leichter_rucksack))  # 3301€ (tatsächlicher Profit = hypothetischer Profit)
print(profit(leichter_rucksack))  # 3301€ (hypothetischer Profit)

print(weight(schwerer_rucksack))  # 54878g > 25000g (Gesamtgewicht des Rucksacks)
print(real_profit(schwerer_rucksack))  # 0€ (tatsächlicher Profit)
print(profit(schwerer_rucksack))  # 55004€ (hypothetischer Profit)

erster_gegenstand = gegenstände[0]
letzter_gegenstand = gegenstände[-1]  # == gegenstände[99]

print("real_profit([0, 99]) =", real_profit([erster_gegenstand, letzter_gegenstand]))
# soviel Profit erhältst du, wenn du den ersten Gegenstand und den letzten Gegenstand mitnimmst
