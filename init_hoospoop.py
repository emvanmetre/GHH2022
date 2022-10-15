# Importing Packages
import pygame, sys
from pygame.locals import *
import pygame.freetype
from pygame import mixer
from tkinter import *
from tkinter import messagebox
import pygamepopup
from pygamepopup.components import Button, InfoBox

# Global Variables
clock = pygame.time.Clock()
screenWidth = 920
screenHeight = 580
size = 920, 580
timer = None
fps = 120
pygame.display.set_caption('HOOSPOOPING?????')
x, y = 200, 130
black = (0,0,0)
white = (255,255,255)
green = (0, 255, 0)
red = (255, 0, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

# Load Graphics
imgGrass = pygame.image.load("venv/content/Graphics/grass.png")
imgGrass = pygame.transform.scale(imgGrass, (920,580))
imgPoop = pygame.image.load("venv/content/Graphics/poop.png")
imgPoop = pygame.transform.scale(imgPoop, (50,50))

# Initialization Function
pygame.init()
screen = None
timer = pygame.time.Clock()
screen = pygame.display.set_mode((size))
pygame.display.set_caption("HoosPooping??")
mixer.init()
mixer.music.load("venv/content/music/8_bit_fun.mp3")
mixer.music.set_volume(0.2)
mixer.music.play(-1)

# Instructions Menu
def intro():
    intro = True
    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Hoos Pooping?", largeText)
        TextRect.center = ((screenWidth / 2), (screenHeight / 2))
        screen.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(screen, bright_green, (150, 450, 100, 50))
        else:
            pygame.draw.rect(screen, green, (150, 450, 100, 50))


        pygame.draw.rect(screen, red, (550, 450, 100, 50))


        pygame.display.update()
        clock.tick(15)




# Bowel (Sprite) Movement Mechanics
sprite = imgPoop
loop = True
while loop:
    screen.fill((0, 0, 0))
    screen.blit(imgGrass, (0, 0))
    # this adds the sprite at every frame rate
    screen.blit(sprite, (x, y))

    for event in pygame.event.get():
        # this is to close the window
        if event.type == QUIT:
            loop = False
            # sys.exit() # this will close the kernel too
            # in development mode leave the comment above
    # This is the list with the keys being pressed, boundaries appended
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 2:  # Making sure the top left position of our character is greater than our vel so we never move off the screen.
        x -= 5
    if keys[pygame.K_RIGHT] and x < 870:  # Making sure the top right corner of our character is less than the screen width - its width
        x += 5
    if keys[pygame.K_UP] and y > 2:  # Same principles apply for the y coordinate
        y -= 5
    if keys[pygame.K_DOWN] and y < 530:
        y += 5
    pygame.time.delay(0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # we update the screen at every frame
    pygame.display.flip()
    # if we put the frame rate at 60 the sprite will move slower
    clock.tick(120)

# Game Loop
done = False
while done == False:

    # Check input
    for event in pygame.event.get():
        if (event.type == QUIT):
            done = True

    # Draw graphics

 ##   window.fill(bgColor)

 ##   window.blit(imgGrass, (0, 0))  # draw at (0,0)
 ##   window.blit(imgPoop, (0, 0))  # draw at (0,0)

    # Update screen
    pygame.display.flip()
    clock.tick(fps)

# Closing the Game
from sys import exit
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
intro()
pygame.display.quit()
pygame.quit()
sys.exit()