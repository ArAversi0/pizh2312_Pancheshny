import pygame
import random

# Инициализация Pygame — необходимо для работы всех модулей библиотеки.
pygame.init()

# Настройки окна и игрового поля
WIDTH, HEIGHT = 640, 480             # Размеры игрового окна
CELL_SIZE = 20                       # Размер одной ячейки (элемента) сетки
FPS = 20                             # Количество кадров в секунду (скорость игры)

# Цветовые константы (RGB)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Векторы направлений движения змейки
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Все возможные координаты ячеек на игровом поле
ALL_CELLS = {
    (x * CELL_SIZE, y * CELL_SIZE) for x in range(WIDTH // CELL_SIZE) for y in range(HEIGHT // CELL_SIZE)
}

# Базовый класс для игровых объектов (наследование: Apple, Snake)
class GameObject:
    def __init__(self, position, body_color):
        """
        Инициализация объекта на игровом поле.
        :param position: координаты объекта
        :param body_color: цвет отрисовки
        """
        self.position = position
        self.body_color = body_color

    def draw(self, screen):
        """
        Пустая функция отрисовки (переопределяется в наследниках).
        """
        pass

# Класс Apple (яблоко), которое должна собирать змейка
class Apple(GameObject):
    def __init__(self, snake_positions):
        """
        Создание яблока и установка его в случайную незанятую ячейку.
        :param snake_positions: список ячеек, занятых телом змейки
        """
        super().__init__((0, 0), RED)
        self.randomize_position(snake_positions)

    def randomize_position(self, snake_positions):
        """
        Генерирует случайную позицию для яблока, исключая позиции, занятые змейкой.
        """
        available_cells = ALL_CELLS - set(snake_positions)
        if not available_cells:
            raise ValueError("No available cells left on the board!")
        self.position = random.choice(tuple(available_cells))

    def draw(self, screen):
        """
        Отрисовка яблока на экране.
        """
        pygame.draw.rect(screen, self.body_color, (*self.position, CELL_SIZE, CELL_SIZE))

# Класс Snake (змейка), управляемая игроком
class Snake(GameObject):
    def __init__(self):
        """
        Инициализация змейки с начальной длиной 1 в центре поля и направлением вправо.
        """
        super().__init__([(WIDTH // 2, HEIGHT // 2)], GREEN)
        self.length = 1
        self.direction = RIGHT
        self.next_direction = None

    def update_direction(self, new_direction):
        """
        Обновление направления движения, если оно не противоположно текущему.
        """
        if (self.direction[0] + new_direction[0], self.direction[1] + new_direction[1]) != (0, 0):
            self.next_direction = new_direction

    def move(self):
        """
        Перемещает змейку на одну ячейку в текущем направлении.
        Увеличивает длину при поедании яблока, иначе удаляет хвост.
        """
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

        head_x, head_y = self.position[0]
        new_head = (
            (head_x + self.direction[0] * CELL_SIZE) % WIDTH,
            (head_y + self.direction[1] * CELL_SIZE) % HEIGHT
        )
        self.position.insert(0, new_head)

        if len(self.position) > self.length:
            self.position.pop()

    def draw(self, screen):
        """
        Отрисовка каждой ячейки тела змейки на экране.
        """
        for pos in self.position:
            pygame.draw.rect(screen, self.body_color, (*pos, CELL_SIZE, CELL_SIZE))

    def get_head_position(self):
        """
        Возвращает координаты головы змейки.
        """
        return self.position[0]

    def reset(self):
        """
        Сброс параметров змейки после столкновения с самой собой.
        """
        self.position = [(WIDTH // 2, HEIGHT // 2)]
        self.length = 1
        self.direction = RIGHT
        self.next_direction = None

# Обработка всех событий клавиатуры и выхода из игры
def handle_keys(snake):
    """
    Обрабатывает все события Pygame, включая выход из игры (крестик или Esc),
    изменение направления змейки, изменение скорости игры.
    """
    global FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            elif event.key == pygame.K_UP:
                snake.update_direction(UP)
            elif event.key == pygame.K_DOWN:
                snake.update_direction(DOWN)
            elif event.key == pygame.K_LEFT:
                snake.update_direction(LEFT)
            elif event.key == pygame.K_RIGHT:
                snake.update_direction(RIGHT)
            elif event.key == pygame.K_q:
                FPS = max(5, FPS - 5)  # Уменьшить FPS, но не меньше 5
            elif event.key == pygame.K_w:
                FPS += 5               # Увеличить FPS

# Основной игровой цикл
def main():
    """
    Главная функция игры:
    - инициализирует экран и объекты;
    - запускает игровой цикл;
    - обрабатывает движение, столкновения и отрисовку;
    - отслеживает рекордную длину змейки и обновляет заголовок окна.
    """
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    snake = Snake()
    apple = Apple(snake.position)
    max_length = snake.length  # Рекордная длина змейки в текущей сессии

    running = True
    while running:
        handle_keys(snake)
        snake.move()

        # Если змейка съела яблоко
        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position(snake.position)
            if snake.length > max_length:
                max_length = snake.length
                pygame.display.set_caption(f"Змейка | Рекорд: {max_length}")

        # Если змейка столкнулась с собой — сброс
        if len(snake.position) != len(set(snake.position)):
            snake.reset()

        # Отрисовка всех объектов на экране
        screen.fill(BLACK)
        snake.draw(screen)
        apple.draw(screen)
        pygame.display.update()

        # Ограничение частоты кадров
        clock.tick(FPS)

# Запуск игры при запуске файла
if __name__ == "__main__":
    main()