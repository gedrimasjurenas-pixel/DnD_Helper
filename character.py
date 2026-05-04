from stats import Stats
from inventory import Inventory
from ability import Ability


class Character:
    def __init__(self, name, char_class, history):
        self._name = name
        self._class = char_class
        self._history = history

        # Composition
        self.stats = Stats()
        self.inventory = Inventory()
        self.abilities = []

        self.health = 10 + self.stats.con

    # Encapsulation
    @property
    def name(self):
        return self._name

    def add_ability(self, ability: Ability):
        self.abilities.append(ability)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += amount

    def __str__(self):
        return f"{self.name} the {self._class} (HP: {self.health})"
