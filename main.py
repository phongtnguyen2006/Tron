"""This is a remake of the famous Tron game. There are two players. One uses WASD whil the other uses arrows keys.
The goal is to score points by living longer than your opponent or killing them.
"""
from cmu_graphics import *

###################################
#####      GameState Class    #####
###################################
app.stepsPerSecond = 60

# background music
#app.tronMusic = Sound("cmu://548659/31050429/Solar+Sailer+(From+_TRON_+Legacy__Score).mp4")

# crash sound
#app.crash = Sound("cmu://548659/31051120/crash.mp4")
#app.tronMusic.play()

# grid background
background = Group(
    Rect(0, 0, 400, 400, fill=rgb(36, 50, 58)),
    Line(40, 0, 40, 400, fill=gradient(rgb(160, 210, 216), rgb(106, 157, 161)), opacity=50),
    Line(80, 0, 80, 400, fill=gradient(rgb(160, 210, 216), rgb(106, 157, 161)), opacity=50),
    Line(120, 0, 120, 400, fill=gradient(rgb(160, 210, 216), rgb(106, 157, 161)), opacity=50),
    Line(160, 0, 160, 400, fill=gradient(rgb(160, 210, 216), rgb(106, 157, 161)), opacity=50),
    Line(200, 0, 200, 400, fill=gradient(rgb(160, 210, 216), rgb(106, 157, 161)), opacity=50),
    Line(240, 0, 240, 400, fill=gradient(rgb(160, 210, 216), rgb(106, 157, 161)), opacity=50),
    Line(280, 0, 280, 400, fill=gradient(rgb(160, 210, 216), rgb(106, 157, 161)), opacity=50),
    Line(320, 0, 320, 400, fill=gradient(rgb(160, 210, 216), rgb(106, 157, 161)), opacity=50),
    Line(360, 0, 360, 400, fill=gradient(rgb(160, 210, 216), rgb(106, 157, 161)), opacity=50),
    Line(0, 40, 400, 40, fill=gradient(rgb(160, 210, 216), rgb(106, 157, 161)), opacity=50),
    Line(0, 80, 400, 80, fill=gradient(rgb(160, 210, 216), rgb(106, 157, 161)), opacity=50),
    Line(0, 120, 400, 120, fill=gradient(rgb(160, 210, 216), rgb(106, 157, 161)), opacity=50),
    Line(0, 160, 400, 160, fill=gradient(rgb(160, 210, 216), rgb(106, 157, 161)), opacity=50),
    Line(0, 200, 400, 200, fill=gradient(rgb(160, 210, 216), rgb(106, 157, 161)), opacity=50),
    Line(0, 240, 400, 240, fill=gradient(rgb(160, 210, 216), rgb(106, 157, 161)), opacity=50),
    Line(0, 280, 400, 280, fill=gradient(rgb(160, 210, 216), rgb(106, 157, 161)), opacity=50),
    Line(0, 320, 400, 320, fill=gradient(rgb(160, 210, 216), rgb(106, 157, 161)), opacity=50),
    Line(0, 360, 400, 360, fill=gradient(rgb(160, 210, 216), rgb(106, 157, 161)), opacity=50)
)

# obstacles. Objects are added once round 3 starts
app.obstacles = Group()


# Game state classes. Controls what state/level the game is on.
class GameState(object):
    def __init__(self):

        # Define the GameState mode.
        self.mode = "START SCREEN"

        self.completed = False

        # Draw game screens
        self.drawStartScreen()
        self.drawTutorial()
        self.drawRoundOne()
        self.drawRoundTwo()
        self.drawRoundThree()

    # displays round one screen
    def displayRoundOne(self):
        self.mode = 'ROUND ONE'
        self.roundOneScreen.visible = True
        self.startScreen.visible = False

    # displays round two screen
    def displayRoundTwo(self):
        self.mode = 'ROUND TWO'
        self.roundTwoScreen.visible = True
        player1.resetPlayer()
        player2.resetPlayer()

    # displays roudn three screen
    def displayRoundThree(self):
        self.mode = 'ROUND THREE'
        self.roundThreeScreen.visible = True
        player1.resetPlayer()
        player2.resetPlayer()

    # begins round one
    def startRoundOne(self):
        self.mode = 'PLAYING STAGE ONE'
        self.roundOneScreen.visible = False

    # begins round two
    def startRoundTwo(self):
        self.mode = 'PLAYING STAGE TWO'
        self.roundTwoScreen.visible = False
        app.stepsPerSecond = 100

    # begins round three
    def startRoundThree(self):
        self.mode = 'PLAYING STAGE THREE'
        self.roundThreeScreen.visible = False
        app.stepsPerSecond = 80
        app.obstacles.add(RegularPolygon(80, 80, 30, 8, fill="darkorange"),
                          RegularPolygon(320, 160, 20, 8, fill="darkorange"),
                          RegularPolygon(60, 240, 25, 8, fill="darkorange"),
                          RegularPolygon(200, 160, 25, 8, fill="darkorange"),
                          RegularPolygon(320, 320, 20, 8, fill="darkorange"), )

    # checks to see if rounds are completed. If so moves on to next round.
    def handleOnStep(self):
        if self.mode == "PLAYING STAGE ONE" and self.completed == True:
            self.displayRoundTwo()
        elif self.mode == "PLAYING STAGE TWO" and self.completed == True:
            self.displayRoundThree()
            player1.resetPlayer()
            player2.resetPlayer()
        elif self.mode == "PLAYING STAGE THREE" and self.completed == True:
            player1.resetPlayer()
            player2.resetPlayer()
            self.drawWinner()

    ##### Drawing Functions #####

    # Draws start screen
    def drawStartScreen(self):
        self.startScreen = Group(
            Rect(115, 178, 170, 54),
            Label('START', 200, 205, fill='white', size=28, bold=True),
            Label('Player 1 uses WASD and Player 2 uses', 200, 275, fill='white', size=15, bold=True),
            Label('arrow keys. Dont hit the walls!', 200, 295, fill='white', size=15, bold=True),
            Label('TRON', 200, 120, fill='cyan', size=70, bold=True),
            Label('TRON', 200, 120, fill='white', size=65, bold=True)

        )
        self.startButton = self.startScreen.children[0]
        self.tutorialButton = self.startScreen.children[2]

    # draws instructions
    def drawTutorial(self):
        self.tutorialScreen = Group(
            Label('Tutorial', 200, 145, size=30, bold=True),
            Label('Press the left and right keys to move.', 200, 187,
                  size=17),
            Label('Avoid all of the icebergs', 200, 212, size=17),
            Label('Click anywhere to continue', 200, 270, size=15, bold=True)
        )
        self.tutorialScreen.visible = False

    # draws round one screen
    def drawRoundOne(self):
        self.roundOneScreen = Label('Round 1 (Click to Continue)', 200, 200, fill='white', size=28, bold=True)
        self.roundOneScreen.visible = False

    # draws round two screen
    def drawRoundTwo(self):
        self.roundTwoScreen = Label('Round 2 (Click to Continue)', 200, 200, fill='white', size=28, bold=True)
        self.roundTwoScreen.visible = False

    # draws round three screen
    def drawRoundThree(self):
        self.roundThreeScreen = Label('Round 3 (Click to Continue)', 200, 200, fill='white', size=28, bold=True)
        self.roundThreeScreen.visible = False

    # draws winner screen
    def drawWinner(self):
        if score.score2 > score.score1:
            Label('Red Wins!', 200, 200, fill='white', size=28, bold=True)
        elif score.score1 > score.score2:
            Label('Blue Wins!', 200, 200, fill='white', size=28, bold=True)
        elif score.score1 == score.score2:
            Label('Tie!', 200, 200, fill='white', size=28, bold=True)


###################################
#####      Player Classes     #####
###################################

# Player1 class. Controls movement and checks for collisions
class Player1(object):
    def __init__(self):
        self.keyInputs = [
            'up',
            'down',
            'left',
            'right'
        ]

        self.speed = 0
        self.angle = 0

        self.trails = Group()

        self.hitBox = Polygon(195, 189, 205, 189, 200, 186)

        self.drawing = Group(
            self.hitBox,
            Circle(195, 190, 5, fill='cyan'),
            Circle(205, 190, 5, fill='cyan'),
            Circle(197, 220, 5, fill='cyan'),
            Circle(203, 220, 5, fill='cyan'),
            Oval(200, 200, 14, 30, fill='black'),
            Oval(200, 214, 10, 24, fill='black'),
            Oval(200, 193, 10, 24, fill='white', border='black', borderWidth=2)
        )

        self.playerScore = 0

        self.drawing.centerX += 20
        self.drawing.centerY += 140

    # takes key inputs and changes respective angle based on the input
    def handleKeyInput(self, value):
        if value == "up" and self.angle == 90:
            self.angle = (self.angle - 90) % 360
            self.drawing.rotateAngle -= 90
        elif value == "up" and self.angle == 270:
            self.angle = (self.angle + 90) % 360
            self.drawing.rotateAngle += 90
        elif value == "down" and self.angle == 90:
            self.angle = (self.angle + 90) % 360
            self.drawing.rotateAngle += 90
        elif value == "down" and self.angle == 270:
            self.angle = (self.angle - 90) % 360
            self.drawing.rotateAngle -= 90
        elif value == "right" and self.angle == 180:
            self.angle = (self.angle - 90) % 360
            self.drawing.rotateAngle -= 90
        elif value == "right" and self.angle == 0:
            self.angle = (self.angle + 90) % 360
            self.drawing.rotateAngle += 90
        elif value == "left" and self.angle == 0:
            self.angle = (self.angle - 90) % 360
            self.drawing.rotateAngle -= 90
        elif value == "left" and self.angle == 180:
            self.angle = (self.angle + 90) % 360
            self.drawing.rotateAngle += 90

    # draws wall behind the bike
    def drawWall(self, x1, y1):
        new_trail = Rect(x1, y1, 2, 2, fill="cyan")
        self.trails.add(new_trail)
        if len(self.trails) > 400:
            self.trails.remove(self.trails.children[0])

    # moves bike
    def move(self):
        if self.angle == 0:
            self.drawing.centerY -= self.speed
        if self.angle == 90:
            self.drawing.centerX += self.speed
        if self.angle == 180 or self.angle == -180:
            self.drawing.centerY += self.speed
        if self.angle == 270:
            self.drawing.centerX -= self.speed

    # checks bike for collision
    def checkCollision(self):
        if self.hitBox.hitsShape(self.trails) or self.hitBox.hitsShape(app.obstacles):
            game.completed = True
            score.add2()
            #app.crash.play()
        if self.hitBox.hitsShape(player2.trails):
            game.completed = True
            score.add2()
            #app.crash.play()
        if self.hitBox.centerX < 0 or self.hitBox.centerX > 400:
            game.completed = True
            score.add2()
            #app.crash.play()
        if self.hitBox.centerY < 0 or self.hitBox.centerY > 400:
            game.completed = True
            score.add2()
            #app.crash.play()

    # starts bike movement
    def start(self):
        self.speed = 1.5

    # resets bikes position
    def resetPlayer(self):
        self.drawing.centerX = 220
        self.drawing.centerY = 340
        self.drawing.rotateAngle = 0
        self.speed = 0
        self.angle = 0
        self.trails.clear()
        game.completed = False

    # draws wall behind bike, moves bike, and checks for collisions
    def handleOnStep(self):
        self.drawWall(self.drawing.centerX, self.drawing.centerY)
        self.move()
        self.checkCollision()


# Player1 class. Controls movement and checks for collisions
class Player2(object):
    def __init__(self):
        self.keyInputs = [
            'w',
            'a',
            's',
            'd'
        ]

        self.speed = 0

        self.angle = 0

        self.trails = Group()

        self.hitBox = Polygon(195, 189, 205, 189, 200, 186)

        self.drawing = Group(
            self.hitBox,
            Circle(195, 190, 5, fill='red'),
            Circle(205, 190, 5, fill='red'),
            Circle(197, 220, 5, fill='red'),
            Circle(203, 220, 5, fill='red'),
            Oval(200, 200, 14, 30, fill='black'),
            Oval(200, 214, 10, 24, fill='black'),
            Oval(200, 193, 10, 24, fill='white', border='black', borderWidth=2)
        )

        self.playerScore = 0

        self.drawing.centerX -= 20
        self.drawing.centerY += 140

    # takes key inputs and changes respective angle based on the input
    def handleKeyInput(self, value):
        if value == "w" and self.angle == 90:
            self.angle = (self.angle - 90) % 360
            self.drawing.rotateAngle -= 90
        elif value == "w" and self.angle == 270:
            self.angle = (self.angle + 90) % 360
            self.drawing.rotateAngle += 90
        elif value == "s" and self.angle == 90:
            self.angle = (self.angle + 90) % 360
            self.drawing.rotateAngle += 90
        elif value == "s" and self.angle == 270:
            self.angle = (self.angle - 90) % 360
            self.drawing.rotateAngle -= 90
        elif value == "d" and self.angle == 180:
            self.angle = (self.angle - 90) % 360
            self.drawing.rotateAngle -= 90
        elif value == "d" and self.angle == 0:
            self.angle = (self.angle + 90) % 360
            self.drawing.rotateAngle += 90
        elif value == "a" and self.angle == 0:
            self.angle = (self.angle - 90) % 360
            self.drawing.rotateAngle -= 90
        elif value == "a" and self.angle == 180:
            self.angle = (self.angle + 90) % 360
            self.drawing.rotateAngle += 90

    # draws wall behind the bike
    def drawWall(self, x1, y1):
        new_trail = Rect(x1, y1, 2, 2, fill="red")
        self.trails.add(new_trail)
        if len(self.trails) > 400:
            self.trails.remove(self.trails.children[0])

    # moves bike
    def move(self):
        if self.angle == 0:
            self.drawing.centerY -= self.speed
        if self.angle == 90:
            self.drawing.centerX += self.speed
        if self.angle == 180 or self.angle == -180:
            self.drawing.centerY += self.speed
        if self.angle == 270:
            self.drawing.centerX -= self.speed

    # checks bike for collision
    def checkCollision(self):
        if self.hitBox.hitsShape(self.trails) or self.hitBox.hitsShape(app.obstacles):
            game.completed = True
            score.add1()
            #app.crash.play()
        if self.hitBox.hitsShape(player1.trails):
            game.completed = True
            score.add1()
            #app.crash.play()
        if self.hitBox.centerX < 0 or self.hitBox.centerX > 400:
            game.completed = True
            score.add1()
            #app.crash.play()
        if self.hitBox.centerY < 0 or self.hitBox.centerY > 400:
            game.completed = True
            score.add1()
            #app.crash.play()

    # starts bike movement
    def start(self):
        self.speed = 1.5

    # resets bikes position
    def resetPlayer(self):
        self.drawing.centerX = 180
        self.drawing.centerY = 340
        self.drawing.rotateAngle = 0
        self.speed = 0
        self.angle = 0
        self.trails.clear()
        game.completed = False

    # draws wall behind bike, moves bike, and checks for collisions
    def handleOnStep(self):
        self.drawWall(self.drawing.centerX, self.drawing.centerY)
        self.move()
        self.checkCollision()


# score class that keeps track of player 1 and player 2 score
class Score(object):
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        self.drawScore1()
        self.drawScore2()

    # draws player 1 score
    def drawScore1(self):
        self.score1Label = Label(self.score1, 380, 20, size=30, fill="cyan")

    # draws player 2 score
    def drawScore2(self):
        self.score2Label = Label(self.score2, 20, 20, size=30, fill="red")

    # adds to player 1 score
    def add1(self):
        self.score1 += 1
        self.score1Label.value = self.score1

    # adds to player 2 score
    def add2(self):
        self.score2 += 1
        self.score2Label.value = self.score2


# instantiates player1, player2, game, and score objects
player1 = Player1()
player2 = Player2()
game = GameState()
score = Score()


###################################
#####      Event Handling     #####
###################################

# takes key inputs and checks to make sure that it is on the right stage before calling player1 and player2 functions
def onKeyPress(value):
    if game.mode == 'PLAYING STAGE ONE' or game.mode == 'PLAYING STAGE TWO' or game.mode == 'PLAYING STAGE THREE':
        if ((value in player1.keyInputs)):
            player1.handleKeyInput(value)
        if ((value in player2.keyInputs)):
            player2.handleKeyInput(value)


# takes mouse input and checks to see that game is on right stage before calling other functions.
def onMousePress(mouseX, mouseY):
    if (game.tutorialButton.contains(mouseX, mouseY) == True):
        game.displayInstructions()
    elif (game.startButton.contains(mouseX, mouseY) == True):
        game.displayRoundOne()
    elif game.mode == "ROUND ONE":
        game.startRoundOne()
        player1.start()
        player2.start()
    elif game.mode == "ROUND TWO":
        game.startRoundTwo()
        player1.start()
        player2.start()
    elif game.mode == "ROUND THREE":
        game.startRoundThree()
        player1.start()
        player2.start()


# calls player1, player2, and game handleOnStep
def onStep():
    player1.handleOnStep()
    player2.handleOnStep()
    game.handleOnStep()

cmu_graphics.run()