__author__ = 'Erick'

'''
Erick Martinez
'''

# Imports
import pygame
import sys
from pygame.locals import *
import pygame.locals
import Tetris
import HelpGUI
import dodgecars

# Constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

HALF = TWO = 2
SIX = 6
QUARTER = 4
# font sizes
SZ_50 = 50
SZ_20 = 20
SZ_80 = 80

# button y coordinate from center
NEW_GAME_Y = 50
HELP_Y = 50
MINI_GAME_Y = 150

CRED_POS = 640, 475

# Colors   R   G   B
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)

ROAD_RAGE = 600, 600

# First closes pygame's modules then system exits to terminate program


def terminateGame():
    pygame.quit()
    sys.exit()


class Menu():

    # Initialized state
    hoveredOver = False

    # Param - text (str)
    # Param - pos (tuple)
    # Param - font (font.Font)
    # Param - screen (pygame.Surface)
    # Param - color (tuple)
    def __init__(self, text, position, font, screen, color=GRAY):
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

    # Sets Render
    def setRend(self):
        self.rend = self.__font.render(self.__text, True, self.getColor())

# -- Accessors --------------------------------------------------------------

    # Returns white if hoveredOver = True else initialized color
    def getColor(self):
        if self.hoveredOver:
            return WHITE
        else:
            return self.__color
    # Sets rect

    def setRect(self):
        self.setRend()
        self.rect = self.rend.get_rect()
        self.rect.center = self.__coordinate


def main():
    # initialize pygame modules
    pygame.init()
    # make screen GUI
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Erick')
    # load background image and get dimensions
    background = pygame.image.load('public/pytris/space.jpg')
    backgroundRect = background.get_rect()
    # load fonts
    menuFont = pygame.font.Font('public/fonts/Digital_tech.otf', SZ_50)
    titleFont = pygame.font.Font('public/fonts/Teio.ttf', SZ_80)
    creditFont = pygame.font.Font('public/fonts/Digital_tech.otf', SZ_20)

    # Makes title text
    titleSurface = titleFont.render('PYTRIS', True, GRAY)
    titleRect = titleSurface.get_rect()
    titleRect.center = (WINDOW_WIDTH/HALF, WINDOW_HEIGHT/SIX)

    # Makes credits text
    creditSurface = creditFont.render('Credits: Erick Martinez', True, GRAY)
    creditRect = creditSurface.get_rect()
    creditRect.bottomright = (CRED_POS)
    # Makes menu option objects
    newGameOption = Menu("NEW GAME", (WINDOW_WIDTH/HALF + TWO,
                                      WINDOW_HEIGHT/HALF - NEW_GAME_Y), menuFont, screen)
    exitGameOption = Menu("EXIT GAME", (WINDOW_WIDTH/HALF + TWO,
                                        WINDOW_HEIGHT/HALF), menuFont, screen)
    helpOption = Menu("HELP", (WINDOW_WIDTH/HALF + TWO,
                               WINDOW_HEIGHT/HALF + HELP_Y), menuFont, screen)
    miniGameOption = Menu('Dodger Minigame', (WINDOW_WIDTH/HALF + TWO,
                                              WINDOW_HEIGHT/HALF + MINI_GAME_Y), menuFont, screen)

    while True:  # Loop
        pygame.event.pump()
        screen.blit(background, backgroundRect)
        screen.blit(titleSurface, titleRect)
        screen.blit(creditSurface, creditRect)

        for event in pygame.event.get():
            if event.type == QUIT:
                terminateGame()

        if newGameOption.rect.collidepoint(pygame.mouse.get_pos()):
            newGameOption.hoveredOver = True
            if pygame.mouse.get_pressed()[0]:
                Tetris.main()
        else:
            newGameOption.hoveredOver = False

        if exitGameOption.rect.collidepoint(pygame.mouse.get_pos()):
            exitGameOption.hoveredOver = True
            if pygame.mouse.get_pressed()[0]:
                terminateGame()
        else:
            exitGameOption.hoveredOver = False

        if miniGameOption.rect.collidepoint(pygame.mouse.get_pos()):
            miniGameOption.hoveredOver = True
            if pygame.mouse.get_pressed()[0]:
                screen = pygame.display.set_mode((ROAD_RAGE))
                dodgecars.main()
        else:
            miniGameOption.hoveredOver = False

        if helpOption.rect.collidepoint(pygame.mouse.get_pos()):
            helpOption.hoveredOver = True
            if pygame.mouse.get_pressed()[0]:
                HelpGUI.runGUI()

        else:
            helpOption.hoveredOver = False

        newGameOption.draw()
        helpOption.draw()
        exitGameOption.draw()
        miniGameOption.draw()

        # Updates display
        pygame.display.update()


main()
