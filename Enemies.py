__author__ = 'Erick'

'''
Erick Martinez
Emarti33@binghamton.edu
'''

UP = RIGHT = True
DOWN = LEFT = False
LANE_ONE_START_X = 195
LANE_TWO_START_X = 270
LANE_THREE_START_X = 355
RESIZE = 50,100

ONE = 1
TWO = 2
THREE = 3
import pygame

class EvilCar():

    # param - carLane (int)
    def __init__(self, carLane):
        self.__car = pygame.image.load("public/roadrage/enemycar.png")
        self.__car = pygame.transform.scale(self.__car, (RESIZE))
        self.__carRect = self.__car.get_rect()
        if carLane == ONE:
            self.__carRect = self.__carRect.move(LANE_ONE_START_X , 0)
        elif carLane == TWO:
            self.__carRect = self.__carRect.move(LANE_TWO_START_X, 0)
        elif carLane == THREE:
            self.__carRect = self.__carRect.move(LANE_THREE_START_X, 0)

# --Accessors----------------------------------------------------------------

    # Get left coordinates
    def getLeft(self):
        return self.__carRect.left

    def getRight(self):
        return self.__carRect.right

    def getTop(self):
        return self.__carRect.top

    def getBottom(self):
        return self.__carRect.bottom

    def moveCar(self, x, y):
        self.__carRect = self.__carRect.move(x, y)

    def getRect(self):
        return self.__carRect

# -- Mutators ---------------------------------------------------------------

    def renderCar(self, screen):
        screen.blit(self.__car,self.__carRect)
