__author__ = 'Erick'

'''
Erick Martinez
'''

import pygame

#Constants

LANE_TWO_COORD = 270,490
ONE = 1
TWO = 2
THREE = 3
W_HEIGHT = 600
RESIZE = 50,100
UP = RIGHT = True
DOWN = LEFT = False
SHIFT_Y = 10
SWITCH_ONE_TWO = 75
SWITCH_TWO_THREE = 85


# Makes player
class PlayerCar():
# -- init -------------------------------------------------------------------
    def __init__(self):
        self.__player = pygame.image.load("cars.png")
        self.__player = pygame.transform.scale(self.__player, (RESIZE))
        self.__lane = TWO
        self.__playerRect = self.__player.get_rect()
        self.__playerRect = self.__playerRect.move(LANE_TWO_COORD)

# -- ACCESSORS --------------------------------------------------------------
    # Get left coordinates
    # return playerRect.left
    def getLeft(self):
        return self.__playerRect.left
    # Get right coordinates
    # return playerRect.right
    def getRight(self):
        return self.__playerRect.right
    # Get top coordinates
    # return playerRect.top
    def getTop(self):
        return self.__playerRect.top
    # Get bottom coordinates
    # returns playerRect.bottom
    def getBottom(self):
        return self.__playerRect.bottom
    # returns lane
    def getLane(self):
        return self.__lane
    # returns rect coordinates
    def getRect(self):
        return self.__playerRect

# -- MUTATORS ---------------------------------------------------------------
    # moves player controlled car
    # param - move (bool)
    def playerMove(self, move):

        if move == LEFT and self.__lane == ONE:
            self.__lane = ONE

        elif move == LEFT and self.__lane == TWO:
            self.__playerRect = self.__playerRect.move(-SWITCH_ONE_TWO,0)
            self.__lane = ONE

        elif move == LEFT and self.__lane == THREE:
            self.__playerRect = self.__playerRect.move(-SWITCH_TWO_THREE,0)
            self.__lane = TWO

        elif move == RIGHT and self.__lane == ONE:
            self.__playerRect = self.__playerRect.move(SWITCH_ONE_TWO,0)
            self.__lane = TWO

        elif move == RIGHT and self.__lane == TWO:
            self.__playerRect = self.__playerRect.move(SWITCH_TWO_THREE,0)
            self.__lane = THREE

        elif move == RIGHT and self.__lane == THREE:
            self.__lane = THREE

    # moves rectangle with car
    # param - screen (int)
    def render(self, screen):
        screen.blit(self.__player, self.__playerRect)

    # moves car up and down the screen
    # param - move (int)
    def shift(self, move):
        if move == UP:
            if self.getTop() > 0:
                self.__playerRect = self.__playerRect.move(0, -SHIFT_Y)
        elif move == DOWN:
            if self.getBottom() < W_HEIGHT:
                self.__playerRect = self.__playerRect.move(0,SHIFT_Y)

