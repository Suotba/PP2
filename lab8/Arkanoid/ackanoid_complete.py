import pygame 
import random
import time
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

#paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


#Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

#Catching sound
collision_sound = pygame.mixer.Sound('audio/catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top
    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    if rect in unbreak_block_list:
        if delta_x > 0:
            dx = -dx
        elif delta_y > 0:
            dy = -dy
    return dx, dy


#block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for i in range(10) for j in range(4)] 

# Create unbreakable blocks
unbreak_block_list = [] 
unbreak_blocks = 5 # count of unbreable blocks
block_indices = random.sample(range(len(block_list)), unbreak_blocks)  # Generate random index for them
for index in block_indices:
    unbreak_block_list.append(block_list[index])
    color_list[index] = (255, 255, 255)  # The color of unbreakable blocks are white

for color, block in zip(color_list, block_list):
    pygame.draw.rect(screen, color, block)

#Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

time1 = pygame.time.get_ticks() # first time

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)

    time2 = pygame.time.get_ticks()  # second time
    if time2 - time1 >= 6000:  # Pass 6 sec
        ballSpeed += 1  
        time1 = time2
    # print(next(enumerate(block_list)))
    
    if time2 - time1 >=10000:
        paddleSpeed +=1
        time1 = time2

    [pygame.draw.rect(screen, color_list[color], block)
     for color, block in enumerate (block_list)] #drawing blocks
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)
    # print(next(enumerate (block_list)))

    #Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    #Collision left 
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    #Collision top
    if ball.centery < ballRadius + 50: 
        dy = -dy
    #Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)
    
    #Collision blocks
    hitIndex = ball.collidelist(block_list)
    ubreakIndex = ball.collidelist(unbreak_block_list)
    perfect_color = [(255,0,0),(0,255,0),(0,0,255)] # bonus color
    if hitIndex != -1:
        hitRect = block_list[hitIndex]
        hitColor = color_list[hitIndex]
        if hitRect not in unbreak_block_list:  # Checling block which not unbreak
            if hitColor in perfect_color:
                game_score+=3
            else:
                game_score+=1
            block_list.pop(hitIndex)
            color_list.pop(hitIndex) 
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            collision_sound.play()
        else:
            dx, dy = detect_collision(dx, dy, ball, hitRect)  

    #Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    #Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255,255, 255))
        screen.blit(wintext, wintextRect)
    # print(pygame.K_LEFT)
    #Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    pygame.display.flip()
    clock.tick(FPS)