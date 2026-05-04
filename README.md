# DnD_Helper 
1. Įvadas

Šio kursinio darbo tikslas – sukurti Python programą, kuri praktiškai pademonstruoja objektinio programavimo (OOP) principus, dizaino šablonų taikymą, duomenų saugojimą faile ir vienetinius testus.
Pasirinkta tema – Dungeons and Dragons (DND) Helper, tai yra įrankis, skirtas kurti ir valdyti DND veikėjus.

Kas yra ši programa?
Programa – tai konsolinė DND veikėjų valdymo sistema. Ji leidžia:
•	kurti naujus veikėjus
•	redaguoti veikėjų atributus
•	keisti statistiką (STR, DEX, CON, INT, WIS, CHA)
•	tvarkyti inventorių
•	pridėti gebėjimus
•	išsaugoti veikėjus faile
•	įkelti veikėjus iš failo

Kaip paleisti programą?
1.	Įsidiegti Python 3.10+
2.	Atsisiųsti projektą iš GitHub
3.	Paleisti komandą:
python main.py

Kaip naudotis programa?
Paleidus programą pateikiamas meniu:
1.	Sukurti naują veikėją
2.	Peržiūrėti išsaugotus veikėjus
3.	Redaguoti išsaugotus veikėjus
4.	Išeiti
Visi veikėjai automatiškai išsaugomi faile data/characters.csv.

2. Analizė
Šiame skyriuje paaiškinama, kaip programa įgyvendina funkcinius reikalavimus ir OOP principus.
 2.1 Funkcinių reikalavimų įgyvendinimas
Veikėjo kūrimas
Veikėjai kuriami naudojant Factory Method dizaino šabloną:
character = CharacterFactory.create_character(name, char_class, history)
Statistikos redagavimas
Statistika saugoma atskiroje klasėje:
stats.update("STR", 15)
Inventoriaus valdymas
Inventorius realizuotas kompozicijos principu:
self.inventory = Inventory()
self.inventory.add_item("Sword")
Gebėjimai
Gebėjimai yra atskiri objektai, pridedami prie veikėjo:
self.abilities.append(Ability("Fireball", "Magic attack", 30))
Failų skaitymas ir rašymas
Veikėjai išsaugomi CSV faile:
writer.writerow([character.name, character._class, character._history])
Veikėjai įkeliami naudojant tą patį fabriką:
characters.append(CharacterFactory.create_character(name, char_class, history))

 2.2 OOP principai
 1. Inkapsuliacija
Atributai apsaugoti naudojant @property:
@property
def name(self):
    return self._name
 2. Paveldėjimas
Nors šiame projekte nėra sudėtingos paveldėjimo hierarchijos, klasės sukurtos taip, kad būtų galima lengvai plėsti:
•	Stats galėtų būti paveldima į RaceStats, ClassStats
•	Character galėtų turėti potipius: Wizard, Fighter, Rogue
•	 3. Polimorfizmas
Factory Method leidžia grąžinti skirtingų tipų veikėjus:
def create_character(...):
    return Character(...)
Ateityje metodas galėtų grąžinti skirtingas veikėjų klases.
 4. Abstrakcija
Sudėtinga logika paslėpta už paprastų metodų:
•	Storage.save_character() paslepia CSV logiką
•	CharacterFactory.create_character() paslepia objektų kūrimą
•	Stats.update() paslepia atributų tikrinimą


 2.3 Kompozicija ir agregacija
Kompozicija
Veikėjas turi statistiką ir inventorių:
self.stats = Stats()
self.inventory = Inventory()
Šie objektai neegzistuoja be veikėjo.
Agregacija
Gebėjimai egzistuoja atskirai, bet gali būti priskirti veikėjui:
self.abilities.append(ability)
 
 2.4 Dizaino šablonas – Factory Method
Programoje naudojamas Factory Method šablonas veikėjų kūrimui.
Kodėl pasirinktas šis šablonas?
•	leidžia centralizuoti veikėjų kūrimą
•	palengvina programos plėtrą
•	atskiria kūrimo logiką nuo pagrindinio kodo
Pavyzdys:
class CharacterFactory:
    @staticmethod
    def create_character(name, char_class, history):
        return Character(name, char_class, history)

2.5 Darbas su failais
Programa naudoja CSV formatą.
Išsaugojimas:
with open(Storage.FILE, "a", newline="") as f:
    writer = csv.writer(f)
Įkėlimas:
reader = csv.reader(f)
 
 2.6 Testavimas
Vienetiniai testai tikrina:
•	veikėjo sveikatos logiką
•	statistikos atnaujinimą
•	inventoriaus veikimą
Pavyzdys:
def test_damage(self):
    c = Character("Test", "Mage", "None")
    c.take_damage(5)
    self.assertEqual(c.health, 5)

3. Rezultatai
•	Factory Method dizaino šablonas padidina lankstumą ir plėtrumą.
•	CSV failų naudojimas leidžia išsaugoti veikėjų duomenis.
•	Vienetiniai testai užtikrina pagrindinių funkcijų stabilumą.
•	Projekto struktūra aiški, modulinė ir atitinka PEP8 stilių.
4. Išvados
Šiame kursiniame darbe sukurta DND Helper programa sėkmingai demonstruoja objektinio programavimo principus ir gerąsias programų architektūros praktikas.
Programa yra funkcionali, lengvai plečiama ir tinkama tolesniam vystymui.
Galimos ateities plėtros kryptys:
•	grafinė vartotojo sąsaja (GUI)
•	JSON ar duomenų bazės palaikymas
•	veikėjų klasių hierarchija (Wizard, Fighter ir kt.)
•	kovų simuliatorius
•	burtų sistema
