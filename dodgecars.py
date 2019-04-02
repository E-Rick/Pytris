'''
Erick Martinez
Emarti33@binghamton.edu
'''

import pygame, sys, random, time
from collections import deque
from Enemies import *
from PlayerCar import *
from pygame.locals import *

RIGHT = True
LEFT = False
UP = True
DOWN = False
#         R    G   B
GRAY  = (185, 185, 185)
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

pygame.init()
W_SIZE = 600, 600
W_WIDTH = 600
ENEMY_RATE = 1
W_HEIGHT = 600
textcolor = 233, 230, 20
SPEED_MIN = 1
SPEED_MAX = 3
HALF = 2
BIG_SIZE = 100
SMALL_SIZE = 18
RANDOM_MULTIPLIER_1 = 100 * random.randint(2, 6)
RANDOM_MULTIPLIER_2 = 100 * random.randint(3,5)
RANDOM_MULTIPLIER_3 = 100 * random.randint(1,5)
SCORE_INCREMENT = 200
NINETY_NINE = 99



# Global Inits
pygame.init()
TEXT_COLOR = BLACK
SHADOW_COLOR = GRAY
SCREENSURF = pygame.display.set_mode([W_WIDTH,W_HEIGHT])
BG = pygame.image.load("public/roadrage/road.png")
BG_RECT = BG.get_rect()
pygame.key.set_repeat(65, 65)
MAIN_CLOCK = pygame.time.Clock()
TEXT_FONT = pygame.font.Font('freesansbold.ttf',20)

# param text (str)
# param fontName (str)
# param color (tuple)
# creates text objects and returns the surface and rect dimensions
def createTextObject(text, fontName, color=GRAY):
    objectSurface = fontName.render(text, True, color)
    return objectSurface, objectSurface.get_rect()

# Loads music and plays it
def loadMusic():
    randomNumber = random.randint(0,1)
    if randomNumber == 0:
        pygame.mixer.music.load('public/music/rainbow_road.mid')
    else:
        pygame.mixer.music.load('public/music/mk64sherbet.mid')
    pygame.mixer.music.play(-1, 0.0)

# checks for any quit events
def checkForQuitEvent():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        endGame() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            endGame() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back

def checkForKeyPress():
    # Go through event queue looking for a KEYUP event.
    # Grab KEYDOWN events to remove them from the event queue.
    checkForQuitEvent()
    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None

# param title (string)
# displays a screen with text
def showScreen(title):
    LARGEFONT = pygame.font.Font('public/fonts/Digital_tech.otf', BIG_SIZE)
    BASICFONT = pygame.font.Font('freesansbold.ttf', SMALL_SIZE)
    titleSurf, titleRect = createTextObject(title, LARGEFONT, SHADOW_COLOR)
    titleRect.center = (int(W_WIDTH/ HALF), int(W_HEIGHT / HALF))
    SCREENSURF.blit(titleSurf, titleRect)

    # Draw the text
    titleSurf, titleRect = createTextObject(title, LARGEFONT, WHITE)
    titleRect.center = (int(W_WIDTH /HALF)-THREE, int(W_HEIGHT / HALF)-THREE)
    SCREENSURF.blit(titleSurf, titleRect)

    # Draw text
    pressKeySurf, pressKeyRect = createTextObject\
        ('Press any key to start.', BASICFONT, WHITE)
    pressKeyRect.center = \
        (int(W_WIDTH/HALF)-THREE,int(W_HEIGHT/HALF)+NINETY_NINE)
    SCREENSURF.blit(pressKeySurf, pressKeyRect)

    while checkForKeyPress() == None:
        pygame.display.update()
        MAIN_CLOCK.tick()

# Terminates the program
def endGame():
    pygame.quit()
    sys.exit()

# param - x (int)
# param - y (int)
# draws the crash image where car explodes and shows game over screen
def crash(x, y):
    pygame.mixer.music.stop()
    loadSounds()
    crashImg = pygame.image.load('public/effects/explosion.png')
    crashRect = crashImg.get_rect()
    crashRect.center = (x,y)
    SCREENSURF.blit(crashImg,crashRect)
    showScreen('Game Over')

# param playerRect (pygame.Surface)
# param enemies (list)
# Has multiple return statments because of how pygame works
# Returns true if playerRect collides with enemyRect if not false
def playerHitEnemy(playerRect, enemies):
    for enemyCar in enemies:
        if playerRect.colliderect(enemyCar.getRect()):
            return True
    return False

# Loads game over sounds
def loadSounds():
    if random.randint(0, 1) == 0:
        pygame.mixer.music.load('public/effects/gameover.wav')
    else:
        pygame.mixer.music.load('public/effects/game_over.wav')
    pygame.mixer.music.play(0)

#Lets BEGIN :D
def begin():
    # Player car object
    playerCar = PlayerCar()

    # enemy car list accumulators
    enemiesIn1 = []
    enemiesIn2 = deque()
    enemiesIn3 = []

    enemyCounter = 0
    score = 0
    #the game loop
    while True:
        SCREENSURF.blit(BG, BG_RECT)


        # makes a scoreboard
        if pygame.time.get_ticks() % SCORE_INCREMENT:
            score += 1
        scoreText = "DISTANCE: %s" % str(score)
        scoreboard = TEXT_FONT.render(scoreText,1,WHITE)
        SCREENSURF.blit(scoreboard,scoreboard.get_rect())

        enemyCounter += 1
        if enemyCounter == ENEMY_RATE:
            enemyCounter = 0
            if pygame.time.get_ticks() % (RANDOM_MULTIPLIER_3) == 0:
                randomNumber = random.randint(1,THREE)
                if randomNumber == ONE:
                    enemiesIn1.append(EvilCar(1))
                elif randomNumber == TWO:
                    enemiesIn2.append(EvilCar(TWO))
                else:
                    enemiesIn3.append(EvilCar(THREE))


        # Assign random values to cars speeds and draws them
        for car in enemiesIn1:
            car.moveCar(0,random.randint(SPEED_MIN,SPEED_MAX))
            car.renderCar(SCREENSURF)
        for car in enemiesIn2:
            car.moveCar(0,random.randint(SPEED_MIN,SPEED_MAX))
            car.renderCar(SCREENSURF)
        for car in enemiesIn3:
            car.moveCar(0,random.randint(SPEED_MIN,SPEED_MAX))
            car.renderCar(SCREENSURF)

        # User event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                endGame()

            if event.type == KEYDOWN:

                if event.key == K_UP:
                    playerCar.shift(UP)

                elif event.key == K_DOWN:
                    playerCar.shift(DOWN)

                elif event.key == K_RIGHT:
                    playerCar.playerMove(RIGHT)

                elif event.key == K_LEFT:
                    playerCar.playerMove(LEFT)

        playerCar.render(SCREENSURF)

        if enemiesIn2:
            if enemiesIn2[0].getTop() > W_HEIGHT:
                #score +=1
                enemiesIn2.popleft()
        for enemyCar in enemiesIn1[:]:
            if enemyCar.getTop() > W_HEIGHT:
                #score += 1
                enemiesIn1.remove(enemyCar)
        for enemyCar in enemiesIn3[:]:
            if enemyCar.getTop() > W_HEIGHT:
                #score +=1
                enemiesIn3.remove(enemyCar)

        pygame.display.flip()

        # Collisions
        if playerHitEnemy(playerCar.getRect(), enemiesIn1):
            coord = playerCar.getRect()
            crash(coord[0], coord[1])
            return

        if playerHitEnemy(playerCar.getRect(), enemiesIn2):
            coord = playerCar.getRect()
            crash(coord[0], coord[1])
            return
        if playerHitEnemy(playerCar.getRect(), enemiesIn3):
            coord = playerCar.getRect()
            crash(coord[0], coord[1])
            return

        MAIN_CLOCK.tick()


# Makes background and starting screen then runs a main game loop
def main():
    # import background and draw it
    backgroundSurf = pygame.image.load('public/roadrage/DodgerBG.jpg')
    backgroundRect = backgroundSurf.get_rect()
    SCREENSURF.blit(backgroundSurf,backgroundRect)
    showScreen('ROAD RAGE 2D')
    #wait till the user presses "enter" key
    while True:
        loadMusic()
        begin()
        pygame.display.update()


if __name__ == "__main__":
    main()
