import calc

zahl1 = 0
zahl2 = 0
operator = None
bedingung = True

while bedingung:
    print("Welche Berechnung möchten Sie durchführen?")
    print("+ | - | / | * | x² | log | wurzel")
    operator = input("").strip().lower()
    if operator in ["+","-","/","*"]:
        try:
            zahl1 = int(input("Zahl 1: ").strip())
            zahl2 = int(input("Zahl 2: ").strip())
        except Exception as error:
            print("Es ist ein Fehler aufgetreten! Bitte überprüfen Sie die Eingabe")
    elif operator in ["log","wurzel","x²"]:
        try:
            zahl1 = int(input("Zahl: ").strip())
        except Exception as error:
            print("Es ist ein Fehler aufgetreten! Bitte überprüfen Sie die Eingabe")
    else:
        print("Es ist ein Fehler aufgetreten! Bitte überprüfen Sie die Eingabe")

    if operator == "+":
        ergebnis = calc.addition(zahl1, zahl2)
        print("Das Ergebnis ist: ", str(ergebnis))

    elif operator == "-":
        ergebnis = calc.subtraktion(zahl1, zahl2)
        print("Das Ergebnis ist: ", str(ergebnis))
    elif operator == "*":
        ergebnis = calc.multiplikation(zahl1, zahl2)
        print("Das Ergebnis ist: ", str(ergebnis))
    elif operator == "/":
        ergebnis = calc.division(zahl1, zahl2)
        print("Das Ergebnis ist: ", str(ergebnis))
    elif operator == "log":
        ergebnis = calc.logarithmus(zahl1)
        print("Das Ergebnis ist: ", str(ergebnis))
    elif operator == "x²":
        ergebnis = calc.quadrat(zahl1)
        print("Das Ergebnis ist: ", str(ergebnis))
    elif operator == "wurzel":
        ergebnis = calc.wurzel(zahl1)
        print("Das Ergebnis ist: " + str(ergebnis))

    decision = input("Möchten Sie es erneut versuchen? (ja | nein) : ").strip().lower()
    if decision == "nein":
        bedingung = False

