#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (253 ,233,16) # Added the yellow color

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COLLECT = 0 # Collect of coins 

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
#Made the same from Enemy to coin but changed value of occurrence
class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(17, SCREEN_WIDTH-17), 0)  # There 

      def move(self):
        global COLLECT
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            COLLECT += 0
            self.rect.top = 0
            self.rect.center = (random.randint(17, SCREEN_WIDTH - 17), 0)

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
M0 = Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
enemies.add(E1)
coins.add(M0)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(M0)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

countcoin = pygame.image.load("countcoin.png")

#Game Loop
while True:      
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    coinss = font_small.render(str(COLLECT), True, YELLOW)
    DISPLAYSURF.blit(coinss, (370,10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()   
          
    # To be run if collision occurs between Player and Coin
    if pygame.sprite.spritecollideany(P1, coins):
        COLLECT += 1 # Count of earn coins will inscrease to 1
        # Music of recieving coin
        pygame.mixer.Sound('CoinRecieveSound.mp3').play() 
        for coin in pygame.sprite.spritecollide(P1, coins, True):
            coin.rect.top = 0  # Reset the position of the coin
            coin.rect.center = (random.randint(17, SCREEN_WIDTH - 17), 0)  # Move it to a new position
            new_coin = Coin()  # Create a new coin sprite
            coins.add(new_coin)  # Add it to the coins group
            all_sprites.add(new_coin)  # Add it to the rendering group

    font = pygame.font.SysFont("Verdana", 10)
    # Did the 'X' between coin and count 
    x = font.render("X", True, BLACK)
    DISPLAYSURF.blit(x, (362, 15))
    DISPLAYSURF.blit(countcoin, (340, 10))
    pygame.display.update()
    FramePerSec.tick(FPS)