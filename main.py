import random
from user304_rsf8mD0BOQ_1 import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

width = 800
height = 600

class Obstacle: #Parent class
    def __init__(self, pos):
        self.pos = pos
        self.vel = Vector()
        self.radius = None
        self.img = None
        self.imgCenter = None
        self.imgDims = None
        self.imgDestDims = None
        
    def draw(self, canvas):
        canvas.draw_image(self.img, self.imgCenter, self.imgDims, self.pos.get_p(), self.imgDestDims)
        
class Moon(Obstacle): #Main player class
    def __init__(self, pos):
        super().__init__(pos)
        self.img = simplegui.load_image('https://i.imgur.com/V8bTliT.png') #Moon
        self.imgCenter = (313, 296)
        self.imgDims = (626, 592)
        self.imgDestDims= (100, 100)
        self.gravity = 0
        self.alive = True
        self.radius = 50   
        self.state = "normal"
        self.imgRotation = 0
        self.step = 0.1
        
    def update(self):   #Vertical displacement of the moon due to gravity
        if self.alive == True:
            self.pos.add(self.vel)
            self.vel.multiply(0.85)
            self.vel.add(Vector(0, (self.gravity)))
            
    def draw(self,canvas):
        canvas.draw_image(self.img, self.imgCenter, self.imgDims, self.pos.get_p(), self.imgDestDims, self.imgRotation) #imgRotation rotates the image

    def getPos(self): #Returns position of the moon
        return self.pos.get_p()
    
    def offset_d(self):
        return self.pos.y - self.radius
    
    def normalFace(self): 
        self.img = simplegui.load_image('https://i.imgur.com/V8bTliT.png') #Normal Face
        self.imgCenter = (313, 296)
        self.imgDims = (626, 592) 
        
    def starPickupFace(self): #Moon png when it picks up a star
        self.img = simplegui.load_image("https://i.imgur.com/JppwJQX.png") #Heart Face
        self.imgCenter = (313, 296)
        self.imgDims = (626, 592)
        
    def obstacleHitFace(self):
        self.img = simplegui.load_image("https://i.imgur.com/5gPFvX7.png") #Surprised Face
        self.imgCenter = (313, 296)
        self.imgDims = (626, 592)
        
class Planet(Obstacle):
    def __init__(self, pos):
        super().__init__(pos)
        self.img = simplegui.load_image('https://i.imgur.com/nh8zRKw.png') #Planet
        self.imgCenter = (273/2, 188/2)
        self.imgDims = (273, 188)
        self.imgDestDims = (140, 96)
        self.radius = 50

class Star(Obstacle):
    def __init__(self, pos):
        super().__init__(pos)
        self.img = simplegui.load_image('https://i.imgur.com/MsKwX7I.png ') #Star
        self.imgCenter = (113/2, 112/2)
        self.imgDims = (113, 112)
        self.imgDestDims = (46, 46)
        self.radius = 23
        
class Cloud(Obstacle):
    def __init__(self, pos):
        super().__init__(pos)
        self.img = simplegui.load_image('https://i.imgur.com/hLxKYTT.png') #Cloud
        self.imgCenter = (250/2, 127/2)
        self.imgDims = (250, 127)
        self.imgDestDims = (86, 46)
        self.radius = 25
        self.goLeft = True
        self.goRight = False
        self.level = 5

    def update(self):  #Set movement path for the cloud (horizontal)          
        self.pos.add(self.vel)
        if self.pos.x <= 0:
            self.goLeft = False
            self.goRight = True
        if self.pos.x >= 800:
            self.goLeft = True
            self.goRight = False
        if self.goLeft:
            self.vel.multiply(0.25)
            self.vel.add(Vector(-self.level - 1, (0)))    
        if self.goRight:
            self.vel.multiply(0.25)
            self.vel.add(Vector(self.level + 1, (0)))
            
    def increaseDifficulty(self, i):
        self.level = i/2
        
class Alien(Obstacle):
    def __init__(self, pos):
        super().__init__(pos)
        self.img = simplegui.load_image('https://i.imgur.com/8OwD4yc.png') #Alien
        self.imgCenter = (229/2, 172/2)
        self.imgDims = (229, 172)
        self.imgDestDims = (88, 48)
        self.radius = 35 
        self.goLeft = True
        self.goRight = False
        self.level = 1
        
    def update(self): #Built in horizontal edge direction
        self.pos.add(self.vel)
        if self.pos.x <= 0:
            self.goLeft = False
            self.goRight = True
        if self.pos.x >= 800:
            self.goLeft = True
            self.goRight = False
        if self.goLeft:
            self.vel.multiply(0.25)
            self.vel.add(Vector(-self.level - 5, (0)))    
        if self.goRight:
            self.vel.multiply(0.25)
            self.vel.add(Vector(self.level+ 5, (0)))
            
    def increaseDifficulty(self,i): #Increase speed of obstacle as levels increase
        self.level = i/2
        
class Asteroid(Obstacle):
    def __init__(self, pos):
        super().__init__(pos)
        self.img = simplegui.load_image('https://i.imgur.com/SBgHMg9.png') #Asteroids
        self.imgCenter = (156/2, 147/2)
        self.imgDims = (156, 147)
        self.imgDestDims = (68, 48)
        self.radius = 25
        self.angle = random.randrange(-5, 5)
        self.speed = random.randrange(2, 6)
        self.imgRotation = 0
        self.step = 0.1
        
    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.25)
        self.vel.add(Vector(self.angle, (self.speed))) #Gives asteroid random direction and random speed
        
    def draw(self,canvas): #Draw handler
        self.imgRotation += self.step #Increase rotation 
        canvas.draw_image(self.img, self.imgCenter, self.imgDims, self.pos.get_p(), self.imgDestDims, self.imgRotation) #img_rot rotates the image
        
class Wall(Obstacle): #Creates a limit wall to make player die when fall on it (out of bounds of screen)
    def __init__(self, x, y, border, colour):
        self.y = y
        self.border = border
        self.colour = colour
        self.normal = Vector(1, 0)
        self.edge = y + border
        
    def draw(self, canvas):
        canvas.draw_line((0, self.y), (width, self.y), (2 * self.border + 1), self.colour)
        
class Keyboard: #Keyboard initialisation
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.space = False
        self.m = False
        self.r = False
        
    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        if key == simplegui.KEY_MAP['left']:
            self.left = True
        if key == simplegui.KEY_MAP['up']:
            self.up = True
        if key == simplegui.KEY_MAP['space']:
            self.space = True
        if key == simplegui.KEY_MAP['M']:
            self.m = True
        if key == simplegui.KEY_MAP['R']:
            self.r = True
            
    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False
        if key == simplegui.KEY_MAP['up']:
            self.up = False
        if key == simplegui.KEY_MAP['space']:
            self.space = False
        if key == simplegui.KEY_MAP['R']:
            self.r = False 
            
class ObstacleHandler: #Deals with drawing all the obstacles by placing them into separate arrays
                        #Also handles updates of all obstacles
    def __init__(self): #Can modify the limit to change game difficulty (add more obstacles)
        self.spawnObjects = False
        self.planetLimit = 1
        self.planetList = [] 
        self.starLimit = 3
        self.starList = []
        self.cloudLimit = 1
        self.cloudList = []
        self.alienLimit = 1
        self.alienList = []
        self.asteroidLimit = 2
        self.asteroidList = []
        self.starRemoval = []
        self.lives = []
        self.walls = []
        
    def spawnPlanets(self):
        for i in range(0, self.planetLimit):
            self.vectorPosition = Vector(random.randrange(170, 730), random.randrange(120, 450))
            self.newPlanet = Planet(self.vectorPosition)
            self.addPlanet(self.newPlanet)
       
    def addPlanet(self,i):
        self.planetList.append(i)
        
    def spawnStars(self):
        for i in range(0, self.starLimit):
            self.vectorPosition = Vector(random.randrange(100, 750), random.randrange(50, 550))
            self.newStar = Star(self.vectorPosition)
            self.addStars(self.newStar)
            
    def spawnSingleStar(self):
            self.vectorPosition = Vector(random.randrange(100, 750), random.randrange(50, 550))
            self.newStar = Star(self.vectorPosition)
            self.addStars(self.newStar) 
            
    def addStars(self, i):
        self.starList.append(i)
        
    def spawnClouds(self):
        for i in range(0, self.cloudLimit):
            self.vectorPosition = Vector(random.randrange(300, 700), random.randrange(100, 500))
            self.newCloud = Cloud(self.vectorPosition)
            self.addCloud(self.newCloud)
    
    def spawnSingleCloud(self):
        self.vectorPosition = Vector(random.randrange(100, 750), random.randrange(50, 550))
        self.newCloud = Cloud(self.vectorPosition)
        self.addCloud(self.newCloud)
     
    def addCloud(self, i):
        self.cloudList.append(i)
        
    def spawnAliens(self):
        for i in range(0, self.alienLimit):
            self.vectorPosition = Vector(random.randrange(700, 750), random.randrange(100, 500))
            self.newAlien = Alien(self.vectorPosition)
            self.addAlien(self.newAlien)
            
    def spawnSingleAlien(self):
        self.vectorPosition = Vector(random.randrange(100, 750), random.randrange(50, 550))
        self.newAlien = Alien(self.vectorPosition)
        self.addAlien(self.newAlien) 
     
    def addAlien(self, i):
        self.alienList.append(i)
        
    def spawnAsteroids(self):
        for i in range(0, self.asteroidLimit):
            self.vectorPosition = Vector(random.randrange(0, 800), random.randrange(-100, 0))
            self.newAsteroid = Asteroid(self.vectorPosition)
            self.addAsteroids(self.newAsteroid)
            
    def spawnSingleAsteroid(self):
        self.vectorPosition = Vector(random.randrange(0, 800), random.randrange(-100, 0))
        self.newAsteroid = Asteroid(self.vectorPosition)
        self.addAsteroids(self.newAsteroid)
            
    def addAsteroids(self, i):
        self.asteroidList.append(i)
        
    def starRemover(self, i): #Checks if star is in list, if it is, deletes it
        for k in self.starList:
            if k == i:
                self.starList.remove(k)
    
    def initalspawn(self): #Set up the map       
        self.spawnPlanets()
        self.spawnClouds()
        self.spawnAliens()
        self.spawnAsteroids()
        self.spawnStars()
    
    def update(self): #Deals with moving obstacles
        for alien in self.alienList:
            alien.update()
        for cloud in self.cloudList:
            cloud.update()
        for asteroid in self.asteroidList:
            asteroid.update()
            if asteroid.pos.x > 820 or asteroid.pos.x < 0 or asteroid.pos.y > 620:
                self.spawnSingleAsteroid()
                self.asteroidList.remove(asteroid)
                
    def draw(self, canvas): #Draws all obstacles on canvas
        if self.spawnObjects == False:
            self.initalspawn()
            self.spawnObjects = True
        for planet in self.planetList:
            planet.draw(canvas)
        for star in self.starList:
            star.draw(canvas)
        for cloud in self.cloudList:
            cloud.draw(canvas)
        for alien in self.alienList:
            alien.draw(canvas)
        for asteroid in self.asteroidList:
            asteroid.draw(canvas)
        self.update()
        
class Interaction:
    def __init__(self,kbd):
        self.backgroundImg = simplegui.load_image("https://i.imgur.com/xOaLyeq.png") #Game Background
        self.gameover = simplegui.load_image("https://i.imgur.com/WeQXoE8.png") #Game Over Screen
        self.hitStar = simplegui.load_sound('https://assets.mixkit.co/sfx/preview/mixkit-game-click-1114.mp3')
        self.endSound = simplegui.load_sound('https://assets.mixkit.co/sfx/preview/mixkit-little-piano-game-over-1944.mp3')
        self.introSound = simplegui.load_sound('https://assets.mixkit.co/sfx/preview/mixkit-cinematic-transition-brass-hum-2282.mp3')
        self.wall = Wall(20, 800, 5, 'Red') #Creates a wall under the the screen to make player die when they fall
        self.moon = Moon(Vector(50, 75))
        self.obstacle = ObstacleHandler()
        self.spaceFlag = True #Makes obstacles visible
        self.start = False
        self.welcomeScreen = True
        self.restartBool = False
        self.musicFlag = True
        self.startMainFlag = True
        self.spawnCloudFlag = False
        self.spawnAlienFlag = True
        self.scoreArray = []
        self.kbd = kbd
        self.score = 0
        self.level = 1
        self.musicCount = 1
        self.lives = 100
        self.alienCap = 3
        self.cloudCap = 2
        
    def update(self):#Controls the player movement and detects the collisions 
        if self.start == True:
            self.keyboardinp()
            self.moon.gravity = 1 #Gives the moon gravity
            self.count = 0
            #Applys penalties and rewards
            for i in self.obstacle.planetList:
                if self.hit(self.moon, i):
                    self.lives -= 0.5
                    self.moon.obstacleHitFace()
            for i in self.obstacle.cloudList:
                if self.hit(self.moon, i):
                    #self.lives -= 0.5 #Removed point deduction for clouds
                    self.moon.normalFace()
                i.increaseDifficulty(self.level)
            for i in self.obstacle.alienList:
                if self.hit(self.moon, i):
                    self.lives -= 1
                    self.moon.obstacleHitFace()
                i.increaseDifficulty(self.level)
            for i in self.obstacle.asteroidList:
                if self.hit(self.moon, i):
                    self.lives -= 1.5
                    self.moon.obstacleHitFace()
            for i in self.obstacle.starList:
                count = 0
                if self.hit(self.moon, i):
                    self.hitStar.play()
                    self.moon.starPickupFace()
                    self.hitStar.set_volume(0.3)
                    self.score += 1
                    self.obstacle.starRemover(i)
                    self.obstacle.spawnSingleStar()
                    if self.score % 5 == 0: #Change level difficulty
                        self.level += 1
                        self.lives += 20 #Increases player's health by 20 every 5 stars collected
            if self.level % 2 == 0 and (len(self.obstacle.cloudList) != self.cloudCap) : #Setup flag to spawn new cloud every 5th level up.
                self.spawnCloudFlag = True
            if self.spawnCloudFlag == True and self.level % 3 == 0:
                self.spawnCloudFlag = False
                self.obstacle.spawnSingleCloud() #Another cloud will spawn on level 3
            if self.level % 4 == 0 and (len(self.obstacle.alienList)!= self.alienCap):
                self.spawnAlienFlag = True
            if self.spawnAlienFlag == True and self.level % 5 == 0:
                self.spawnAlienFlag = False
                self.obstacle.spawnSingleAlien() #Another alien will spawn on level 5 and 10 
            if self.lives <= 0:#Dies if you have no more health points
                self.moon.alive = False
            elif self.hitWall(self.moon, self.wall): #Dies when you hit wall
                self.moon.alive = False
            if self.moon.pos.x >990 or self.moon.pos.y < -200 or self.moon.pos.x < -200: #L,R,U OUTOFBOUND CHECK
                self.moon.alive = False

    def introScreen(self, canvas): #Displays intro screen and updates flag to remove it.
        self.intro = simplegui.load_image('https://i.imgur.com/yFGA3Sh.png') #Intro Screen 
        if self.kbd.m == False:
            self.introSound.play()
            self.introSound.set_volume(0.015)
            canvas.draw_image(self.intro, (1144/2, 719/2), (1144, 719), (400, 300), (930, 705)) #Setting Intro Screen dimensions 850, 650
        if self.kbd.m == True:
            self.startMainFlag = False   
    
    def hit(self, b1, b2): #Used to detect collisions
        sepVec = b1.pos.copy().subtract(b2.pos)
        return sepVec.length() < b1.radius + b2.radius
        #Version 2:
        #Offset1 = b1.pos + b1.radius
        #Return b1.pos + b1.radius >= b2.pos+b2.radius or b1.pos + b1.radius <= b2.pos-b2.radius
        
    def hitWall(self, m1, wall):
         return m1.offset_d() >= self.wall.edge
    
    def startGame(self):
        if self.kbd.space == True:
            self.start = True 
    
    def tick(self): #Timer - every tick it will randomise the star position
        for i in self.obstacle.starList:
            i.pos = Vector(random.randrange(170, 600), random.randrange(100, 500))
         
    def keyboardinp(self):
        if self.kbd.right:
            self.moon.vel.add(Vector(1, 0))
            if self.moon.imgRotation < 0.5:
                self.moon.imgRotation += self.moon.step #Rotates the moon to the right up to a certain point
        if self.kbd.left:
            self.moon.vel.add(Vector(-1, 0))
            if self.moon.imgRotation > -0.5:
                self.moon.imgRotation -= self.moon.step #Rotates the moon to the left up to a certain point
        if self.kbd.up:
            self.moon.vel.add(Vector(0, (-3.5)))
                  
    def mainGame(self, canvas):
        if self.startMainFlag == True:
            self.introScreen(canvas)
        if self.startMainFlag == False:
            canvas.draw_image(self.backgroundImg, (1564/2, 1123/2), (1564, 1123), (400, 300), (900, 700)) #Sets dimensions of game background screen
            self.restartBool = False
            self.startGame()
            self.update() 
            self.wall.draw(canvas)
            if self.kbd.space == True: #Detects if spacebar has been pressed in order to display obstacles/stars
                self.spaceFlag = False
            if self.spaceFlag == True:
                canvas.draw_text("START", (10, 25), 25, 'White', 'sans-serif')
                canvas.draw_text("PRESS SPACE TO START", (100, 300), 50, 'White', 'sans-serif') #(10, 40), 10
                canvas.draw_text("Avoid the aliens, the asteroids and the planet.", (200, 335), 20, 'White', 'sans-serif')
                canvas.draw_text("Collect stars for points!", (290, 355), 20, 'White', 'sans-serif')
            if self.spaceFlag == False:
                self.obstacle.draw(canvas) #if statement for when game is started
                canvas.draw_text("Stars: %s" % self.score, (680, 25), 23, 'Yellow', 'sans-serif') #Displays number of stars collected
                canvas.draw_text("Level: %s" % self.level, (680, 50), 20, 'White', 'sans-serif') #Displays the level the user is on
                canvas.draw_text("Health: %s" % self.lives, (680, 75), 20, 'LightGreen', 'sans-serif') #Displays the health the user has 
            self.moon.update()
            self.moon.draw(canvas)
            if self.score != 0: #Makes sure "+20" doesnt show at start of game
                if self.score % 5 == 0:
                    canvas.draw_text("+20", (770, 90), 15, 'LightGreen', 'sans-serif') #Tells the user +20 health has been added
                if self.level == 5 :
                    canvas.draw_text("An alien has appeared!", (230, 50), 30, 'Red', 'sans-serif')
                if self.level == 10:
                    canvas.draw_text("Another alien has appeared!", (200, 50), 30, 'Red', 'sans-serif')
            if self.lives <= 0: #Resets game when lives are 0
                self.reset(canvas)
        
    def reset(self,canvas):
        if self.musicFlag == True: #Plays gameover music for 1 loop.
            self.endSound.play()
            self.endSound.set_volume(0.05)
            self.musicCount += 1
        if self.musicCount > 120:
            self.musicFlag = False
        if self.musicFlag == False:
            self.endSound.rewind()
            #self.endSound.pause()		
        self.scoreArray.append(self.score)
        self.scoreArray.sort(reverse = True) #Highscore list.
        canvas.draw_image(self.gameover, (1144/2, 719/2), (1144, 719), (400, 300), (950, 705))
        canvas.draw_text("Level Reached: Level %s" % self.level, (316, 490), 18, 'black', 'sans-serif')
        canvas.draw_text("Total Stars: %s" % self.score, (351, 510), 18, 'black', 'sans-serif')
        canvas.draw_text("Highest Score: %s" % self.scoreArray[0] , (323, 530), 18, 'black', 'sans-serif')
        if self.kbd.r == True:
            self.restartBool = True
        if self.restartBool == True: #Reset obstacle array. create reset func in obstacle. RESET EVERYTHING
            self.lives = 100
            self.level = 1
            self.score = 0
            self.moon = Moon(Vector(50, 75))
            self.obstacle = ObstacleHandler()
            self.start = False
            self.moon.alive = True
            self.musicCount = 0
            self.musicFlag = True
            self.spaceFlag = True
            self.introSound.play()
            
    def draw(self,canvas):
        if self.moon.alive == True:
            self.mainGame(canvas)
        elif self.moon.alive == False:
            self.reset(canvas)
            
frame = simplegui.create_frame('HOPPY MOON', width, height)
label1 = frame.add_label('WELCOME TO HOPPY MOON!')
label2 = frame.add_label('', 400)
label3 = frame.add_label('Instructions:')
label4 = frame.add_label('1. Use arrow keys to move.')
label5 = frame.add_label('2. Avoid the obstacles - they ruin your health!')
label6 = frame.add_label('3. Collect stars for points - you get 20 health points for every 5 stars you collect.', 200)
label7 = frame.add_label('4. Click spacebar to start moving the moon.')

interval = 5000
kbd = Keyboard()
interaction = Interaction(kbd)

timer = simplegui.create_timer(interval, interaction.tick)
frame.set_draw_handler(interaction.draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()
timer.start()
