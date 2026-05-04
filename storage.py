import csv
from factory import CharacterFactory


class Storage:
    FILE = "data/characters.csv"

    @staticmethod
    def save_character(character):
        with open(Storage.FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([character.name, character._class, character._history])

    @staticmethod
    def save_all(characters):
        with open(Storage.FILE, "w", newline="") as f:
            writer = csv.writer(f)
            for c in characters:
                writer.writerow([c.name, c._class, c._history])

    @staticmethod
    def load_characters():
        characters = []
        try:
            with open(Storage.FILE, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    # Skip empty or broken rows
                    if len(row) != 3:
                        continue

                    name, char_class, history = row
                    characters.append(
                        CharacterFactory.create_character(name, char_class, history)
                    )
        except FileNotFoundError:
            pass

        return characters
