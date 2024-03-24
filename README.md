# Programmierworkshop zum Rucksackproblem

## Worum geht's?

Stell dir vor, du brichst in ein Museum ein und stiehlst wertvolle Ausstellungsstücke. Du hast einen Rucksack, aber
du kannst nicht alle Gegenstände mitnehmen, weil dein Rucksack sonst zu schwer wird. Du musst also eine Auswahl treffen
und einige Gegenstände zurücklassen. Von allen Ausstellungsstücken kennst du das Gewicht und den Wert.
Überlege dir gut, welche Gegenstände du mitnehmen willst, um den maximalen Profit herauszuholen.

## Aufgabenstellung

Gegeben ist ein Rucksack mit einem maximalen Gewicht von 25kg. Es gibt 100 Gegenstände, die in den Rucksack gepackt werden können. Jeder Gegenstand hat ein Gewicht und einen Wert. Es soll eine Auswahl getroffen werden, welche Gegenstände in den Rucksack gepackt werden, sodass der Gesamtwert der Gegenstände maximal ist und das Gewicht nicht überschritten wird.

## Die Ausstellungstücke

Die Ausstellungsstücke des Museums mit ihren Werten und Gewichten sind in der Datei `values.json` codiert. Die Datei enthält eine Liste von 100 Gegenständen. Jeder Gegenstand ist ein Tupel, das aus drei Werten besteht: seinem Gewicht, seinem Wert und seiner Nummer. Die Nummer ist die Position des Gegenstandes in der Liste. Die Liste hat diese Struktur:


```json
[
  [1026, 1010, 0], // Gegenstand 1 mit Gewicht 1026 Gramm und Wert 1010€
  [1108, 1105, 1], // Gegenstand 2 mit Gewicht 1108 Gramm und Wert 1105€
  [1177, 1186, 2] // Gegenstand 3 mit Gewicht 1177 Gramm und Wert 1186€
  ...
]
```

Du musst dich allerdings nicht um die JSON-Datei kümmern. Es gibt eine vorbereitete Funktion,
die die Daten aus der Datei liest, sodass du sie in deinem Programm verwenden kannst.

## Voraussetzungen

- du hast **Python3** auf deinem Computer installiert (Version 3.8 oder höher)
- du hast einen Texteditor oder eine Entwicklungsumgebung (IDE) auf deinem Computer installiert
- du weißt, wie du ein Terminal auf deinem Computer öffnest
  - Windows: `Win + R` und dann `powershell` eingeben
  - Linux: `Strg + Alt + T`
  - Mac: `Cmd + Leertaste` und dann `terminal` eingeben

## Und jetzt?

- Wenn du mit **_GitHub_** vertraut bist, clone dieses Repository
- Wenn du nicht mit **_GitHub_** vertraut bist, lade die Dateien
  - `values.json`,
  - `main.py` und
  - `utils.py` herunter.
  - Speichere sie dann in einem Ordner
- Öffne den Ordner in deiner IDE (Entwicklungsumgebung)
- Du kannst `main.py` in deiner IDE starten.
- Wenn du keine Entwicklungsumgebung hast, öffne den Ordner im normalen Texteditor (z.B. Notepad)
- Starte ein Terminal
  - Navigiere in das Verzeichnis, in dem du die Dateien gespeichert hast mit `cd pfad/zum/ordner`
- Du kannst `main.py` im Terminal starten indem du `python main.py` eingibst
  - Linux/Mac: `python3 main.py`
- öffne die Datei `main.py` in deinem Editor und schreibe den Code, der dir den maximalen Profit beschert

## Und los!

Du kannst die Funktionen `weight`, `real_profit` und `profit` verwenden.
Sie sollen dir helfen, den maximalen Profit zu berechnen.
Probiere ruhig mal per Hand verschiedene Kombinationen von Gegenständen 
aus, um ein Gefühl für das Problem zu bekommen.

```python
# Datei: main.py
...
leichter_rucksack = [0, 1, 2]
schwerer_rucksack = [96, 97, 98, 99]

print(weight(leichter_rucksack))  # 3311g < 25000g (Gesamtgewicht des Rucksacks)
print(real_profit(leichter_rucksack))  # 3301€ (tatsächlicher Profit = hypothetischer Profit)
print(profit(leichter_rucksack))  # 3301€ (hypothetischer Profit)

print(weight(schwerer_rucksack))  # 54878g > 25000g (Gesamtgewicht des Rucksacks)
print(real_profit(schwerer_rucksack))  # 0€ (tatsächlicher Profit)
print(profit(schwerer_rucksack))  # 55004€ (hypothetischer Profit)
```

## Erlaubte Hilfsmittel

**ALLE**, also insbesondere:

- StackOverflow
- Python Packages (z.B. numpy)
  - optional, das Problem kann auch mit den *Bordmitteln* gut bewältigt werden
- ChatGPT
- Andere Programme (z.B. Excel, MatLab, ...)
- Andere Programmiersprachen

## Teamarbeit

Tip: Tut euch gerne in kleinen Teams von 2-3 Personen zusammen.
Ihr könnt gemeinsam Ideen sammeln, wie ihr das Problem am besten löst.

## Challenge

**Das Team, das den höchsten Profit erzielt, sichert sich Ruhm und Ehre bis in alle Ewigkeit und erhält eine kleine Überraschung.**

## Hinweis

Wenn du glaubst, dass du keinen höheren Profit mehr erzielen kannst, dann versuche, deinen Code zu beschleunigen.

## Variante (schwieriger!)

Wenn du die optimale Lösung für das Rucksackproblem mit ganzen Zahlen gefunden hast, versuche,
eine Lösung für das Rucksackproblem mit Fließkommazahlen zu finden.
Setze dazu in der Datei `utils.py` die Variable `INTEGER` auf `False`.