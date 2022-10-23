import pygame
import pygame.freetype
import random
import time

#Width and Height
width = 400
height = 400

cx, cy = 0, 0

player1Co, player2Co = 0, 0

window = 1

greenColor = 150, 200, 20
blueColor = 67, 84, 255
orangeColor = 255, 165, 0
redColor = 250, 0, 0
purpleColor = 172, 79, 198
grayColor = 128, 128, 128

player1C = redColor
player1Choice = 1
player2C = orangeColor
player2Choice = 1

startScreen = True

FPS = 60

player_amount = 1

starttime = 0

pygame.init()

class mainDraw():
    def __init__(self):
        pass
    def drawGameBoard(self):
        pygame.draw.line(screen, (0, 0, 0), (0, 100), (400, 100))
        pygame.draw.line(screen, (0, 0, 0), (0, 300), (400, 300))
        pygame.draw.line(screen, (0, 0, 0), (150, 100), (150, 250))
        pygame.draw.line(screen, (0, 0, 0), (349, 150), (349, 300))
        pygame.draw.rect(screen, (150, 200, 20), (350, 101, 50, 198))
        pygame.draw.rect(screen, (150, 200, 20), (0, 101, 150, 198))

class player():
    def __init__(self, x, y, vel, u, d, l, r, name):
        self.x = x
        self.y = y
        self.vel = vel
        self.u = u
        self.d = d
        self.l = l
        self.r = r
        self.name = name
        self.coinColl = False
        self.cx, self.cy = 0, 0
        self.timeTick = 0
        self.endtick = 0

    def drawPlayer(self, color):
        self.color = color
        pygame.draw.rect(screen, (self.color), (self.x, self.y, 20, 20))

    def movePlayer(self):
        keys = pygame.key.get_pressed()

        if keys[self.l] and self.x > self.vel:
            if self.x == 150 and self.y < 250:
                pass
            elif self.x == 355 and self.y > 150:
                pass
            else:
                self.x -= self.vel
        if keys[self.r] and self.x < 400 - 20 - self.vel:
            if self.x == 150 - 20 and self.y < 250:
                pass
            elif self.x == 350 - 20 and self.y > 130:
                pass
            else:
                self.x += self.vel
        if keys[self.u] and self.y > 100 + 5:
            if abs(self.y - 250) < 5 and self.x > 130 and self.x < 152:
                pass
            else:
                self.y -= self.vel
        if keys[self.d] and self.y < 400 - 20 - self.vel - 100:
            if abs(self.y - 145) < 5 and self.x > 330 and self.x < 350:
                pass
            else:
                self.y += self.vel

    def collided(self):
        ticks = pygame.time.get_ticks() - starttime - self.endtick
        millis = ticks % 1000
        seconds = int(ticks / 1000 % 60)
        minutes = int(ticks / 60000 % 24)
        if self.timeTick == 0:
            out = '{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
        else:
            millisE = self.endtick % 1000
            secondsE = int(self.endtick / 1000 % 60)
            minutesE = int(self.endtick / 60000 % 24)
            out = '{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutesE, millis=millisE, seconds=secondsE)
        fontT.render_to(screen, (150, 85), out, pygame.Color('dodgerblue'))
        if event.type == pygame.MOUSEBUTTONUP:
            self.cx, self.cy = pygame.mouse.get_pos()
        didCollide1 = Ob1.detectCollP1()
        didCollide2 = Ob2.detectCollP1()
        didCollide3 = Ob3.detectCollP1()
        didCollide4 = Ob4.detectCollP1()
        coinX, coinY = c1.returnXYcoin()
        if didCollide1 or didCollide2 or didCollide3 or didCollide4 == True:
            self.x, self.y = 25, 200
            self.coinColl = False
        if abs(self.x - coinX) <= 20:
            if abs(self.y - coinY) <= 20:
                self.coinColl = True
        if self.coinColl == True:
            if self.x < 135:
                self.vel = 0
                if self.timeTick == 0:
                    self.endtick = pygame.time.get_ticks() - starttime
                    print(self.endtick)
                    self.timeTick = 1
                Won = font.render(f"{self.name} Wins!", bool(1), (255, 255, 255))
                screen.blit(Won, (100, 200))
                reset = font.render("Reset", bool(1), (255, 255, 255))
                screen.blit(reset, (150, 250))
                if self.cx > 153 and self.cx < 245:
                    if self.cy > 250 and self.cy < 281:
                        self.cx, self.cy = 0, 0
                        self.vel = 2.5
                        self.coinColl = False
                        self.timeTick = 0

    def collided2(self):
        didCollide1 = Ob1.detectCollP2()
        didCollide2 = Ob2.detectCollP2()
        didCollide3 = Ob3.detectCollP2()
        didCollide4 = Ob4.detectCollP2()
        coinX, coinY = c1.returnXYcoin()
        if didCollide1 or didCollide2 or didCollide3 or didCollide4 == True:
            self.x, self.y = 25, 200
            self.coinColl = False

    def returnXY(self):
        return self.x, self.y

    def returnCoincoll(self):
        return self.coinColl

class obstacles():
    def __init__(self, vel, x, x1, x2, y):
        self.vel = vel
        self.x = x
        self.x1 = x1
        self.x2 = x2
        self.y = y

    def drawObstacle(self):
        pygame.draw.circle(screen, (67, 84, 255), (self.x, self.y), 10, 0)

    def moveObstacle(self):
        self.x += self.vel
        if self.x == self.x1:
            self.vel = 2.5
        if self.x == self.x2:
            self.vel = -2.5

    def detectCollP1(self):
        x1, y1 = player1.returnXY()
        if abs(x1 - self.x) <= 14:
            if abs(y1 - self.y) <= 14:
                return True
            return False
        return False

    def detectCollP2(self):
        x2, y2 = player2.returnXY()
        if abs(x2 - self.x) <= 14:
            if abs(y2 - self.y) <= 14:
                return True
            return False
        return False

class coin():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drawCoin(self, p1Color, p2Color, player_amount):
        ifColl = player1.returnCoincoll()
        ifColl2 = player2.returnCoincoll()
        self.p1Color = p1Color
        self.p2Color = p2Color
        self.player_amount = player_amount
        if ifColl == True:
            pass
        else:
            pygame.draw.circle(screen, (self.p1Color), (self.x - 10, self.y), 10, 0)
        if ifColl2 == True:
            pass
        else:
            if player_amount == 2:
                pygame.draw.circle(screen, (self.p2Color), (self.x + 10, self.y), 10, 0)

    def returnXYcoin(self):
        return self.x, self.y

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#Define classes
draw = mainDraw()
player1 = player(25, 200, 2.5, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, 'Mystic')
player2 = player(25, 200, 2.5, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, 'Guest')

#Obstacles
Ob1 = obstacles(2.5, 160, 160, 340, 125)
Ob2 = obstacles(2.5, 160, 160, 340, 225)
Ob3 = obstacles(-2.5, 340, 160, 340, 175)
Ob4 = obstacles(-2.5, 340, 160, 340, 275)

#Coin
c1 = coin(375, 200)

#Event Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            cx, cy = pygame.mouse.get_pos()
            print(cx, cy)

    screen.fill((177,156,217))

    font = pygame.font.SysFont("comicsans", 50)
    fontT = pygame.freetype.SysFont("comicsans", 25)
    fontT.origin = True
    fontS = pygame.font.SysFont("comicsans", 25)

    mx, my = pygame.mouse.get_pos()
    startX, startY = 100, 200

    if startScreen == True:
        #Draw background
        for i in range(0, 15):
            x = random.randint(0, 400)
            y = random.randint(0, 400)
            dimension = random.randint(0, 40)
            color = random.choice([blueColor, redColor, orangeColor, greenColor])
            pygame.draw.rect(screen, (color), (x, y, dimension, dimension))
        #Draw start button
        start = pygame.image.load('Daco_4422541.png')
        start = pygame.transform.scale(start, (200, 70))
        dark = pygame.Surface((start.get_width(), start.get_height()), flags=pygame.SRCALPHA)
        dark.fill((100, 100, 100, 0))
        if mx > 100 and mx < 300:
            if my > 200 and my < 270:
                start.blit(dark, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
                start = pygame.transform.scale(start, (300, 105))
                startX, startY = 50, 175
        screen.blit(start, (startX, startY))
        if cx > 100 and cx < 300:
            if cy > 200 and cy < 270:
                cx, cy = 0, 0
                startScreen = False
                starttime = pygame.time.get_ticks()
                print(starttime)
        #Select amount of players
        if player_amount == 1:
            player1Co, player2Co = 255, 0
        if player_amount == 2:
            player1Co, player2Co = 0, 255
        player_amount1 = font.render("1 Player", bool(1), (player1Co, 0, 0))
        screen.blit(player_amount1, (135, 300))
        player_amount2 = font.render("2 Player", bool(1), (player2Co, 0, 0))
        screen.blit(player_amount2, (135, 350))
        if cx > 137 and cx < 270:
            if cy > 301 and cy < 337:
                player_amount = 1
        if cx > 137 and cx < 270:
            if cy > 352 and cy < 386:
                player_amount = 2

    if startScreen == False:
    #Call Classes
        draw.drawGameBoard()

    #Players
        player1.drawPlayer(player1C)
        player1.movePlayer()
        player1.collided()

        if player_amount == 2:
            player2.drawPlayer(player2C)
            player2.movePlayer()
            player2.collided()
            player2.collided2()

    #Call and Draw obstacles
        Ob1.drawObstacle()
        Ob1.moveObstacle()

        Ob2.drawObstacle()
        Ob2.moveObstacle()

        Ob3.drawObstacle()
        Ob3.moveObstacle()

        Ob4.drawObstacle()
        Ob4.moveObstacle()

    #Draw Coin
        c1.drawCoin(player1C, player2C, player_amount)

    #Change Window
        speed_up = fontS.render("^", bool(1), (0, 0, 0))
        screen.blit(speed_up, (200, 325))
        speed_up = fontS.render("v", bool(1), (0, 0, 0))
        screen.blit(speed_up, (200, 365))
        if cx > 200 and cx < 208:
            if cy > 326 and cy < 335:
                cx, cy = 0, 0
                if player_amount == 1:
                    if window == 2:
                        pass
                    else:
                        window += 1
                else:
                    window += 1
        if cx > 200 and cx < 208:
            if cy > 369 and cy < 379:
                cx, cy = 0, 0
                if window == 1:
                    pass
                else:
                    window -= 1
        if window == 1:
        #Speed Button
            #pygame.draw.rect(screen, (255, 255, 255), (160, 325, 100, 50))
            speed_label = fontS.render(f"Speed: {FPS}", bool(1), (0, 0, 0))
            screen.blit(speed_label, (164, 342))
            speed_up = fontS.render(">", bool(1), (0, 0, 0))
            screen.blit(speed_up, (265, 340))
            speed_down = fontS.render("<", bool(1), (0, 0, 0))
            screen.blit(speed_down, (140, 340))

        #Speed functionality
            if cx > 140 and cx < 150:
                if cy > 345 and cy < 356:
                    cx, cy = 0, 0
                    FPS -= 10
            if cx > 265 and cx < 345:
                if cy > 345 and cy < 356:
                    cx, cy = 0, 0
                    FPS += 10
        if window == 2:
            speed_label = fontS.render("Player 1", bool(1), (0, 0, 0))
            screen.blit(speed_label, (175, 342))
            speed_up = fontS.render(">", bool(1), (0, 0, 0))
            screen.blit(speed_up, (265, 340))
            speed_down = fontS.render("<", bool(1), (0, 0, 0))
            screen.blit(speed_down, (140, 340))
            if cx > 140 and cx < 150:
                if cy > 345 and cy < 356:
                    cx, cy = 0, 0
                    if player1Choice == 1:
                        pass
                    else:
                        player1Choice -= 1
            if cx > 265 and cx < 345:
                if cy > 345 and cy < 356:
                    cx, cy = 0, 0
                    if player1Choice == 4:
                        pass
                    else:
                        player1Choice += 1
            if player1Choice == 1:
                player1C = redColor
            if player1Choice == 2:
                player1C = orangeColor
            if player1Choice == 3:
                player1C = grayColor
            if player1Choice == 4:
                player1C = blueColor
        if window == 3:
                speed_label = fontS.render("Player 2", bool(1), (0, 0, 0))
                screen.blit(speed_label, (175, 342))
                speed_up = fontS.render(">", bool(1), (0, 0, 0))
                screen.blit(speed_up, (265, 340))
                speed_down = fontS.render("<", bool(1), (0, 0, 0))
                screen.blit(speed_down, (140, 340))
                if cx > 140 and cx < 150:
                    if cy > 345 and cy < 356:
                        cx, cy = 0, 0
                        if player2Choice == 1:
                            pass
                        else:
                            player2Choice -= 1
                if cx > 265 and cx < 345:
                    if cy > 345 and cy < 356:
                        cx, cy = 0, 0
                        if player2Choice == 4:
                            pass
                        else:
                            player2Choice += 1
                if player2Choice == 1:
                    player2C = orangeColor
                if player2Choice == 2:
                    player2C = blueColor
                if player2Choice == 3:
                    player2C = grayColor
                if player2Choice == 4:
                    player2C = redColor

#Draw title
    game_label = font.render("Capture the Flag", bool(1), (0, 0, 0))
    screen.blit(game_label, (60, 25))

#Update Display
    pygame.display.update()
    clock.tick(FPS)