
from bestelo.produkte import Produkt

class Bestellposition:
    def __init__ (self, produkt: Produkt, menge: int=1) -> None:
     self._produkt = produkt
     self.menge = menge

@property
def produkt(self) -> Produkt:
     return self._produkt

@property
def menge(self) -> int:
     return self._menge

@menge.setter 
def menge(self, wert:int) -> None:
     if not wert >= 1:
        raise ValueError("Menge muss 1 sein")
     self._menge = wert

def netto(self) -> float:
    return self.produkt.nettopreis*self.menge

def mwst(self) -> float:
    return self.netto()*self.produkt.mwst_satz

def brutto(self) -> float:
    return self.netto()+self.mwst()

def __str__ (self) -> str:
    return(
        f"{self.menge}x {self.produkt.beschreibung} "
        f"für {self.produkt.nettopreis:.2f}€"
        f"= {self.netto():.2f}€"
    )

    