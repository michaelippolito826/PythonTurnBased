from moveset import champs
from typing_file import typing_moves
import random
import py_cui

class Player:
    def __init__(self, name):
        self.name = name
        self.champ = None

    # Choosing what champ player wants
    def choose_champ(self):
        choice = input("Champ?\n").lower()
        if choice == "kaisa":
            choice = "kai'sa"
        self.champ = choice


class Champ:
    def __init__(self, name, type, health, mana, q, w, e, r):
        self.name = name
        self.type = type
        self.health = health
        self.mana = mana
        self.q = q
        self.w = w
        self.e = e
        self.r = r


class Match:
    def __init__(self):
        self.game_over = False
        self.turn = 0

    def attack(self, attacker, defender, ai: bool):
        # If attacker is player
        if ai is False:
            move = input("Which move? (Q, W, E, R)\n").upper()
        # If attacker is AI
        elif ai is True:
            move_int = random.randint(0, 3)
            # q = 0, w = 1, e = 2, r = 3
            if move_int == 0:
                move = "Q"
            if move_int == 1:
                move = "W"
            if move_int == 2:
                move = "E"
            if move_int == 3:
                move = "R"

        # Find move type, move damage, and mana cost
        move_type = champs[attacker.name][move][0]
        attacker_damage = champs[attacker.name][move][1]
        mana_cost = champs[attacker.name][move][2]

        # Calculate attacker mana
        attacker_mana = attacker.mana
        if attacker.mana <= 0:
            print(f"No Mana! {attacker.name.capitalize()} does nothing!")
            attacker_damage = 0
        else:
            attacker_mana -= mana_cost
            if attacker_mana < 0:
                attacker_mana = 0
    
        # Typing multiplier
        defender_type = champs[defender.name]["Type"]
        type_multiplier = typing_moves[move_type][defender_type]
        attacker_damage *= type_multiplier

        # Calculate defender health
        defender_health = defender.health
        defender_health -= attacker_damage

        if defender_health <= 0:
            defender_health = 0

        # Adding defender health and attacker mana back to object
        defender.health = defender_health
        attacker.mana = attacker_mana

    def next_turn(self):
        self.turn += 1
        print(f"\n{self.turn}\n")

    def check_win(self, ally, enemy):
        # If ally dies
        if ally.health < 1 and enemy.health > 0:
            self.game_over = True
            print("You lost!")

        # If enemy dies
        elif ally.health > 0 and enemy.health < 1:
            self.game_over = True
            print("You Win!")

        # If tie
        elif ((ally.health < 1 and enemy.health < 1) or
                (ally.mana < 1 and enemy.mana < 1)):
            self.game_over = True
            print("Draw!")

    def end_turn(self, ally, enemy):
        print(f"a: {ally.health}, m: {ally.mana} and e: {enemy.health}")


class Game:
    def __init__(self):
        self.quit = False

    def name(self):
        return input("What is your name?\n")

    def intro(self):
        print("Welcome to the world of Leaguiemon!\n"
              "It is time to choose your starter and fight your rival!\n")

    def starter(self):
        starter = input("Which starter do you want to choice?\n"
                        "Kai'sa (Void), Lee Sin (Fighting), "
                        "or Aatrox (Dark)\n")
        if starter == "kaisa":
            starter = "kai'sa"
        return starter


# Init game
in_game = Game()
name = in_game.name()
in_game.intro()
in_game.starter()

current_match = Match()
player = Player(name)

# Init enemy champ
enemy = Champ(champs["kai'sa"]["Name"],
              champs["kai'sa"]["Type"],
              champs["kai'sa"]["Health"],
              champs["kai'sa"]["Mana"],
              champs["kai'sa"]["Q"],
              champs["kai'sa"]["W"],
              champs["kai'sa"]["E"],
              champs["kai'sa"]["R"])

# Init player's champ
player.choose_champ()

ally = Champ(champs[player.champ]["Name"],
             champs[player.champ]["Type"],
             champs[player.champ]["Health"],
             champs[player.champ]["Mana"],
             champs[player.champ]["Q"],
             champs[player.champ]["W"],
             champs[player.champ]["E"],
             champs[player.champ]["R"])

# Game Loop
while not current_match.game_over:
    # Player Attack
    current_match.attack(ally, enemy, False)
    # Enemy Attack
    current_match.attack(enemy, ally, True)
    # Display Health and Mana
    current_match.end_turn(ally, enemy)
    # Win Con Met breaks loop
    current_match.check_win(ally, enemy)
