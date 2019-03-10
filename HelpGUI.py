__author__ = 'Erick'

'''
Erick Martinez
Emarti33@binghamton.edu
'''

import pygame
import sys
from pygame.locals import *
import pygame.locals
import Tetris
from Tetris import makeTextObject

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
TITLE_HEIGHT = 480/6

HALF = TWO = 2
QUARTER = 4

# Credit text pos
CRED_POS = 640,475
# Font sizes
SZ_50 = 50
SZ_30 = 30
SZ_20 = 20
SZ_25 = 25

# Text Y coordinates from top
START_Y = 170
LEFT_Y = 50
RIGHT_Y = 70
UP_Y = 90
DOWN_Y = 110
Q_Y = 130
SPACE_Y =210
QUIT_Y = 230
PAUSE_Y = 250

# Colors   R   G   B
GRAY  =  (100,100,100)
WHITE =  (255,255,255)

# First closes pygame's modules then system exits to terminate program
def terminateGame():
    pygame.quit()
    sys.exit()


class Help():

    # Initialized state
    hoveredOver = False

    # Param - text (str)
    # Param - pos (tuple)
    # Param - font (font.Font)
    # Param - screen (pygame.Surface)
    # Param - color (tuple)
    def __init__(self, text, position, font, screen, color = GRAY):
        self.__text = text
        self.__coordinate = position
        self.__font = font
        self.__color = color
        self.__screen = screen
        self.setRect()
        self.draw()

    # Draws object
    def draw(self):
        self.setRend()
        self.__screen.blit(self.rend, self.rect)

    # Sets render
    def setRend(self):
        self.rend = self.__font.render(self.__text, True, self.getColor())

# -- Accessors --------------------------------------------------------------

    # Returns white if hoveredOver = True else initialized color
    def getColor(self):
        if self.hoveredOver:
            return WHITE
        else:
            return self.__color

    # Set rect coordinates
    def setRect(self):
        self.setRend()
        self.rect = self.rend.get_rect()
        self.rect.center = self.__coordinate

# Runs the gui
def runGUI():
    # initialize pygame modules
    pygame.init()
    # make screen GUI
    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    # load background image and get dimensions
    background = pygame.image.load('space.jpg')
    backgroundRect = background.get_rect()
    # load fonts
    menuFont = pygame.font.Font('Square.TTF', SZ_25)
    titleFont = pygame.font.Font('Teio.ttf', SZ_50)
    startFont = pygame.font.Font('SM.TTF', SZ_30)
    creditFont = pygame.font.Font('Digital_tech.otf',SZ_20)

    # Makes title text
    titleSurface = titleFont.render('CONTROL KEYS', True, GRAY)
    titleRect = titleSurface.get_rect()
    print(titleRect)
    titleRect.center = (WINDOW_WIDTH/HALF, TITLE_HEIGHT)

    # Makes credits text
    creditSurface = creditFont.render\
        ('Credits: Erick Martinez, Jayson Ramos, Al Sweigart', True, GRAY)
    creditRect = creditSurface.get_rect()
    creditRect.bottomright = (CRED_POS)

    # Makes menu option objects
    startOption = Help("START A GAME",
        (WINDOW_WIDTH/HALF + TWO, WINDOW_HEIGHT/HALF +START_Y), startFont, screen)


    # Make all the text surfaces and rectangles and assign coordinates
    leftSurf, leftRect=makeTextObject\
        ('Left arrow / A - Move left',menuFont,WHITE)
    leftRect.center = (WINDOW_WIDTH/HALF, TITLE_HEIGHT+LEFT_Y)
    rightSurf,rightRect=makeTextObject\
        ('Right arrow / D - Move right',menuFont,WHITE)
    rightRect.center = (WINDOW_WIDTH/HALF, TITLE_HEIGHT+RIGHT_Y)
    upSurf,upRect=makeTextObject\
        ('Up arrow / W - Rotate right',menuFont,WHITE)
    upRect.center = (WINDOW_WIDTH/HALF, TITLE_HEIGHT+UP_Y)
    downSurf,downRect=makeTextObject\
        ('Down arrow / S - Soft drop',menuFont,WHITE)
    downRect.center = (WINDOW_WIDTH/HALF, TITLE_HEIGHT+DOWN_Y)
    QSurf,QRect=makeTextObject\
        ('Q - Rotate Left',menuFont,WHITE)
    QRect.center = (WINDOW_WIDTH/HALF, TITLE_HEIGHT+Q_Y)
    spaceSurf,spaceRect=makeTextObject\
        ('Space - Hard drop',menuFont,WHITE)
    spaceRect.center=(WINDOW_WIDTH/HALF, TITLE_HEIGHT+SPACE_Y)
    quitSurf,quitRect=makeTextObject\
        ('Esc - Quit Game',menuFont,WHITE)
    quitRect.center = (WINDOW_WIDTH/HALF, TITLE_HEIGHT+QUIT_Y)
    pauseSurf,pauseRect=makeTextObject\
        ('P - Pause Game',menuFont,WHITE)
    pauseRect.center = (WINDOW_WIDTH/HALF, TITLE_HEIGHT+PAUSE_Y)

    while True: # Loop
        # Blit all the objects on the surface
        pygame.event.pump()
        screen.blit(background,backgroundRect)
        screen.blit(titleSurface,titleRect)
        screen.blit(creditSurface,creditRect)
        screen.blit(leftSurf,leftRect)
        screen.blit(rightSurf,rightRect)
        screen.blit(upSurf,upRect)
        screen.blit(downSurf,downRect)
        screen.blit(spaceSurf,spaceRect)
        screen.blit(pauseSurf,pauseRect)
        screen.blit(quitSurf,quitRect)
        screen.blit(QSurf,QRect)

        for event in pygame.event.get():
            if event.type == QUIT:
                terminateGame()

        if startOption.rect.collidepoint(pygame.mouse.get_pos()):
            startOption.hoveredOver = True
            if pygame.mouse.get_pressed()[0]:
                Tetris.main()


        else:
            startOption.hoveredOver = False


        startOption.draw()

        # Updates display
        pygame.display.update()
