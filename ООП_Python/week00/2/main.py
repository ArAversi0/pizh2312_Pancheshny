class Person:
    def __init__(self, name, surname, qualification=1):
        self.name = name
        self.surname = surname
        self.qualification = qualification

    def __str__(self):
        return f"Имя: {self.name}, Фамилия: {self.surname}, Квалификация: {self.qualification}"

    def __del__(self):
        print(f"До свидания, мистер {self.name} {self.surname}...")


# Создание объектов и просмотр информации
person1 = Person("Александр", "Иванов", 3)
person2 = Person("Андрей", "Петров", 2)
person3 = Person("Алексей", "Сидоров")  # Квалификация по умолчанию = 1

print(person1)
print(person2)
print(person3)

# Определение и увольнение "самого слабого звена"
weakest_person = min([person1, person2, person3], key=lambda person: person.qualification)
print(f"\nУволен: {weakest_person.name} {weakest_person.surname}")
del weakest_person


# Ожидание нажатия Enter
input("\nНажмите Enter для завершения...")