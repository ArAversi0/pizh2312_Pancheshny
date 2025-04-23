# _Создание классов и объектов_

Задача:

- Создать класс "Воин" ("Warrior")
- Создать 2 экземпляра этого класса (2 юнита)
- Каждому юниту установить начальное здоровье
- Юниты должны бить друг друга в случайном порядке (причём атакующий не теряет здоровье)
- Атакованный юнит должен терять фиксированное здоровье
- Каждый удар должен сопровождаться выводом сообщения: кто атаковал, сколько здоровья осталость у противника
- Здоровье = 0 или неиже => программа завершается сообщением о победителе

Решение (Код программы целиком):

```python

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

```

---

## _Разберём участки кода подробнее_

1. `import random` Импортирует модуль random для генерации случайных чисел.
2.

```python
def __init__(self, name): # определили конструктор класса
    self.name = name # Инициализация атрибута name именем воина.
    self.health = 100 # Инициализация атрибута health значением 100 (хп воина).
```

3.

```python

def attack(self, opponent): # Определяет метод, моделирующий атаку на другого воина.
        damage = 20
        opponent.health -= damage # Уменьшение здоровья противника на величину урона.
        print(f"{self.name} attacked {opponent.name}!")
        print(f"{opponent.name}'s health: {opponent.health}") # Вывод сообщений о том, кто кого атаковал и об остатке здоровья противника.
```

4.

```python

def is_alive(self): # Определяет метод, проверяющий, жив ли воин.
    return self.health > 0 # Возвращает True, если здоровье больше 0, и False в противном случае.
```

5.

```python
# Создание 2-х необходимых экземпляра класса
warrior1 = Warrior("Unit 1")
warrior2 = Warrior("Unit 2")
```

6.

```python
 # Цикл продолжается, пока оба воина живы.
while warrior1.is_alive() and warrior2.is_alive():
    attacker, defender = random.sample([warrior1, warrior2], 2) # Случайным образом выбирает двух разных воинов из списка.
    attacker.attack(defender) # Вызывает метод attack атакующего воина, чтобы атаковать защищающегося.
```

7.

```python
# Проверяет, жив ли warrior1 после завершения цикла:
if warrior1.is_alive():
    print(f"{warrior1.name} wins!") # Если жив, выводит сообщение о победе warrior1.
else:
    print(f"{warrior2.name} wins!") # Иначе выводит сообщение о победе warrior2.
```

---
