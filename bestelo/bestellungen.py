
from bestelo.kunden import Kunde
from bestelo.bestellposition import Bestellposition

class Bestellung:
      def __init__(self, nummer: int , kunde: Kunde) ->None:
            self.nummer= nummer
            self.kunde= kunde
            self.status= 'offen'
            self.position= []

def position_hinzufügen(self, position:Bestellposition) ->None:
      self.position.append(position)

def gesamtSumme_netto(self) -> float:
      summe=0

      for position in self.position:
            summe+=position.netto()

        return summe

def gesamtSumme_brutto(self) -> float:
      summe=0

      for position in self.position:
            summe+=position.brutto()

        return summe

def gesamtSumme_mwst(self) -> float:
      summe=0

      for position in self.position:
            summe+=position.mwst()

        return summe

def bestelnummer(self) -> str:
      if self.nummer <10:
            return "000"+str(self.nummer)
      elif self.nummer <100:
            return "00"+str(self.nummer)
      elif self.nummer <1000:
                  return "0"+str(self.nummer)
      return str(self.nummer)