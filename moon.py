import random
from user304_rsf8mD0BOQ_1 import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH = 800
HEIGHT = 600

class Obstacle:
    def __init__(self, pos, radius = 10):
        self.pos = pos
        self.vel = Vector()
        self.radius = max(radius, 10)
        self.IMG = None
        self.IMG_CENTRE = None
        self.IMG_DIMS = None
        self.img_dest_dim = None
        
    def draw(self, canvas):
        canvas.draw_image(self.IMG, self.IMG_CENTRE, self.IMG_DIMS, self.pos.get_p(), self.img_dest_dim)
        
class Moon(Obstacle):
    def __init__(self, pos, radius = 10):
        super().__init__(pos, radius = 10)
        self.IMG = simplegui.load_image('https://i.imgur.com/cuRu9OZ.png') #MOON
        self.IMG_CENTRE = (311,294)
        self.IMG_DIMS = (622,588)
        self.img_dest_dim = (100, 100)
        self.gravity = 0
        self.ALIVE = True
            
    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.85)
        self.vel.add(Vector(0, (self.gravity)))

    def getPos(self):
        return self.pos.get_p()

class Planet(Obstacle):
    def __init__(self, pos, radius = 10):
        super().__init__(pos, radius = 10)
        self.IMG = simplegui.load_image('https://i.imgur.com/nh8zRKw.png') #PLANET
        self.IMG_CENTRE = (273/2, 188/2)
        self.IMG_DIMS = (273, 188)
        self.img_dest_dim = (140, 100)

class Star(Obstacle):
    def __init__(self, pos, radius = 10):
        super().__init__(pos, radius = 10)
        self.IMG = simplegui.load_image('https://i.imgur.com/MsKwX7I.png ') #STAR
        self.IMG_CENTRE = (113/2, 112/2)
        self.IMG_DIMS = (113, 112)
        self.img_dest_dim = (58, 58)
        
class Cloud(Obstacle):
    def __init__(self, pos, radius = 10):
        super().__init__(pos, radius = 10)
        self.IMG = simplegui.load_image('https://i.imgur.com/hLxKYTT.png') #CLOUD
        self.IMG_CENTRE = (250/2, 127/2)
        self.IMG_DIMS = (250, 127)
        self.img_dest_dim = (108, 58)
        
class Alien(Obstacle):
    def __init__(self, pos, radius = 10):
        super().__init__(pos, radius = 10)
        self.IMG = simplegui.load_image('https://i.imgur.com/8OwD4yc.png') #ALIEN
        self.IMG_CENTRE = (229/2, 172/2)
        self.IMG_DIMS = (229, 172)
        self.img_dest_dim = (88, 48)

class Asteroid(Obstacle):
    def __init__(self, pos, radius = 10):
        super().__init__(pos, radius = 10)
        self.IMG = simplegui.load_image('https://i.imgur.com/SBgHMg9.png') #ASTEROID
        self.IMG_CENTRE = (156/2, 147/2)
        self.IMG_DIMS = (156, 147)
        self.img_dest_dim = (85, 60)

#class LevelHandler: #WIP
    #def __init__(self):
        #self.levelInstructions = #instruction screen
        #self.levelCongrats = #level complete screen
        #self.levelHolder = #array to store level objects??
        #self.levelBoundary = 5
        
    #def updateLevel(self,player):
        #display instructionscreen
        #if player.getStarCount == self.levelBoundary:
            #displaylevelCongrats.
            #updateLevel
            #self.levelBoundary+= 5 #need 5 stars to get to next lvl
        #in interaction class, if player.starlevel == x: grab new level from array and load
        
    #def draw(canvas):
        #draw currently loaded level onto screen.

class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.space = False
        self.m = False

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

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False
        if key == simplegui.KEY_MAP['up']:
            self.up = False
        if key == simplegui.KEY_MAP['space']:
            self.space = False
            
class ObstacleHandler:
    def __init__(self):
        self.updateCounter = False
        self.planetLimit = 1
        self.planets_list = [] 
        self.starLimit = 1
        self.star_list = []
        self.cloudLimit = 1
        self.cloud_list = []
        self.alienLimit = 1
        self.alien_list = []
        self.asteroidLimit = 1
        self.asteroid_list = []
    
    def spawn_planets(self):
        for i in range(0, self.planetLimit):
            self.vectorPosition = Vector(random.randrange(170, 600), random.randrange(100, 500))
            self.newPlanet = Planet(self.vectorPosition)
            self.add_planet(self.newPlanet)
       
    def add_planet(self,i):
        self.planets_list.append(i)
        
    def spawn_stars(self):
        for i in range(0, self.starLimit):
            self.vectorPosition = Vector(random.randrange(170, 600), random.randrange(100, 500))
            self.newStar = Star(self.vectorPosition)
            self.add_star(self.newStar)
     
    def add_star(self, i):
        self.star_list.append(i)
        
    def spawn_clouds(self):
        for i in range(0, self.cloudLimit):
            self.vectorPosition = Vector(random.randrange(170, 600), random.randrange(100, 500))
            self.newCloud = Cloud(self.vectorPosition)
            self.add_cloud(self.newCloud)
     
    def add_cloud(self, i):
        self.cloud_list.append(i)
        
    def spawn_aliens(self):
        for i in range(0, self.alienLimit):
            self.vectorPosition = Vector(random.randrange(170, 600), random.randrange(100, 500))
            self.newAlien = Alien(self.vectorPosition)
            self.add_alien(self.newAlien)
     
    def add_alien(self, i):
        self.alien_list.append(i)
        
    def spawn_asteroids(self):
        for i in range(0, self.asteroidLimit):
            self.vectorPosition = Vector(random.randrange(170, 600), random.randrange(100, 500))
            self.newAsteroid = Asteroid(self.vectorPosition)
            self.add_asteroids(self.newAsteroid)
     
    def add_asteroids(self, i):
        self.asteroid_list.append(i)
        
    def update(self):        
        self.spawn_planets()
        self.spawn_clouds()
        self.spawn_aliens()
        self.spawn_asteroids()
        self.spawn_stars()
        
    def draw(self, canvas):
        if self.updateCounter == False:
            self.update()
            self.updateCounter = True
        for planet in self.planets_list:
            planet.draw(canvas)
        for star in self.star_list:
            star.draw(canvas)
        for cloud in self.cloud_list:
            cloud.draw(canvas)
        for alien in self.alien_list:
            alien.draw(canvas)
        for asteroid in self.asteroid_list:
            asteroid.draw(canvas)
        
class Interaction:
    def __init__(self, wheel, keyboard):
        self.wheel = wheel
        self.keyboard = keyboard
        self.START = False

    def update(self):
        if self.START == True:
            self.keyboardinp()
            self.wheel.gravity = 1.25
            
    def introScreen(self, canvas):
        intro = simplegui.load_image('https://i.imgur.com/bdN3ctD.png')
        if self.keyboard.m == False:
            canvas.draw_image(intro, (1144/2, 719/2), (1144, 719), (400, 300), (850, 650))        

    def startgame(self):
        if self.keyboard.space == True:
            self.START = True

    def keyboardinp(self):
        if self.keyboard.right:
            self.wheel.vel.add(Vector(1, 0))
        if self.keyboard.left:
            self.wheel.vel.add(Vector(-1, 0))
        if self.keyboard.up:
            self.wheel.vel.add(Vector(0, (-3.5)))

kbd = Keyboard()
moon = Moon(Vector((WIDTH-745), (HEIGHT-530)), 40)
inter = Interaction(moon, kbd)
background_img = simplegui.load_image("https://i.imgur.com/j4yZLIh.png")
obstacle = ObstacleHandler()

#------------
#planet = Planet(Vector((WIDTH-600), (HEIGHT-200)), 40) ## test planet spawn
#star = Star(Vector((WIDTH-100), (HEIGHT-100)), 40) # stick this into obstacle handler - randomise pos
#cloud = Cloud(Vector((WIDTH-450), (HEIGHT-400)), 40) #in obstacke handler - random pos below planets
#alien = Alien(Vector((WIDTH-150), (HEIGHT-500)), 40) #in obstacle handler - coming from right edge in lvl 2&3 ?
#asteroid = Asteroid(Vector((WIDTH-250), (HEIGHT-250)), 40) #in obstacle handler - rotating in static pos ?
#------------

def draw(canvas):
    canvas.draw_image(background_img, (2057/2, 1442/2), (2057, 1442), (400, 300), (850, 650))
    obstacle.draw(canvas)
    inter.startgame()
    inter.update()
    moon.update()
    moon.draw(canvas)
    inter.introScreen(canvas)

nameInp = input("Welcome to HOPPY MOON! What is your name?")
frame = simplegui.create_frame('HOPPY MOON', WIDTH, HEIGHT)
label1 = frame.add_label('WELCOME TO HOPPY MOON '+ nameInp + "!")
label2 = frame.add_label('', 300)
label3 = frame.add_label('Instructions:')
label4 = frame.add_label('1. Use arrow keys to move.')
label5 = frame.add_label('2. Avoid the obstacles and collect stars to level up!', 200)
label6 = frame.add_label('3. Click spacebar to start.')

frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()
