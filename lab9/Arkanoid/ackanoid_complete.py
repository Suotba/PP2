import pygame 
import random
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
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
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
    return dx, dy

#block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for i in range(10) for j in range(4)] 

unbreak_block_list = [] 
unbreak_blocks = 5 # count of unbreable blocks
block_indices = random.sample(range(len(block_list)), unbreak_blocks)  # Generate random index for them
for index in block_indices:
    unbreak_block_list.append(block_list[index])
    color_list[index] = (255, 255, 255)  # The color of unbreakable blocks are white
    
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

#Pause Screen
pausefont = pygame.font.SysFont('comicsansms', 35)
p_font = pygame.font.SysFont('comicsansms', 80)
pausetext = p_font.render('Pause', 1, (255, 255, 255))
pausetextRect = pausetext.get_rect()
pausetextRect.center = (W // 2, H // 2)
paused = False

#Setting menu when paused 
settingtext = pausefont.render('Settings',1,(0,255,0))
settingRect = settingtext.get_rect()
settingRect.center = (W // 2, H // 2 - 100)
settings = False
# Speed increase button
speedincrease = pausefont.render('Speed+', 1, (0, 255, 0))
speedRectin = speedincrease.get_rect()
speedRectin.center = (W // 2 - 50, H // 2 - 200)
speedincr = False

#Paddle length increase button
paddlelenincrease = pausefont.render('PadLen+',1,(0,255,0))
paddlelenRectin = paddlelenincrease.get_rect()
paddlelenRectin.center = (W//2 - 50, H // 2 - 300)
paddlelenincr = False

# Speed decrease button
speeddecrease = pausefont.render('Speed-', 1, (255, 0, 0))
speedRectde = speeddecrease.get_rect()
speedRectde.center = (W // 2 + 90 , H // 2 - 200)
speeddecr = False

# Paddle length decrease button
paddlelendecrease = pausefont.render('PadLen-',1,(255,0,0))  # Исправлено
paddlelenRectde = paddlelendecrease.get_rect()
paddlelenRectde.center = (W//2 + 90, H // 2 - 300)
paddlelendecr = False

# Ваш основной цикл
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN: # Проверка на паузу
            if event.key == pygame.K_SPACE:   
                paused = not paused  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if settingRect.collidepoint(event.pos):
                settings = True
                paused = True
            elif speedRectin.collidepoint(event.pos):
                speedincr = True
            elif speedRectde.collidepoint(event.pos):
                speeddecr = True
            elif paddlelenRectin.collidepoint(event.pos):
                paddlelenincr = True
            elif paddlelenRectde.collidepoint(event.pos):
                paddlelendecr = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
                settings = False

    screen.fill(bg)
    
    if not paused:
        for color, block in enumerate(block_list):
            pygame.draw.rect(screen, color_list[color], block) #drawing blocks
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
        pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

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
            if hitRect not in unbreak_block_list:  # Checking block which not unbreak
                if hitColor in perfect_color:
                    game_score+=3
                block_list.pop(hitIndex)
                color_list.pop(hitIndex) 
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            collision_sound.play()
        
        #Game score
        game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
        screen.blit(game_score_text, game_score_rect)
    
        #Win/lose screens
        if ball.bottom > H:
            screen.fill((0, 0, 0))
            screen.blit(losetext, losetextRect)
            paused = False
        elif not len(block_list):
            screen.fill((255, 255, 255))
            screen.blit(wintext, wintextRect)
        
        #Paddle Control
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddleSpeed
        if key[pygame.K_RIGHT] and paddle.right < W:
            paddle.right += paddleSpeed
    else:  # If the game is paused, display the pause screen
        screen.blit(pausetext, pausetextRect)
        screen.blit(settingtext,settingRect)
    # This setting mode for game when we pressed SPACE for pause
    if settings and paused: # Checking for event
        screen.blit(speedincrease,speedRectin)
        screen.blit(speeddecrease,speedRectde)
        screen.blit(paddlelenincrease,paddlelenRectin)
        screen.blit(paddlelendecrease,paddlelenRectde)
        # Changing parametrs
        if speedincr:
            ballSpeed += 1
            speedincr = False
        elif speeddecr:
            ballSpeed -= 1
            speeddecr = False
        elif paddlelenincr:
            paddleW += 10
            paddle.width = paddleW
            paddlelenincr = False
        elif paddlelendecr:
            paddleW -= 10
            paddle.width = paddleW
            paddlelendecr = False  
    else : # Its for again pause. WHen you pressed pause without this. Screen already open setting parametrs
        settings = False
    pygame.display.flip()
    clock.tick(FPS)
