import pygame
from random import randrange

w_and_s = 800
s_size = 40 # Snake head size
# Random potision for spawn and othere variables
x, y = randrange(s_size, w_and_s - s_size, s_size), randrange(s_size, w_and_s - s_size, s_size)
apple = randrange(s_size, w_and_s - s_size, s_size), randrange(s_size, w_and_s - s_size, s_size)
length = 1
snake = [(x, y)]
dx = 0
dy = 0
score = 0
snake_speed = 5
level = 1
apples_to_next_level = 5

pygame.init()
screen = pygame.display.set_mode([w_and_s, w_and_s])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)#Для вывода счетчика счета
font_end = pygame.font.SysFont('Arial', 66, bold=True)

def close_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False

def generate_food():
    new_apple = randrange(s_size, w_and_s - s_size, s_size), randrange(s_size, w_and_s - s_size, s_size)
    while new_apple in snake:
        new_apple = randrange(s_size, w_and_s - s_size, s_size), randrange(s_size, w_and_s - s_size, s_size)
    return new_apple

run = True
while run:
    screen.fill((0, 0, 0))

    # drawing snake, apple
    [pygame.draw.rect(screen, pygame.Color('green'), (i, j, s_size - 1, s_size - 1)) for i, j in snake]
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, s_size, s_size))

    # show score
    render_score = font_score.render(f'SCORE: {score}  LEVEL: {level}', 1, pygame.Color('orange'))
    screen.blit(render_score, (5, 5))

    # snake movement
    if not score % apples_to_next_level and score != 0:
        level += 1
        snake_speed += 2
        apples_to_next_level += 5
    
    #Add length after ate
    x += dx * s_size
    y += dy * s_size
    snake.append((x, y))
    snake = snake[-length:]

    # eating food
    if snake[-1] == apple:
        apple = generate_food()
        length += 1
        score += 1

    # game over
    if x < 0 or x > w_and_s - s_size or y < 0 or y > w_and_s - s_size or len(snake) != len(set(snake)):
        run = False
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            screen.blit(render_end, (w_and_s // 2 - 200, w_and_s // 3))
            pygame.display.flip()
            if close_game():
                pygame.quit()
                exit()

    pygame.display.flip()
    clock.tick(snake_speed)
    # Controls
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and dy != 1:
                dx, dy = 0, -1
            elif event.key == pygame.K_s and dy != -1:
                dx, dy = 0, 1
            elif event.key == pygame.K_a and dx != 1:
                dx, dy = -1, 0
            elif event.key == pygame.K_d and dx != -1:
                dx, dy = 1, 0

    if close_game():
        pygame.quit()
        exit()
