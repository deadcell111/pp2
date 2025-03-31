import pygame
import random
import sys

pygame.init()

# Настройки экрана и клеток
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
COLS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)
BLUE = (0, 100, 255)
ORANGE = (255, 165, 0)

# Инициализация экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake_Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# Начальные значения
snake = [(5, 5), (4, 5), (3, 5)]
direction = (1, 0)
score = 0
level = 1
speed = 10

# Стены по краям
walls = []
for x in range(COLS):
    walls.append((x, 0))
    walls.append((x, ROWS - 1))
for y in range(ROWS):
    walls.append((0, y))
    walls.append((COLS - 1, y))

# Типы еды: вес, цвет
FOOD_TYPES = [
    {"value": 1, "color": RED},
    {"value": 2, "color": ORANGE},
    {"value": 3, "color": YELLOW}
]

# Получить новую еду со случайным весом и таймером
def get_food():
    while True:
        x = random.randint(1, COLS - 2)
        y = random.randint(1, ROWS - 2)
        if (x, y) not in snake and (x, y) not in walls:
            food_type = random.choice(FOOD_TYPES)
            return {
                "pos": (x, y),
                "value": food_type["value"],
                "color": food_type["color"],
                "timer": 300  # сколько тиков до исчезновения (примерно 30 сек)
            }

# Отрисовка игры
def draw_game():
    screen.fill(BLACK)

    # Стены
    for wall in walls:
        pygame.draw.rect(screen, GRAY, (wall[0]*CELL_SIZE, wall[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Змейка
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Еда
    if food:
        pygame.draw.rect(screen, food["color"], (food["pos"][0]*CELL_SIZE, food["pos"][1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Очки и уровень
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 120, 10))

    pygame.display.update()

# Экран окончания игры
def show_game_over_screen():
    screen.fill(BLACK)
    screen.blit(font.render("Game Over!", True, RED), (WIDTH // 2 - 80, HEIGHT // 2 - 60))
    screen.blit(font.render(f"Final Score: {score}", True, WHITE), (WIDTH // 2 - 80, HEIGHT // 2 - 20))
    screen.blit(font.render(f"Level Reached: {level}", True, WHITE), (WIDTH // 2 - 80, HEIGHT // 2 + 20))
    screen.blit(font.render("Press ESC to quit...", True, GRAY), (WIDTH // 2 - 100, HEIGHT // 2 + 60))
    pygame.display.update()

    # Ожидание выхода
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

# Генерируем первую еду
food = get_food()

running = True
while running:
    clock.tick(speed)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Движение змейки по стрелкам
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, 1):
        direction = (0, -1)
    elif keys[pygame.K_DOWN] and direction != (0, -1):
        direction = (0, 1)
    elif keys[pygame.K_LEFT] and direction != (1, 0):
        direction = (-1, 0)
    elif keys[pygame.K_RIGHT] and direction != (-1, 0):
        direction = (1, 0)

    # Новая голова
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Проверка на столкновение
    if new_head in walls or new_head in snake:
        show_game_over_screen()

    snake.insert(0, new_head)

    # Если съели еду
    if food and new_head == food["pos"]:
        score += food["value"]
        food = get_food()
        if score % 5 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    # Обновляем таймер еды
    if food:
        food["timer"] -= 1
        if food["timer"] <= 0:
            food = get_food()

    draw_game()
