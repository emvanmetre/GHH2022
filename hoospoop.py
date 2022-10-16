# Importing Packages
import sys
import pygame.freetype
from pygame import mixer
import webbrowser

# Global Variables
clock = pygame.time.Clock()
screenWidth = 920
screenHeight = 580
size = 920, 580
timer = None
fps = 120
pygame.display.set_caption('HOOSPOOPING?????')
x, y = 200, 130
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
count = 0
score = 0

# Initialization
pygame.init()
screen = pygame.display.set_mode((size))
pygame.display.set_caption("HoosPooping??")
mixer.init()

# Game Components
    # Sound
mixer.music.load("venv/content/music/8_bit_fun.mp3")
mixer.music.set_volume(0.2)
mixer.music.play(-1)
fartSound = pygame.mixer.Sound("venv/content/music/fart.wav")
flushSound = pygame.mixer.Sound("venv/content/music/flush.wav")
    # Graphics
imgGrass = pygame.image.load("venv/content/Graphics/grass.png")
imgGrass = pygame.transform.scale(imgGrass, (920, 580))
imgPoop = pygame.image.load("venv/content/Graphics/poop.png")
imgPoop = pygame.transform.scale(imgPoop, (50, 50))
sprite = imgPoop
poops = []
    # Loops
loop = True
scoring = False
start = False
end = False
startScreen = pygame.image.load("venv/content/Graphics/Intro.png")
startScreen = pygame.transform.scale(startScreen, (880, 540))
startButton = pygame.image.load("venv/content/Graphics/Start.png")
startButton = pygame.transform.scale(startButton, (600,150))
endScreen = pygame.image.load("venv/content/Graphics/alldone.png")
endScreen = pygame.transform.scale(endScreen, (430, 515))
categories = pygame.image.load("venv/content/Graphics/categories.png")
categories = pygame.transform.scale(categories, (320, 509))

# Game Loop
while loop:
    screen.fill((0, 0, 0))
    screen.blit(imgGrass, (0, 0))

    # Adding a sprite at every frame
    i = 0
    while i < len(poops):
        screen.blit(sprite, (poops[i], poops[i+1]))
        i = i + 2
    screen.blit(sprite, (x, y))

    # Action Screens
    if not start:
        screen.blit(startScreen, (20, 20))
        screen.blit(startButton, (150, 400))
    if scoring:
        screen.blit(categories, (320, 40))
    if end:
        screen.blit(endScreen, (275, 20))

    # Counters
    if start:
        white = (255, 255, 255)
        font = pygame.font.Font("venv/content/fonts/comicsansms.ttf", 26)
        poop = font.render('Current Poops: ' + str(count), True, white)
        scores = font.render('Total Score: ' + str(score), True, white)
        poopRect = poop.get_rect()
        scoresRect = scores.get_rect()
        poopRect.center = (780, 20)
        scoresRect.center = (550, 20)
        screen.blit(poop, poopRect)
        screen.blit(scores, scoresRect)

    # Actions Screen Actions
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            # Start or Quit
            if start == False:
                if 177 <= mouse[0] <= 429 and 429 <= mouse[1] <= 525:
                    start = True
                if 470 < mouse[0] < 721 and 429 < mouse[1] < 525:
                    loop = False
            # Finish Game
            if end and 380 <= mouse[0] <= 583 and 455 <= mouse[1] <= 504:
                loop = False

    # Gameplay Actions
    keys = pygame.key.get_pressed()
    if not scoring and not end:

        # Movement
        if keys[pygame.K_LEFT] and x > 2 and start:
            # Making sure the top left position of our character is greater than our vel so we never move off the screen.
            x -= 5
        if keys[pygame.K_RIGHT] and x < 870 and start:
            # Making sure the top right corner of our character is less than the screen width - its width
            x += 5
        if keys[pygame.K_UP] and y > 2 and start:  # Same principles apply for the y coordinate
            y -= 5
        if keys[pygame.K_DOWN] and y < 530 and start:
            y += 5

        # Dropping a Poop
        if keys[pygame.K_SPACE] and not (725 < x < 920 and 500 < y < 580) and not (520 < x < 715 and 480 < y < 580) and start:
            poops.append(x)
            poops.append(y)
            fartSound.play()
            count += 1
            pygame.time.delay(200)
            scoring = True

        # Initiating Endgame
        if keys[pygame.K_SPACE] and 520 < x < 715 and 480 < y < 580:
            scoring = False
            end = True

        # Scoring
    if keys[pygame.K_1] and scoring:
        score += 1
        scoring = False
    if keys[pygame.K_2] and scoring:
        score += 2
        scoring = False
    if keys[pygame.K_3] and scoring:
        score += 3
        scoring = False
    if keys[pygame.K_4] and scoring:
        score += 4
        scoring = False
    if keys[pygame.K_5] and scoring:
        score += 5
        scoring = False

        # Done Pooping and Flushing
    if keys[pygame.K_SPACE] and 725 < x < 920 and 480 < y < 580:
        flushSound.play()
        count = 0
        poops = []
        pygame.time.delay(500)

        # Quitting the Game Prematurely (X button)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        #Idk what this is but it breaks the game if removed
    pygame.display.flip()
    clock.tick(120)






