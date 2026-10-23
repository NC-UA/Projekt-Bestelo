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
 