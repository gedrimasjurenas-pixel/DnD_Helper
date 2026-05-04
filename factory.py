from character import Character


class CharacterFactory:
    @staticmethod
    def create_character(name, char_class, history):
        return Character(name, char_class, history)
