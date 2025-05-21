import random

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, opponent):
        damage = 20
        opponent.health -= damage
        print(f"{self.name} attacked {opponent.name}!")
        print(f"{opponent.name}'s health: {opponent.health}")

    def is_alive(self):
        return self.health > 0

# Create two warriors
warrior_1 = Warrior("Unit_1")
warrior_2 = Warrior("Unit_2")

# Game loop
while warrior_1.is_alive() and warrior_2.is_alive():
    # Determine who attacks
    attacker, defender = random.sample([warrior_1, warrior_2], 2)

    # Attack
    attacker.attack(defender)

# Determine the winner
if warrior_1.is_alive():
    print(f"{warrior_1.name} wins!")
else:
    print(f"{warrior_2.name} wins!")