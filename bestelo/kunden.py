from datetime import date

class Kunde:
    def __init__(self, kundennummer: int, name: str, email: str) -> None:
        #dieser Block prüft, ob Kundennummer kleiner als 1000 ist. Wenn ja -> ValueError, 
        # wenn nein -> wird der Wert als gültige Kundennummer gespeichert
        if kundennummer < 1000:
            raise ValueError("Fehler: Kundennummer darf nicht kleiner als 1000 sein!")
        else:
            self._kundennummer = kundennummer

        self.name = name
        self.email = email

    @property #Kundennummer wird nur lesend gemacht...keine Setter-Methode
    def kundennummer(self) -> int:
        return self._kundennummer

    @property
    def name(self) -> str:
        return self._name
    
    #Name wird durch Setter-Methode definiert. Wenn es keinen Namen gibt (Name ist "leer") -> ValueError,
    # ansonsten wird der Name als gültige Kundenname gespeichert 
    @name.setter 
    def name(self, kundenname: str) -> None:
        if not kundenname.strip(): #entfernt Leerzeichen von beiden Seiten und prüft,  
            raise ValueError("Name darf nicht leer sein") #ob ein Text vorhanden ist
        else:
            self._name = kundenname.strip()

    #durch @staticmethod wird festgelegt welche Kriterien soll eine gültige E-Mail Adresse entsprechen.
    @staticmethod
    def ist_gueltige_email(email: str) -> bool:
        return "@" in email and "." in email.split("@")[-1] #prüft, ob @ in E-Mail vorkommt 
                                                            #und ob es . nach dem @ vorkommt
    @property #Setter-Methode für E-Mail
    def email(self) -> str:
        return self._email

    @email.setter #prüft, ob angegebene E-Mail den Anforderugen von ist_gueltige_email entspricht
    def email(self, adresse: str) -> None:
        if not self.ist_gueltige_email(adresse):
            raise ValueError("Fehler: Diese E-Mail Adresse ist ungültig")
        else:
            self._email = adresse

    def begruessung(self) -> str: #Der Kunde wird begrüßt 
        return f"Hallo {self.name}!"

    def rabattsatz(self, rabatt: float = 0.0) -> float: #Rabattsatz standartmäßig auf 0.0 setzen. 
        return rabatt                                   #später wird er von anderen Kundenklassen überschrieben. 

    def __str__(self) -> str: # __str__ macht die Ausgabe von Kundeninformation für Menschen lesbar
        return f"Kunde {self.kundennummer}: {self.name}"

    def __repr__(self) -> str: #__repr__ ist für Entwickler hilfreich
        return (f"Kunde ({self.kundennummer!r}, {self.name!r})")

    def __eq__(self, other: object) -> bool: # gibt True zurück, wenn Kundennummern gleich sind,
        if not isinstance(other, Kunde):     #ansonsten gibt False zurück 
            return NotImplemented
        else:
            return self.kundennummer == other.kundennummer

 
class Privatkunde(Kunde):
    def __init__(self, kundennummer: int, name: str, email: str, geburtsjahr: int,
                 stammkunde: bool = False) -> None:
        super().__init__(kundennummer, name, email)
        self.geburtsjahr = geburtsjahr
        self.stammkunde = stammkunde


    @property
    def geburtsjahr(self) -> int:
        return self._geburtsjahr
    
    #prüft das angegebene Geburtsjahr. Wenn es kleiner als 1900 oder größer als aktuelles Jahr ist,
    #wird ValueError ausgelöst, ansonsten wird der Wert in der Variable self._geburtsjahr gespeichert. 
    @geburtsjahr.setter 
    def geburtsjahr(self, geburtstag: int) -> None:
        aktuelles_jahr = date.today().year
        if geburtstag < 1900 or geburtstag > aktuelles_jahr:
            raise ValueError
        else:
            self._geburtsjahr = geburtstag

    def alter(self, stichjahr: int | None = None) -> int:
        if stichjahr is None: #stichjahr holt sich das aktuelle Jahr, solange kein Jahr angegeben ist
            stichjahr = date.today().year
        return stichjahr - self._geburtsjahr #hier findet die Berechnung des Alters eines Kundens statt

    def rabattsatz(self) -> float:
        if self.stammkunde:
            return super().rabattsatz() + 0.02 # Stammkunden erhalten 2 % Rabatt. 
        else:                                  # Rabattsatz-Funktion aus Kunde wird hier überschrieben
            return super().rabattsatz()        #Kein Stammkunde -> kein Rabatt

    def __repr__(self):
        return f"Privatkunde ({self.kundennummer!r}, {self.name!r})"