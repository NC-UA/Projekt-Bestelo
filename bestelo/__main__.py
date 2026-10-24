from bestelo.kunden import Kunde, Privatkunde

anna = Kunde(1001, "  Anna Müller ", "anna@example.com")
print(anna)
print(repr(anna))
print(anna.begruessung(), anna.rabattsatz())
print(anna == Kunde(1001, "A. Müller", "a.mueller@example.com"))
print(Kunde.ist_gueltige_email("anna-at-example.com"))

try:
    anna.name = " "
except ValueError as fehler:
    print("Fehler:", fehler)


anna = Privatkunde(1001, "Anna Müller", "anna@example.com", 1995, stammkunde=True)
print(anna)
print(repr(anna))
print(anna.alter(2026), anna.rabattsatz())
print(isinstance(anna, Kunde))


"""diese __main__.py Datei soll man im VS-Code im Termin mit folgendem Befehl ausführen:
python -m bestelo (so steht auch im Skript auf Seite 13, wenn ich das richtig verstanden habe).
Wenn man __main__.py über "Run Python File Button startet, dann kommt es zu folgen Fehlermeldung: 
'ModuleNotFoundError: No module named 'bestelo' """