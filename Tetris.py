'''
Erick Martinez

CREDIT TO: AL SEIGART al@inventwithpython.com

HE PROVIDED THE TEMPLATES AND STRUCTURE OF SOME OF THE FUNCTIONS USED
IN THIS FILE.

'''

import sys, time, pygame, random
from pygame.locals import *

FPS = 25
W_WIDTH = 640 # Window dimensions
W_HEIGHT = 480
BOX_SZ = 20 # Tetrad box dimensions
B_WIDTH = 10
B_HEIGHT = 20
EMP_SPACE = '.'
ABOVE_BOARD = -2
MIDDLE_OF_BOARD = B_WIDTH*BOX_SZ
BASIC_SZ = 18
PAUSED_SZ = 24
HELP_SZ = 15
LARGE_SZ = 100
HALF = TWO = 2
THREE = 3
MOVE_SIDEWAYS_FREQ = 0.15
MOVE_DOWN_FREQ = 0.1

SHADOW_DRAWING_WIDTH = BOX_SZ -4
SHADOW_DRAWING_HEIGHT = BOX_SZ -4

SCORE_COORD = (W_WIDTH - 150, 20)
LEVEL_COORD = (W_WIDTH-150,50)

NEXT_RECT_COORD = (W_WIDTH - 120, 80) # X & Y COORDS
NEXT_PIECE_X_COORD = W_WIDTH-120
NEXT_PIECE_Y_COORD = 100

X_MARGIN = (W_WIDTH-B_WIDTH * BOX_SZ)/2
TOP_MARGIN = W_HEIGHT-(B_HEIGHT * BOX_SZ)-5

#               R    G    B
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
LIGHT_RED    = (175,  20,  20)
GREEN       = (  0, 155,   0)
LIGHT_GREEN  = ( 20, 175,  20)
BLUE        = (  0,   0, 155)
LIGHT_BLUE   = ( 20,  20, 175)
YELLOW      = (155, 155,   0)
LIGHT_YELLOW = (175, 175,  20)
ORANGE      = (255, 165,   0)
LIGHT_ORANGE = (239, 118, 51)

B_COLOR = BLUE
BG_COLOR = WHITE
TEXT_COLOR = BLACK
SHADOW_COLOR = GRAY
COLORS      = (BLUE,GREEN,RED,YELLOW)
LIGHT_COLORS = (LIGHT_BLUE, LIGHT_GREEN, LIGHT_RED, LIGHT_YELLOW)
assert len(COLORS) == len(LIGHT_COLORS) # assigns each dark to light

T_HEIGHT, T_WIDTH = 5, 5 #template dimensions

S_TETRAD_TEMPLATE = [['.....',
                     '.....',
                     '..OO.',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....']]

Z_TETRAD_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....']]

I_TETRAD_TEMPLATE = [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....']]

O_TETRAD_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']]

J_TETRAD_TEMPLATE = [['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....']]

L_TETRAD_TEMPLATE = [['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....']]

T_TETRAD_TEMPLATE = [['.....',
                     '..O..',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '.....']]

# Makes a collection of the tetrad templates for dictionary access
TETRADS = {'S': S_TETRAD_TEMPLATE,
          'Z': Z_TETRAD_TEMPLATE,
          'J': J_TETRAD_TEMPLATE,
          'L': L_TETRAD_TEMPLATE,
          'I': I_TETRAD_TEMPLATE,
          'O': O_TETRAD_TEMPLATE,
          'T': T_TETRAD_TEMPLATE}

# ----- Functions -----------------------------------------------------------

#shortcut that allows the programmer to use the same object for a text
#param text (str)
#param font (str)
#param color (tuple)
def makeTextObject(text, fontName, color=GRAY):
    objectSurface = fontName.render(text, True, color)
    return objectSurface, objectSurface.get_rect()

#terminates the program
def endGame():
    pygame.quit()
    sys.exit()

#goes through the event queue to look for the KEYUP, KEYDOWN events
def checkForKeyPress():
    # Go through event queue looking for a KEYUP event.
    # Grab KEYDOWN events to remove them from the event queue.
    checkForQuit()

    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None

# Displays a text box, pauses the game, and lists the controls in the center
# of the board until P is pressed again
# param - screen (pygame.Surface)
# param - font (str)
# param - color (tuple)
def pauseAndControls(font,color):

    # draws pause outline then inner rectangle
    pygame.draw.rect(SCREEN,BLUE,
        (X_MARGIN,TOP_MARGIN+15,(B_WIDTH*BOX_SZ)+6,(B_HEIGHT*BOX_SZ)-35),5)
    pygame.draw.rect(SCREEN,BLUE,
        (X_MARGIN+3,TOP_MARGIN+17,(B_WIDTH*BOX_SZ),(B_HEIGHT*BOX_SZ)-40))

    # Make all the text surfaces and rectangles and assign coordinates
    # Paused Text
    pausedSurf,pausedRect=makeTextObject('Paused', PAUSEDFONT, color)
    pausedRect.center=(X_MARGIN+MIDDLE_OF_BOARD/2,TOP_MARGIN+50)
    # Control Key Text
    cntrlTitleSurf,cntrlTitleRect=\
        makeTextObject('Control Keys', PAUSEDFONT, color)
    cntrlTitleRect.center = (X_MARGIN+MIDDLE_OF_BOARD/2,TOP_MARGIN+100)
    # Left key text
    leftSurf,leftRect=\
        makeTextObject('Left arrow / A - Move left',font,color)
    leftRect.center = (X_MARGIN+MIDDLE_OF_BOARD/2,TOP_MARGIN+170)
    # Right key text
    rightSurf,rightRect=\
        makeTextObject('Right arrow / D - Move right',font,color)
    rightRect.center = (X_MARGIN+MIDDLE_OF_BOARD/2,TOP_MARGIN+190)
    # Up key text
    upSurf,upRect=makeTextObject('Up arrow / W - Rotate right',font,color)
    upRect.center = (X_MARGIN+MIDDLE_OF_BOARD/2,TOP_MARGIN+210)
    # Down key text
    downSurf,downRect=\
        makeTextObject('Down arrow / S - Soft drop',font,color)
    downRect.center = (X_MARGIN+MIDDLE_OF_BOARD/2,TOP_MARGIN+250)
    # Space key text
    spaceSurf,spaceRect=makeTextObject('Space - Hard drop',font,color)
    spaceRect.center=(X_MARGIN+MIDDLE_OF_BOARD/2,TOP_MARGIN+320)
    # Quit key text
    quitSurf,quitRect=makeTextObject('Esc - Quit Game',font,color)
    quitRect.center = (X_MARGIN+MIDDLE_OF_BOARD/2,TOP_MARGIN+350)
    # Pause key text
    pauseSurf,pauseRect=makeTextObject('P - Pause Game',font,color)
    pauseRect.center =(X_MARGIN+MIDDLE_OF_BOARD/2,TOP_MARGIN+370)
    # Mute key text
    muteSurf,muteRect=makeTextObject('Q - Rotate Left',font,color)
    muteRect.center = (X_MARGIN+MIDDLE_OF_BOARD/2,TOP_MARGIN+230)

    # Blit all the objects on the surface
    SCREEN.blit(pausedSurf,pausedRect)
    SCREEN.blit(cntrlTitleSurf,cntrlTitleRect)
    SCREEN.blit(leftSurf,leftRect)
    SCREEN.blit(rightSurf,rightRect)
    SCREEN.blit(upSurf,upRect)
    SCREEN.blit(downSurf,downRect)
    SCREEN.blit(spaceSurf,spaceRect)
    SCREEN.blit(pauseSurf,pauseRect)
    SCREEN.blit(quitSurf,quitRect)
    SCREEN.blit(muteSurf,muteRect)

    while checkForKeyPress() == None:
        pygame.display.update()
        FPSCLOCK.tick()

# Loads music
def loadMusic():
    randomNumber = random.randint(0,THREE)
    if randomNumber == 0:
        pygame.mixer.music.load('Tetris_MusicA.mid')
    elif randomNumber == 1:
        pygame.mixer.music.load('Tetris_MusicB.mid')
    elif randomNumber == TWO:
        pygame.mixer.music.load('Tetris_MusicB2.mid')
    else:
        pygame.mixer.music.load('Tetris_MusicA2.mid')
    pygame.mixer.music.play(-1, 0.0)


#creates start and game over screen
#param text (str)
def showTextScreen(text):
    # This function displays large text in the
    # center of the screen until a key is pressed.
    # Draw the text drop shadow
    titleSurf, titleRect = makeTextObject(text, LARGEFONT, SHADOW_COLOR)
    titleRect.center = (int(W_WIDTH/ HALF), int(W_HEIGHT / HALF))
    SCREEN.blit(titleSurf, titleRect)

    # Draw the text
    titleSurf, titleRect = makeTextObject(text, LARGEFONT, WHITE)
    titleRect.center = (int(W_WIDTH / HALF) - 3, int(W_HEIGHT / HALF) - 3)
    SCREEN.blit(titleSurf, titleRect)

    # Draw text drop shadow
    pressKeySurf, pressKeyRect = makeTextObject('Press a key to play.',
                                                BASICFONT, SHADOW_COLOR)
    pressKeyRect.center = (int(W_WIDTH / HALF)-3, int(W_HEIGHT / HALF) + 99)
    SCREEN.blit(pressKeySurf, pressKeyRect)

    # Draw the additional "Press a key to play." text.
    pressKeySurf, pressKeyRect = makeTextObject('Press a key to play.',
                                                BASICFONT, WHITE)
    pressKeyRect.center = (int(W_WIDTH / HALF), int(W_HEIGHT / 2) + 100)
    SCREEN.blit(pressKeySurf, pressKeyRect)

    while checkForKeyPress() == None:
        pygame.display.update()
        FPSCLOCK.tick()

#handles any events that causes the program to terminate
def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        endGame() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            endGame() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back

#generates a random piece at the top of the screen
#randomly generates a color for each piece
#returns newPiece
def calculateLevelAndFallFreq(score):
    # Based on the score, return the level the player is on and
    # how many seconds pass until a falling piece falls one space.
    level = int(score / 10) + 1
    fallFreq = 0.27 - (level * 0.02)
    return level, fallFreq

#this function takes the data structure of the piece and adds
#  its boxes to the board
#data structure when the piece lands
#param board (str)
#param piece (str)
def getNewPiece():
    # return a random new piece in a random rotation and color
    shape = random.choice(list(TETRADS.keys()))
    newPiece = {'shape': shape,
                'rotation': random.randint(0, len(TETRADS[shape]) - 1),
                'x': int(B_WIDTH / HALF) - int(T_WIDTH / HALF),
                'y': ABOVE_BOARD, # start it above the board (i.e. less than 0)
                'color': random.randint(0, len(COLORS)-1)}
    # print(type(newPiece))
    # print(newPiece)
    # print(newPiece.keys())
    return newPiece

# --- BOARD FUNCTIONS -------------------------------------------------------

#creates a new blank board
#returns a new blank board
def addToBoard(board, piece):
    # fill in the board based on piece's location, shape, and rotation
    for x in range(T_WIDTH):
        for y in range(T_HEIGHT):
            if TETRADS[piece['shape']][piece['rotation']][y][x] != EMP_SPACE:
                board[x + piece['x']][y + piece['y']] = piece['color']


def getBlankBoard():
    # create and return a new blank board data structure
    board = []
    for i in range(B_WIDTH):
        board.append([EMP_SPACE] * B_HEIGHT)
    return board

#checks the XY coordinates
#param x (int)
#param y (int)
#returns true if XY coordinates are greater than 0
def isOnBoard(x, y):
    return x >= 0 and x < B_WIDTH and y < B_HEIGHT

#returns true if all the boxes in the pieces are on the board and
# isn't overlapping another piece
#param board (str)
#param piece (str)
#param adjX (int)
#param adjY (int)
def isValidPos(board, piece, adjX=0, adjY=0):
    # Return True if the piece is within the board and not colliding
    for x in range(T_WIDTH):
        for y in range(T_WIDTH):
            isAboveBoard = y + piece['y'] + adjY < 0
            if isAboveBoard or \
                TETRADS[piece['shape']][piece['rotation']][y][x]==EMP_SPACE:
                continue
            if not isOnBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
                return False
            if board[x + piece['x'] + adjX][y + piece['y'] + adjY] !=\
                    EMP_SPACE:
                return False
    return True

#returns true if a line is filled with boxes with no gaps
#param board (str)
#param y (str)
def isCompleteLine(board, y):
    # Return True if the line filled with boxes with no gaps.
    for x in range(B_WIDTH):
        if board[x][y] == EMP_SPACE:
            return False
    return True

#removes any completed lines
#moves everything above the completed line down
#records the number of completed lines
#returns number of lines removed
#param board (str)
def removeCompleteLines(board):
    # Remove any completed lines on the board, move everything
    # above them down, and return the number of complete lines.
    numLinesRemoved = 0
    y = B_HEIGHT - 1 # start y at the bottom of the board
    while y >= 0:
        if isCompleteLine(board, y):
            # Remove the line and pull boxes down by one line.
            for pullDownY in range(y, 0, -1):
                for x in range(B_WIDTH):
                    board[x][pullDownY] = board[x][pullDownY-1]
            # Set very top line to blank.
            for x in range(B_WIDTH):
                board[x][0] = EMP_SPACE
            numLinesRemoved += 1
            # Note on the next iteration of the loop, y is the same.
            # This is so that if the line that was pulled down is also
            # complete, it will be removed.
        else:
            y -= 1 # move on to check next row up
    return numLinesRemoved

#converts board's box coordinates to pixel coordinates
#returns converted pixels
#param boxx (int)
#param boxy (int)
def convertToPixelCoords(boxx, boxy):
    # Convert the given xy coordinates of the board to xy
    # coordinates of the location on the screen.
    return (X_MARGIN + (boxx * BOX_SZ)), (TOP_MARGIN + (boxy * BOX_SZ))


#--- Drawing Functions ------------------------------------------------------

#creates a single box for a piece on the screen
#stores the next boxes in pixelx and pixely
#param boxX (int)
#param boxY (int)
#param color (int)
#param pixelX (int)
#param pixelY (int)
def drawBox(boxX, boxY, color, pixelX=None, pixelY=None):
    # draw a single box (each tetromino piece has four boxes)
    # at xy coordinates on the board. Or, if pixelx & pixely
    # are specified, draw to the pixel coordinates stored in
    # pixelx & pixely (this is used for the "Next" piece).
    if color == EMP_SPACE:
        return
    if pixelX == None and pixelY == None:
        pixelX, pixelY = convertToPixelCoords(boxX,boxY)
    pygame.draw.rect(SCREEN, COLORS[color],
                     (pixelX + 1, pixelY + 1, BOX_SZ - 1, BOX_SZ - 1))
    pygame.draw.rect(SCREEN, LIGHT_COLORS[color],
                     (pixelX + 1, pixelY + 1, SHADOW_DRAWING_WIDTH,
                      SHADOW_DRAWING_HEIGHT))

#creates the board's border and all the boxes on the board
#fills the boards background
#param board (str)
#param screen (pygame.Surface)
def drawBoard(board):
    # draw the border around the board
    pygame.draw.rect(SCREEN, BLUE,
        (X_MARGIN - 3, TOP_MARGIN - 7,
         (B_WIDTH * BOX_SZ) + 8, (B_HEIGHT * BOX_SZ) + 8), 5)

    # fill the background of the board
    pygame.draw.rect(SCREEN, BG_COLOR,
        (X_MARGIN, TOP_MARGIN, BOX_SZ * B_WIDTH, BOX_SZ * B_HEIGHT))

    # draw the individual boxes on the board
    for x in range(B_WIDTH):
        for y in range(B_HEIGHT):
            drawBox(x, y, board[x][y])


#creates the score text
#creates the level text
#param score (str)
#param level (str)
def drawStatus(score, level):
    # draw the score text
    scoreSurf = BASICFONT.render('Score: %s' % score, True,WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = SCORE_COORD
    SCREEN.blit(scoreSurf, scoreRect)

    # draw the level text
    levelSurf = BASICFONT.render('Level: %s' % level, True,WHITE)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = LEVEL_COORD
    SCREEN.blit(levelSurf, levelRect)


#this function is used to create the falling piece and the next piece
#if pixelx and pixely has not been found then it uses the
# location stored in the piece data structure
#param piece (str)
#param pixelx (int)
#param pixely (int)
def drawPiece(piece, pixelx=None, pixely=None):
    shapeToDraw = TETRADS[piece['shape']][piece['rotation']]
    if pixelx == None and pixely == None:
        # if pixelx & pixely hasn't been specified, use the location
        # stored in the piece data structure
        pixelx, pixely = convertToPixelCoords(piece['x'], piece['y'])

    # draw each of the boxes that make up the piece
    for x in range(T_WIDTH):
        for y in range(T_HEIGHT):
            if shapeToDraw[y][x] != EMP_SPACE:
                drawBox(None, None, piece['color'],
                        pixelx + (x * BOX_SZ), pixely + (y * BOX_SZ))


#uses drawPiece function to create the next piece according
# to the pixelx and pixely parameters
#param piece (str)
def drawNextTetrad(tetrad):
    # draw the "next" text
    nextSurf = BASICFONT.render('Next:', True, WHITE)
    nextRect = nextSurf.get_rect()
    nextRect.topleft = NEXT_RECT_COORD
    SCREEN.blit(nextSurf, nextRect)
    # draw the "next" piece
    drawPiece(tetrad, pixelx=NEXT_PIECE_X_COORD, pixely=NEXT_PIECE_Y_COORD)

#starts a new game
#creates a new piece for the player to see while setting the falling piece
#uses a while loop to call the getNewPiece() function that
# appears on top of the board
#returns false if the isValidPosition() function is not met
# causing a game over
#uses an event handling loop that takes care of the rotating pieces
# and pauses the game
#creates the pause screen that hides the game and is activated by
# pressing the p key
#assigns movement variables keys for user to input
#if a block is in the way of rotation it returns the piece back to the
# position it was in before the key input
#increases the speed of the falling blocks when pressing the down or s key
#allows the user to press the space bar to make the piece immediately drop
#allows the pieces to continuously move the pieces by holding down the key
#after the game loop has handled all the events the game state is drawn to
#  the screen
def runGame():
    # setup variables for the start of the game
    score = 0
    lastDownT,lastSideT,lastFallT=time.time(),time.time(),time.time()
    moveD, moveL, moveR = False,False,False
    level, fallFreq = calculateLevelAndFallFreq(score)
    gameBoard = getBlankBoard()
    tetradDropping = getNewPiece()
    upcomingTetrad = getNewPiece()

    while True: # game loop
        if tetradDropping == None:
            # No falling piece in play, so start a new piece at the top
            tetradDropping = upcomingTetrad
            upcomingTetrad = getNewPiece()
            lastFallT = time.time() # reset lastFallTime

            if not isValidPos(gameBoard, tetradDropping):
                return # can't fit a new piece on the board, so game over
        possibleRotations = len(TETRADS[tetradDropping['shape']])
        checkForQuit()
        for event in pygame.event.get(): # event handling loop
            if event.type == KEYUP:
                if (event.key == K_LEFT or event.key == K_a):
                    moveL = False
                elif (event.key == K_RIGHT or event.key == K_d):
                    moveR = False
                elif (event.key == K_DOWN or event.key == K_s):
                    moveD = False
                elif event.key == K_p: # pauses game
                    pygame.mixer.music.stop()
                    pauseAndControls(HELPFONT,WHITE)
                    pygame.mixer.music.play(-1, 0.0)
                    lastDownT = time.time()
                    lastSideT = time.time()
                    lastFallT = time.time()

            elif event.type == KEYDOWN:
                # moving the piece sideways
                if (event.key == K_LEFT or event.key == K_a) and\
                        isValidPos(gameBoard, tetradDropping, adjX=-1):
                    tetradDropping['x'] -= 1
                    moveL, moveR = True, False
                    lastSideT = time.time()
                elif (event.key == K_RIGHT or event.key == K_d) and\
                        isValidPos(gameBoard, tetradDropping, adjX=1):
                    tetradDropping['x'] += 1
                    moveR, moveL = True, False
                    lastSideT = time.time()
                # rotating the piece (if there is room to rotate)
                elif event.key == K_q: # rotate
                    tetradDropping['rotation'] =\
                        (tetradDropping['rotation'] - 1) % possibleRotations
                    if not isValidPos(gameBoard, tetradDropping):
                        tetradDropping['rotation'] =\
                        (tetradDropping['rotation'] + 1) % possibleRotations
                elif event.key == K_UP or event.key == K_w:
                    tetradDropping['rotation'] =\
                        (tetradDropping['rotation'] + 1) % possibleRotations
                    if not isValidPos(gameBoard, tetradDropping):
                        tetradDropping['rotation'] =\
                            (tetradDropping['rotation']-1)%possibleRotations

                # making the piece fall faster with the down key
                elif (event.key == K_DOWN or event.key == K_s):
                    moveD = True
                    if isValidPos(gameBoard, tetradDropping, adjY=1):
                        tetradDropping['y'] += 1
                    lastDownT = time.time()

                # move the current piece all the way down
                elif event.key == K_SPACE:
                    moveD, moveL, moveR = False,False,False
                    for i in range(1, B_HEIGHT):
                        if not isValidPos\
                                    (gameBoard, tetradDropping, adjY=i):
                            break
                    tetradDropping['y'] += i - 1

        # handle moving the piece because of user input
        if (moveL or moveR) and time.time() - lastSideT > MOVE_SIDEWAYS_FREQ:
            if moveL and isValidPos(gameBoard,tetradDropping,adjX=-1):
                tetradDropping['x'] -= 1
            elif moveR and isValidPos(gameBoard,tetradDropping, adjX=1):
                tetradDropping['x'] += 1
            lastSideT = time.time()

        if moveD and time.time() - lastDownT > MOVE_DOWN_FREQ and\
                isValidPos(gameBoard,tetradDropping,adjY=1):
            tetradDropping['y'] += 1
            lastDownT = time.time()

        # let the piece fall if it is time to fall
        if time.time() - lastFallT > fallFreq:
            # see if the piece has landed
            if not isValidPos(gameBoard,tetradDropping,adjY=1):
                # falling piece has landed, set it on the board
                addToBoard(gameBoard,tetradDropping)
                score += removeCompleteLines(gameBoard)
                level, fallFreq = calculateLevelAndFallFreq(score)
                tetradDropping = None
            else:
                # piece did not land, just move the piece down
                tetradDropping['y'] += 1
                lastFallT = time.time()

        # drawing everything on the screen
        background = pygame.image.load('background.jpg')
        backgroundRect = background.get_rect()
        SCREEN.blit(background,backgroundRect)
        drawBoard(gameBoard)
        drawStatus(score,level)
        drawNextTetrad(upcomingTetrad)
        if tetradDropping != None:
            drawPiece(tetradDropping)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

# ---- MAIN -----------------------------------------------------------------

# main() function creates global constants and shows start screen
# In pygame main is for input handling, updating screen, and game objects
# randomly decides what background music to play
# calls runGame
def main():
    global FPSCLOCK,SCREEN,BASICFONT,PAUSEDFONT,HELPFONT,LARGEFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASIC_SZ)
    PAUSEDFONT = pygame.font.Font('Digital_tech.otf',PAUSED_SZ)
    HELPFONT = pygame.font.Font('freesansbold.ttf',HELP_SZ)
    LARGEFONT = pygame.font.Font('Digital_tech.otf',LARGE_SZ)
    pygame.display.set_caption('Tetromino')
    showTextScreen('Pytris')
    while True: # game loop
        loadMusic()
        runGame()
        pygame.mixer.music.stop()
        if random.randint(0, 1) == 0:
            pygame.mixer.music.load('gameover.wav')
        else:
            pygame.mixer.music.load('game_over.wav')
        pygame.mixer.music.play(0)
        showTextScreen('Game Over')

if __name__ == '__main__':
    main()
