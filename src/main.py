import os
import time
import random

version = 'alpha'
characters = []
sep = '------------------------------------------'
enemy_classes = {
    1: 'Goblin'
}
player_classes = {
    1: 'Warrior',
    2: 'Rogue',
    3: 'Mage'
}
menues = {
    1: [
        f'Welcome to Text RPythonG V. {version}',
        '',
        'Menu:',
        '[1] New game',
        '[2] Create character',
        '[3] Exit'
    ], 2: [
        'Welcome to character creation'
    ], 3: [
        'Choose a class:',
        '[1] Warrior',
        '[2] Rogue',
        '[3] Mage'
    ]
}
default_ui_speed = .05
current_ui_speed = .05
current_ui = 1


class Entity:
    def __init__(self, entity_name):
        self.entity_name = entity_name
        self.max_hp = 1
        self.current_hp = 1
        self.strength = 1


class Player(Entity):
    def __init__(self, entity_name, player_class):
        super(Player, self).__init__(entity_name)
        self.player_class = player_class
        self.resource = 'null'
        self.resource_amount = 0
        self.gold = 0
        self.exp = 0

    def resolve_class_attributes(self):
        # Warrior
        if self.player_class == 1:
            self.max_hp = random.randint(70, 90)
            self.resource = 'Rage'
            self.resource_amount = 0
            self.gold = random.randint(1, 10)
            self.strength = random.randint(5, 10)
        self.current_hp = self.max_hp


class Enemy(Entity):
    def __init__(self, entity_name, enemy_class):
        super(Enemy, self).__init__(entity_name)
        self.enemy_class = enemy_class

    def resolve_class_attributes(self):
        if self.enemy_class == 1:
            self.max_hp = random.randint(1, 10)
        self.current_hp = self.max_hp


def random_enemy():
    enemy = Enemy('Gob', random.randint(1, 1))
    enemy.resolve_class_attributes()
    return enemy


def main():
    global current_ui_speed
    global current_ui

    random.seed()

    option = None
    while option != 1:
        print_menu()

        if characters:
            print_ui(sep)
            print_ui('Characters:')
            for character in characters:
                print_ui(f'Name: {character.entity_name} | Class: {player_classes[character_class]} | XP: {character.exp} | Gold: {character.gold}')
                print_ui(f'HP: {character.current_hp}/{character.max_hp} | {character.resource}: {character.resource_amount}')
            print_ui(sep)

        option = get_input('Please input an option:')
        if option == '1':
            current_character = None
            if not characters:
                print_ui('You have no characters to play with!')
                current_ui_speed = 0
            else:
                combat_end = False
                goblin = random_enemy()
                while not combat_end:

                    if goblin.current_hp == 0 or current_character.hp == 0:
                        combat_end = True
        elif option == '2':
            new_character = None
            character_name = None
            character_class = None
            while new_character is None:
                refresh_ui()
                if current_ui is not 2:
                    current_ui = 2
                    print_menu()

                if character_name:
                    print_ui(f'Name: {character_name}')
                else:
                    character_name = get_input('Name:')

                current_ui = 3
                print_menu()
                try:
                    character_class = int(get_input('Class:'))
                except ValueError:
                    input('Please enter a valid option. Press Enter key to continue')

                if character_class is not None and character_name is not None:
                    new_character = Player(character_name, character_class)
                    new_character.resolve_class_attributes()
                    characters.append(new_character)
                    current_ui = 1
                    refresh_ui()
        elif option == '3':
            exit()
        else:
            print('Incorrect option.')

    interactive = False
    while interactive:
        refresh_ui()


def print_ui(ui):
    for char in ui:
        print(char, end='', flush=True)
        time.sleep(current_ui_speed)
    print()


def print_menu():
    for line in menues[current_ui]:
        for char in line:
            print(char, end='', flush=True)
            time.sleep(current_ui_speed)
        print()


def get_input(input_line):
    for char in input_line:
        print(char, end='', flush=True)
        time.sleep(current_ui_speed)
    print(' ', end='')
    return input()


def refresh_ui():
    global current_ui_speed

    os.system('cls')
    current_ui_speed = default_ui_speed


os.system('cls')
main()
