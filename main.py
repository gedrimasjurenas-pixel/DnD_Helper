from factory import CharacterFactory
from storage import Storage


def edit_basic_info(character):
    print("\n--- Edit Character Info ---")
    character._name = input(f"New name ({character.name}): ") or character.name
    character._class = input(f"New class ({character._class}): ") or character._class
    character._history = input(f"New history ({character._history}): ") or character._history
    print("Character info updated!")


def edit_stats(character):
    print("\n--- Edit Stats ---")
    for stat in ["STR", "DEX", "CON", "INT", "WIS", "CHA"]:
        current = getattr(character.stats, stat)
        new_val = input(f"{stat} ({current}): ")
        if new_val.isdigit():
            character.stats.update(stat, int(new_val))
    print("Stats updated!")


def edit_inventory(character):
    print("\n--- Inventory ---")
    print("Current items:", character.inventory.items)

    print("1. Add item")
    print("2. Remove item")
    choice = input("Choose: ")

    if choice == "1":
        item = input("Item to add: ")
        character.inventory.add_item(item)
    elif choice == "2":
        item = input("Item to remove: ")
        character.inventory.remove_item(item)

    print("Inventory updated!")


def edit_abilities(character):
    print("\n--- Abilities ---")
    print("Current abilities:")
    for a in character.abilities:
        print(f"- {a.name} ({a.power})")

    print("1. Add ability")
    print("2. Remove ability")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Ability name: ")
        desc = input("Description: ")
        power = int(input("Power: "))
        from ability import Ability
        character.add_ability(Ability(name, desc, power))

    elif choice == "2":
        name = input("Ability name to remove: ")
        character.abilities = [a for a in character.abilities if a.name != name]

    print("Abilities updated!")


def edit_health(character):
    print("\n--- Health ---")
    print(f"Current HP: {character.health}")

    print("1. Damage")
    print("2. Heal")
    choice = input("Choose: ")

    amount = int(input("Amount: "))

    if choice == "1":
        character.take_damage(amount)
    else:
        character.heal(amount)

    print(f"New HP: {character.health}")


def edit_character(character):
    while True:
        print(f"\nEditing {character.name}")
        print("1. Edit basic info")
        print("2. Edit stats")
        print("3. Edit inventory")
        print("4. Edit abilities")
        print("5. Edit health")
        print("6. Back")

        choice = input("Choose: ")

        if choice == "1":
            edit_basic_info(character)
        elif choice == "2":
            edit_stats(character)
        elif choice == "3":
            edit_inventory(character)
        elif choice == "4":
            edit_abilities(character)
        elif choice == "5":
            edit_health(character)
        elif choice == "6":
            break


def main():
    print("=== DND Helper ===")

    while True:
        print("\n1. Create character")
        print("2. View characters")
        print("3. Edit character")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            char_class = input("Class: ")
            history = input("History: ")

            character = CharacterFactory.create_character(name, char_class, history)
            Storage.save_character(character)
            print("Character saved!")

        elif choice == "2":
            chars = Storage.load_characters()
            for c in chars:
                print(c)

        elif choice == "3":
            chars = Storage.load_characters()
            if not chars:
                print("No characters found.")
                continue

            print("\nSelect character:")
            for i, c in enumerate(chars):
                print(f"{i+1}. {c.name} ({c._class})")

            index = int(input("Choose number: ")) - 1
            character = chars[index]

            edit_character(character)

            Storage.save_all(chars)

        elif choice == "4":
            break


if __name__ == "__main__":
    main()
