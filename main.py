import pygame
import random
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARKGREEN = (0, 75, 0)
GREYGREEN = (30, 45, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (0, 150, 150)
GREY = (120, 120, 120)
DARKGREY = (50, 50, 50)
LIGHTBROWN = (255, 170, 100)


# hero
class hero():
    def __init__(self):
        self.x = 0
        self.y = 300
        self.hp = 5
        self.ammo = 10
        self.width = 30
        self.height = 75
        self.distance = 800
        self.inSafe = 0
        self.inGerms = pygame.time.get_ticks()
        self.enterTime = pygame.time.get_ticks()

    # hero movement
    def moveHero(self):
        if 0 <= self.x + xChange <= 775 and 115 <= self.y + yChange <= 480:
            self.x += xChange
            self.y += yChange

    # draw hero on screen
    def drawHero(self, screen):
        # pants
        pygame.draw.rect(screen, BLUE, [self.x + 18, self.y + 50, 10, 25])
        pygame.draw.rect(screen, BLUE, [self.x, self.y + 50, 10, 25])
        # shoes
        pygame.draw.rect(screen, BLACK, [self.x + 18, self.y + 75, 10, 10])
        pygame.draw.rect(screen, BLACK, [self.x, self.y + 75, 10, 10])
        # body
        pygame.draw.rect(screen, RED, [self.x - 5, self.y + 20, 35, 40])
        # head
        pygame.draw.rect(screen, LIGHTBROWN, [self.x, self.y, 30, 25])
        # eyes
        pygame.draw.rect(screen, BLACK, [self.x + 13, self.y + 5, 4, 10])
        pygame.draw.rect(screen, BLACK, [self.x + 25, self.y + 5, 4, 10])
        # hair
        pygame.draw.rect(screen, BLACK, [self.x - 2, self.y - 8, 35, 14])
        # mask
        pygame.draw.rect(screen, LIGHTBLUE, [self.x + 5, self.y + 13, 25, 10])
        pygame.draw.line(screen, LIGHTBLUE, [self.x + 5, self.y + 13], [self.x, self.y + 10], 3)
        pygame.draw.line(screen, LIGHTBLUE, [self.x + 5, self.y + 20], [self.x, self.y + 20], 3)
        # arms
        pygame.draw.line(screen, LIGHTBROWN, [self.x + 10, self.y + 35], [self.x - 5, self.y + 35], 7)

        # gun
        pygame.draw.rect(screen, GREEN, [self.x + 10, self.y + 30, 30, 10])
        pygame.draw.rect(screen, GREEN, [self.x + 10, self.y + 30, 10, 18])

    # draw hero healthbar
    def drawHealth(self, screen):
        self.healthX = 100
        for i in range(self.hp):
            pygame.draw.polygon(screen, RED, [[self.healthX, 20],[self.healthX + 5, 25], [self.healthX + 10, 20]])
            pygame.draw.circle(screen, RED, [self.healthX + 3, 20], 3)
            pygame.draw.circle(screen, RED, [self.healthX + 8, 20], 3)
            self.healthX += 20

    # draw hero ammobar
    def drawAmmo(self, screen):
        self.ammoX = 100
        for i in range(self.ammo):
            pygame.draw.rect(screen, LIGHTBLUE, [self.ammoX, 40, 10, 6])
            pygame.draw.circle(screen, LIGHTBLUE, [self.ammoX + 10, 43], 3)
            self.ammoX += 20

    # damage from zombie germ circle
    def tooClose(self):
        # distance from circle
        self.distance = math.sqrt((750 - self.x - self.width) ** 2 + (325 - self.y - self.height) ** 2)
        # entered circle and past 1 sec
        if self.distance < 200 and pygame.time.get_ticks() - self.enterTime >= 1000:
            self.enterTime = pygame.time.get_ticks()
            self.hp -= 1

            # draw damage
            # pants
            pygame.draw.rect(screen, RED, [self.x + 18, self.y + 50, 10, 25])
            pygame.draw.rect(screen, RED, [self.x, self.y + 50, 10, 25])
            # shoes
            pygame.draw.rect(screen, RED, [self.x + 18, self.y + 75, 10, 10])
            pygame.draw.rect(screen, RED, [self.x, self.y + 75, 10, 10])
            # body
            pygame.draw.rect(screen, RED, [self.x - 5, self.y + 20, 35, 40])
            # head
            pygame.draw.rect(screen, RED, [self.x, self.y, 30, 25])
            # eyes
            pygame.draw.rect(screen, BLACK, [self.x + 13, self.y + 5, 4, 10])
            pygame.draw.rect(screen, BLACK, [self.x + 25, self.y + 5, 4, 10])
            # hair
            pygame.draw.rect(screen, RED, [self.x - 2, self.y - 8, 35, 14])
            # mask
            pygame.draw.rect(screen, LIGHTBLUE, [self.x + 5, self.y + 13, 25, 10])
            pygame.draw.line(screen, LIGHTBLUE, [self.x + 5, self.y + 13], [self.x, self.y + 10], 3)
            pygame.draw.line(screen, LIGHTBLUE, [self.x + 5, self.y + 20], [self.x, self.y + 20], 3)
            # arms
            pygame.draw.line(screen, RED, [self.x + 10, self.y + 35], [self.x - 5, self.y + 35], 7)

    # damage from germs on ground
    def germDamage(self, germs):
        if germs.createGerms:
            # distance from safe area
            self.safeDist = math.sqrt((germs.safeX - self.x - self.width) ** 2 + (germs.safeY - self.y - self.height) ** 2)
            # out of safe area (in germs) and past 1 sec
            if self.safeDist > germs.safeRad and pygame.time.get_ticks() - self.inGerms >= 1000:
                self.inGerms = pygame.time.get_ticks()
                self.hp -= 1

                # draw damage
                # pants
                pygame.draw.rect(screen, RED, [self.x + 18, self.y + 50, 10, 25])
                pygame.draw.rect(screen, RED, [self.x, self.y + 50, 10, 25])
                # shoes
                pygame.draw.rect(screen, RED, [self.x + 18, self.y + 75, 10, 10])
                pygame.draw.rect(screen, RED, [self.x, self.y + 75, 10, 10])
                # body
                pygame.draw.rect(screen, RED, [self.x - 5, self.y + 20, 35, 40])
                # head
                pygame.draw.rect(screen, RED, [self.x, self.y, 30, 25])
                # eyes
                pygame.draw.rect(screen, BLACK, [self.x + 13, self.y + 5, 4, 10])
                pygame.draw.rect(screen, BLACK, [self.x + 25, self.y + 5, 4, 10])
                # hair
                pygame.draw.rect(screen, RED, [self.x - 2, self.y - 8, 35, 14])
                # mask
                pygame.draw.rect(screen, LIGHTBLUE, [self.x + 5, self.y + 13, 25, 10])
                pygame.draw.line(screen, LIGHTBLUE, [self.x + 5, self.y + 13], [self.x, self.y + 10], 3)
                pygame.draw.line(screen, LIGHTBLUE, [self.x + 5, self.y + 20], [self.x, self.y + 20], 3)


# hero's bullets
class bullet():
    def __init__(self, hero):
        self.bulX = hero.x
        self.bulY = hero.y
        self.drawBul = True

    # bullet movement
    def moveBullet(self):
        self.bulX += 5

    # draw bullet on screen
    def drawBullet(self, screen):
        pygame.draw.rect(screen, LIGHTBLUE, [self.bulX + 10, self.bulY + 32, 25, 5])

# vaccine ammo
class vaccine():
    def __init__(self):
        self.vacX = 0
        self.vacY = 0
        self.drawVax = False

    # create vaccine
    def createVaccine(self):
        self.vacX = random.randint(0, 550)
        self.vacY = random.randint(115, 450)

    # draw vaccine on screen
    def drawVaccine(self, screen):
        pygame.draw.rect(screen, LIGHTBLUE, [self.vacX, self.vacY, 15, 30])
        pygame.draw.polygon(screen, LIGHTBLUE, [[self.vacX, self.vacY + 30], [self.vacX + 14, self.vacY + 30], [self.vacX + 7, self.vacY + 40]])
        pygame.draw.line(screen, LIGHTBLUE, [self.vacX + 7, self.vacY], [self.vacX + 7, self.vacY - 10], 3)
        pygame.draw.ellipse(screen, LIGHTBLUE, [self.vacX, self.vacY - 15, 16, 5])

    # hero collects vaccine
    def collectVaccine(self, hero):
        # if hero on vaccine
        if hero.x < self.vacX + 7 < hero.x + hero.width and hero.y - 10 < self.vacY + 5 < hero.y + hero.height and hero.ammo < 10:
            hero.ammo += 1
            self.drawVax = False
        else:
            self.drawVax = True

# zombie/infected
class zombie():
    def __init__(self):
        self.x = 675
        self.y = 200
        self.hp = 15
        self.xChange = 0

    # bullet zombie collision
    def shootZombie(self, bullet):
        # if bullet hits zombie
        if self.x == bullet.bulX and self.y - 100 < bullet.bulY < self.y + 240:
            bullet.drawBul = False
            self.hp -= 1

            # draw damage
            pygame.draw.rect(screen, RED, [self.x, self.y + 140, 35, 100])
            pygame.draw.rect(screen, RED, [self.x + 55, self.y + 140, 35, 100])
            # body
            pygame.draw.rect(screen, RED, [self.x, self.y, 100, 150])
            # head
            pygame.draw.rect(screen, RED, [self.x - 15, self.y - 25, 80, 70])
            # eyes
            pygame.draw.rect(screen, BLACK, [self.x, self.y, 5, 15])
            pygame.draw.rect(screen, BLACK, [self.x + 25, self.y, 5, 15])
            # eyebrows
            pygame.draw.line(screen, BLACK, [self.x - 8, self.y - 5], [self.x + 50, self.y - 5], 3)
            # arms
            pygame.draw.rect(screen, RED, [self.x - 100, self.y + 50, 100, 20])
            pygame.draw.rect(screen, RED, [self.x - 50, self.y + 65, 100, 25])

    # draw zombie on screen
    def drawZombie(self, screen):
        # pants
        pygame.draw.rect(screen, BLUE, [self.x, self.y + 140, 35, 100])
        pygame.draw.rect(screen, BLUE, [self.x + 55, self.y + 140, 35, 100])
        # body
        pygame.draw.rect(screen, DARKGREEN, [self.x, self.y, 100, 150])
        # head
        pygame.draw.rect(screen, GREEN, [self.x - 15, self.y - 25, 80, 70])
        # eyes
        pygame.draw.rect(screen, BLACK, [self.x, self.y, 5, 15])
        pygame.draw.rect(screen, BLACK, [self.x + 25, self.y, 5, 15])
        # eyebrows
        pygame.draw.line(screen, BLACK, [self.x - 8, self.y - 5], [self.x + 50, self.y - 5], 3)
        # arms
        pygame.draw.rect(screen, GREEN, [self.x - 100, self.y + 50, 100, 20])
        pygame.draw.rect(screen, GREEN, [self.x - 50, self.y + 65, 100, 25])

    # draw zombie healthbar
    def drawHealth(self, screen):
        self.healthX = 785
        for i in range(self.hp):
            pygame.draw.polygon(screen, GREEN, [[self.healthX, 20], [self.healthX - 5, 25], [self.healthX - 10, 20]])
            pygame.draw.circle(screen, GREEN, [self.healthX - 3, 20], 3)
            pygame.draw.circle(screen, GREEN, [self.healthX - 8, 20], 3)
            self.healthX -= 20

# germs on ground
class germs():
    def __init__(self):
        self.safeX = 0
        self.safeY = 0
        self.safeRad = 0
        self.drawSafe = True
        self.createGerms = False

    # create safe spaces
    def createSafe(self):
        self.safeX = random.randint(100, 450)
        self.safeY = random.randint(200, 400)
        self.safeRad = random.randint(50, 100)

    # draw ground germs on screen
    def drawGerms(self, screen):
        pygame.draw.rect(screen, GREYGREEN, [0, 125, 800, 420])
        pygame.draw.circle(screen, DARKGREY, [self.safeX, self.safeY], self.safeRad)

# create/draw background
def drawBackground():
    # road lines
    offset = 0
    while offset < 800:
        pygame.draw.rect(screen, YELLOW, [-20 + offset, 300, 100, 10])
        offset += 150

    # border / fence
    pygame.draw.rect(screen, GREY, [0, 575, 800, 7])
    pygame.draw.rect(screen, GREY, [0, 590, 800, 7])

    pygame.draw.rect(screen, GREY, [0, 75, 800, 7])
    pygame.draw.rect(screen, GREY, [0, 90, 800, 7])

    offset = 0
    while offset < 850:
        pygame.draw.rect(screen, GREY, [-2 + offset, 565, 5, 40])
        pygame.draw.rect(screen, GREY, [-2 + offset, 65, 5, 40])
        offset += 50

pygame.init()

# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# objects
myHero = hero()
myZombie = zombie()
myGerms = germs()
myVaccine = vaccine()
myBullet = bullet(myHero)

# item lists
bulletList = []
safeList = []
zombieList = []

# speed
xChange = 0
yChange = 0

# time
germTime = pygame.time.get_ticks()
safeTime = pygame.time.get_ticks()
zombieTime = pygame.time.get_ticks()

# shoot bullet var
shoot = False

# -------- Main Program Loop -----------

while not done:

    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            # movement via arrow keys
            if event.key == pygame.K_UP:
                yChange = -5
            elif event.key == pygame.K_DOWN:
                yChange = 5
            elif event.key == pygame.K_LEFT:
                xChange = -5
            elif event.key == pygame.K_RIGHT:
                xChange = 5
        # stop movement
        elif event.type == pygame.KEYUP:
            xChange = 0
            yChange = 0

        # mouseclick
        if event.type == pygame.MOUSEBUTTONDOWN:
            shoot = True

        # --- Game logic should go here
    screen.fill(DARKGREY)

    # hero dies
    if myHero.hp == 0:

        # length of cutscene
        if len(zombieList) < 5:
            drawBackground()
            # add new zombie/ 2 seconds
            if pygame.time.get_ticks() - zombieTime >= 2000:
                zombieTime = pygame.time.get_ticks()
                myZombie = zombie()
                myZombie.x = 1000
                zombieList.append(myZombie)

            # draw zombie mob
            for item in zombieList:
                item.drawZombie(screen)
                item.x -= random.randint(1, 5)
                if item.x < -100:
                    item.x = 850

        # loser test
        else:
            font = pygame.font.SysFont("Pokemon GB.ttf", 50, True, False)
            loseText1 = font.render("OH NO!", True, WHITE)
            loseText2 = font.render("THE INFECTED HAVE TAKEN OVER!", True, WHITE)
            screen.blit(loseText1, [300, 250])
            screen.blit(loseText2, [50, 300])

    # zombie dies
    elif myZombie.hp == 0:
        drawBackground()

        # draw winner hero
        pygame.draw.circle(screen, YELLOW, [400, 460], 100)
        myHero.x = 385
        myHero.y = 430
        myHero.drawHero(screen)

        # winner text
        font = pygame.font.SysFont("Pokemon GB.ttf", 50, True, False)
        winText1 = font.render("CONGRATS!", True, WHITE)
        winText2 = font.render("YOU HAVE DEFEATED THE INFECTED", True, WHITE)
        winText3 = font.render("AND SAVED THE WORLD!", True, WHITE)
        screen.blit(winText1, [300, 150])
        screen.blit(winText2, [50, 200])
        screen.blit(winText3, [160, 250])

    # in game
    else:

        # create bullets
        if shoot and myHero.ammo > 0:
            myBullet = bullet(myHero)
            bulletList.append(myBullet)
            myHero.ammo -= 1
            shoot = False

        # create/pick up vaccines
        if not myVaccine.drawVax:
            myVaccine.createVaccine()
        myVaccine.collectVaccine(myHero)

        # create germs
        if pygame.time.get_ticks() - germTime >= 10000:
            germTime = pygame.time.get_ticks()
            myGerms.createGerms = not myGerms.createGerms

        # create safe spaces
        if pygame.time.get_ticks() - safeTime >= 3000 and myGerms.drawSafe:
            safeTime = pygame.time.get_ticks()
            myGerms.createSafe()
            myGerms.drawSafe = False
        else:
            myGerms.drawSafe = True


        # DRAWING
        drawBackground()

        # distancing area
        pygame.draw.circle(screen, GREYGREEN, [750, 325], 200)

        # draw germs and safe areas
        if myGerms.createGerms:
            myGerms.drawGerms(screen)

        # draw healthbar and ammo bar
        myHero.drawHealth(screen)
        myHero.drawAmmo(screen)

        # draw vaccine
        if myVaccine.drawVax:
            myVaccine.drawVaccine(screen)

        # draw zombie, zombie healthbar
        myZombie.drawZombie(screen)
        myZombie.drawHealth(screen)

        # shoot/draw bullets
        for item in bulletList:
            item.moveBullet()
            myZombie.shootZombie(item)
            if item.drawBul:
                item.drawBullet(screen)

        # move/draw hero, take damage
        myHero.moveHero()
        myHero.drawHero(screen)
        myHero.tooClose()
        myHero.germDamage(myGerms)

        # health, ammo text
        font = pygame.font.SysFont("Pokemon GB.ttf", 27, True, False)
        healthText = font.render("HEALTH", True, WHITE)
        ammoText = font.render("AMMO", True, WHITE)
        screen.blit(healthText, [5, 12])
        screen.blit(ammoText, [10, 35])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()