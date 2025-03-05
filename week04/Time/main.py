# Программирование на языке высокого уровня (Python).
# Задание №4.3.4. Вариант 4
#
# Выполнил: Панчешный Александр Алексеевич
# Группа: ПИЖ-б-о-23-1-2
# E-mail: pancheshny2020@yandex.ru

# Импортирование всех классов
from time_classes import Time, MilitaryTime, FormattedTime
from stopwatch import Stopwatch

# Создание объектов Time
time1 = Time(10, 30, 45)
time2 = Time.from_string("12:15:30")

# Вывод времени
print(f"Time 1: {time1}")  # Вывод: Time 1: 10:30:45
print(f"Time 2: {time2}")  # Вывод: Time 2: 12:15:30

# Арифметические операции
time3 = time1 + time2
time4 = time2 - time1
print(f"Time 1 + Time 2: {time3}")  # Вывод: Time 1 + Time 2: 22:46:15
print(f"Time 2 - Time 1: {time4}")  # Вывод: Time 2 - Time 1: 01:44:45

# Преобразование времени
print(f"Time 1 в секундах: {time1.to_seconds()}")  # Вывод: Time 1 в секундах: 37845
print(f"Time 2 в минутах: {time2.to_minutes()}")  # Вывод: Time 2 в минутах: 735
print(f"Time 3 в часах: {time3.to_hours()}")  # Вывод: Time 3 в часах: 22.770833333333332

# Сохранение и загрузка времени
time1.save("time1.json")
time5 = Time()
time5.load("time1.json")
print(f"Загруженное время: {time5}")  # Вывод: Загруженное время: 10:30:45

# Военное время
military_time = MilitaryTime(15, 45, 0)
print(f"Военное время: {military_time}")  # Вывод: Военное время: 1545

# Форматированное время
formatted_time = FormattedTime(15, 45, 30)
print(f"Форматированное время: {formatted_time}")  # Вывод: Форматированное время: 03:45:30 PM

# Секундомер
stopwatch = Stopwatch()
start_time = Time(10, 0, 0)
stop_time = Time(10, 0, 10)
stopwatch.start(start_time)
stopwatch.stop(stop_time)
elapsed_time = stopwatch.elapsed_time()
print(f"Прошедшее время секундомера: {elapsed_time}")  # Вывод: Прошедшее время секундомера: 00:00:10