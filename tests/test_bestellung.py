
from bestelo.kunden import Kunde
from bestelo.bestellposition import Bestellposition

class TestKunde:
    pass

class TestProdukt:
    nettopreis=10.0
    mwst_satz=0.10

def test_bestellnummer():
 bestellung=Bestellung(nummer=2, kunde=TestKunde())
 ergebnis=bestellung.bestelnummer()
 if ergebnis != "0002":
    raise AssertionError("Die Bestellnummer sollte 0002 sein!")

def test_gesamtsumme_netto():
   bestellung=Bestellung(nummer=1, kunde=TestKunde())
   produkt=TestProdukt()

   position1=Bestellposition(produkt,menge=1)
   position2=Bestellposition(produkt,menge=1)

   bestellung.position_hinzufügen(position1)
   bestellung.position_hinzufügen(position2)

   ergebnis=bestellung.gesamtSumme_netto()

   if ergebnis != 20.0:
      raise AssertionError("Die Bestellsumme sollte bei 20.0 liegen!")