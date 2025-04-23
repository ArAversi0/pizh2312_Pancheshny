# _Наследование_

Задача:

1. Реализация класса Unit (базовый класс):

- Создать класс Unit.
- Реализовать конструктор \_\_init\_\_, принимающий аргумент team (принадлежность к команде).
- Реализовать автоматическую генерацию уникального идентификатора (id) для каждого юнита. Идентификатор должен быть уникальным для всех юнитов в игре (независимо от типа или команды).
- Реализовать метод \_\_str\_\_ для отображения информации о юните (id и команда).

2. Реализация класса Soldier (наследуется от Unit):

- Создать класс Soldier, наследующийся от Unit.
- Реализовать конструктор \_\_init\_\_, вызывающий конструктор базового класса и инициализирующий атрибут following (за кем следует солдат) значением None.
- Реализовать метод follow_hero(hero), принимающий объект типа Hero в качестве аргумента. Метод должен устанавливать атрибут following солдата равным переданному герою и выводить сообщение в консоль о том, что солдат теперь следует за героем. Предусмотреть проверку, что аргумент hero действительно является объектом класса Hero.
- Переопределить метод \_\_str\_\_ для отображения информации о солдате (id, команда и id героя, за которым он следует, или "None", если он никому не следует).

3. Реализация - са Hero (наследуется от Unit):

- Создать класс Hero, наследующийся от Unit.
- Реализовать конструктор \_\_init\_\_, вызывающий конструктор базового класса и инициализирующий атрибут level (уровень героя) значением 1.
- Реализовать метод increase_level(), увеличивающий уровень героя на 1 и выводящий сообщение в консоль о повышении уровня.
- Переопределить метод \_\_str\_\_ для отображения информации о герое (id, команда и уровень).

4. Создание героев:

- В основной части программы создать по одному объекту класса Hero для каждой из двух команд (team 1 и team 2).

5. Генерация солдат:

- В цикле создать заданное количество объектов класса Soldier (например, 20).
- Случайно определять, к какой команде принадлежит каждый солдат (team 1 или team 2).
- Добавлять созданных солдат в соответствующие списки (team1_soldiers и team2_soldiers).

6. Определение команды с большим количеством солдат и повышение уровня героя:

- Определить, в какой команде больше солдат (сравнив длины списков team1_soldiers и team2_soldiers).
- Увеличить уровень героя команды с большим количеством солдат, вызвав метод increase_level() соответствующего объекта Hero.
- В случае равенства количества солдат в обеих командах, вывести сообщение об этом в консоль.

7. Вывод информации о героях:

- Вывести на экран информацию о героях (team1_hero и team2_hero), используя метод \_\_str\_\_.

8. Назначение солдат герою:

- Выбрать двух разных солдат из первой команды (team1_soldiers).
- Вызвать метод follow_hero() для выбранных солдат, передав ему объект team1_hero.
- Вывести на экран информацию о выбранных солдатах после того, как они начали следовать за героем, используя метод \_\_str\_\_.

Решение (Код программы целиком):

```python

import random

class Unit: # Базовый класс для всех юнитов
    next_id = 1 # Статическая переменная для генерации уникальных ID

    def __init__(self, team):
        self.id = Unit.next_id # Присваиваем юниту уникальный ID
        Unit.next_id += 1
        self.team = team # Команда, к которой принадлежит юнит

    def __str__(self):
        return f"Unit ID: {self.id}, Team: {self.team}" # Строковое представление юнита

class Soldier(Unit):
    def __init__(self, team):
        super().__init__(team)  # Вызываем конструктор базового класса
        self.following = None #  Солдат изначально никому не следует

    def follow_hero(self, hero):
        if isinstance(hero, Hero): # Проверяем, что hero является объектом класса Hero
            self.following = hero # Устанавливаем, за каким героем следует солдат
            print(f"Soldier {self.id} of Team {self.team} is now following Hero {hero.id} of Team {hero.team}")
        else:
            print("Error: Can only follow a Hero object.") # Ошибка: следовать можно только за объектом класса Hero.

    def __str__(self): # Переопределяем строковое представление
        if self.following: # Если солдат за кем-то следует
            return f"Soldier ID: {self.id}, Team: {self.team}, Following: Hero {self.following.id}"
        else:
            return f"Soldier ID: {self.id}, Team: {self.team}, Following: None" # Если солдат никому не следует

class Hero(Unit):
    def __init__(self, team):
        super().__init__(team)
        self.level = 1 # Начальный уровень героя

    def increase_level(self):
        self.level += 1 # Увеличиваем уровень героя
        print(f"Hero {self.id} of Team {self.team} increased level to {self.level}!")

    def __str__(self):
         return f"Hero ID: {self.id}, Team: {self.team}, Level: {self.level}"  # Включаем уровень в строковое представление

# Main program
team1_hero = Hero(1) # Создаем героя для первой команды
team2_hero = Hero(2) # Создаем героя для второй команды

team1_soldiers = [] # Список солдат первой команды
team2_soldiers = [] # Список солдат второй команды

num_soldiers = 20 # Общее количество солдат для генерации

for _ in range(num_soldiers):
    team = random.choice([1, 2]) # Случайно определяем команду для солдата
    soldier = Soldier(team) # Создаем солдата
    if team == 1:
        team1_soldiers.append(soldier) # Добавляем солдата в соответствующий список
    else:
        team2_soldiers.append(soldier)

print(f"Number of soldiers in Team 1: {len(team1_soldiers)}") # Выводим количество солдат в каждой команде
print(f"Number of soldiers in Team 2: {len(team2_soldiers)}")

if len(team1_soldiers) > len(team2_soldiers):
    team1_hero.increase_level() # Увеличиваем уровень героя команды с большим количеством солдат
elif len(team2_soldiers) > len(team1_soldiers):
    team2_hero.increase_level()
else:
    print("Teams have equal number of soldiers. No level increase.") # Команды имеют одинаковое количество солдат. Уровень не повышается.

print(team1_hero) # Выводим информацию о героях
print(team2_hero)

# Заставляем двух солдат следовать за первым героем
if team1_soldiers: # Проверяем, что в первой команде есть солдаты
    soldier1 = random.choice(team1_soldiers)  # Случайно выбираем солдата из первой команды
    soldier1.follow_hero(team1_hero)  # Отправляем солдата следовать за героем первой команды
    print(soldier1)

    # Выбираем другого уникального солдата
    available_soldiers = [s for s in team1_soldiers if s != soldier1]
    if available_soldiers:
        soldier2 = random.choice(available_soldiers)
        soldier2.follow_hero(team1_hero)
        print(soldier2)

```

---
