import random
from user304_rsf8mD0BOQ_1 import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH = 800
HEIGHT = 600

class Obstacle:
    def __init__(self, pos):
        self.pos = pos
        self.vel = Vector()
        self.radius = None
        self.IMG = None
        self.IMG_CENTRE = None
        self.IMG_DIMS = None
        self.img_dest_dim = None
        
    def draw(self, canvas):
        canvas.draw_image(self.IMG, self.IMG_CENTRE, self.IMG_DIMS, self.pos.get_p(), self.img_dest_dim)
        
class Moon(Obstacle):
    def __init__(self, pos):
        super().__init__(pos)
        self.IMG = simplegui.load_image('https://i.imgur.com/cuRu9OZ.png') #MOON
        self.IMG_CENTRE = (311, 294)
        self.IMG_DIMS = (622, 588)
        self.img_dest_dim = (100, 100)
        self.gravity = 0
        self.ALIVE = True
        self.radius = 50   
        
    def update(self):
        if self.ALIVE == True:
            self.pos.add(self.vel)
            self.vel.multiply(0.85)
            self.vel.add(Vector(0, (self.gravity)))
        #if self.ALIVE == False:
        #print("Your dead")
            
    def getPos(self):
        return self.pos.get_p()
    
    def offset_d(self):
        return self.pos.y - self.radius

class Planet(Obstacle):
    def __init__(self, pos):
        super().__init__(pos)
        self.IMG = simplegui.load_image('https://i.imgur.com/nh8zRKw.png') #PLANET
        self.IMG_CENTRE = (273/2, 188/2)
        self.IMG_DIMS = (273, 188)
        self.img_dest_dim = (112, 80)
        self.radius = 56

class Star(Obstacle):
    def __init__(self, pos):
        super().__init__(pos)
        self.IMG = simplegui.load_image('https://i.imgur.com/MsKwX7I.png ') #STAR
        self.IMG_CENTRE = (113/2, 112/2)
        self.IMG_DIMS = (113, 112)
        self.img_dest_dim = (46, 46)
        self.radius = 23
        
class Cloud(Obstacle):
    def __init__(self, pos):
        super().__init__(pos)
        self.IMG = simplegui.load_image('https://i.imgur.com/hLxKYTT.png') #CLOUD
        self.IMG_CENTRE = (250/2, 127/2)
        self.IMG_DIMS = (250, 127)
        self.img_dest_dim = (86, 46)
        self.radius = 25   
        
class Alien(Obstacle):
    def __init__(self, pos):
        super().__init__(pos)
        self.IMG = simplegui.load_image('https://i.imgur.com/8OwD4yc.png') #ALIEN
        self.IMG_CENTRE = (229/2, 172/2)
        self.IMG_DIMS = (229, 172)
        self.img_dest_dim = (88, 48)
        self.radius = 35   

class Asteroid(Obstacle):
    def __init__(self, pos):
        super().__init__(pos)
        self.IMG = simplegui.load_image('https://i.imgur.com/SBgHMg9.png') #ASTEROID
        self.IMG_CENTRE = (156/2, 147/2)
        self.IMG_DIMS = (156, 147)
        self.img_dest_dim = (68, 48)
        self.radius = 25
        
class Wall(Obstacle):
    def __init__(self, x, y, border, colour):
        self.y = y
        self.border = border
        self.colour = colour
        self.normal = Vector(1, 0)
        self.edge = y + border
        
    def draw(self, canvas):
        canvas.draw_line((0, self.y),
                         (WIDTH, self.y),
                         (2 * self.border + 1),
                         self.colour)
        
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
        self.starRemoval = []
        self.lives = []
        self.walls = []
        
    def spawn_planets(self):
        for i in range(0, self.planetLimit):
            self.vectorPosition = Vector(random.randrange(170, 250), random.randrange(100, 500))
            self.newPlanet = Planet(self.vectorPosition)
            self.add_planet(self.newPlanet)
       
    def add_planet(self,i):
        self.planets_list.append(i)
        
    def spawn_stars(self):
        for i in range(0, self.starLimit):
            self.vectorPosition = Vector(random.randrange(100, 750), random.randrange(50, 550))
            self.newStar = Star(self.vectorPosition)
            self.add_star(self.newStar)
            
    def spawnSingleStar(self):
            self.vectorPosition = Vector(random.randrange(100, 750), random.randrange(50, 550))
            self.newStar = Star(self.vectorPosition)
            self.add_star(self.newStar) 
            
    def add_star(self, i):
        self.star_list.append(i)
        
    def spawn_clouds(self):
        for i in range(0, self.cloudLimit):
            self.vectorPosition = Vector(random.randrange(300, 450), random.randrange(100, 500))
            self.newCloud = Cloud(self.vectorPosition)
            self.add_cloud(self.newCloud)
     
    def add_cloud(self, i):
        self.cloud_list.append(i)
        
    def spawn_aliens(self):
        for i in range(0, self.alienLimit):
            self.vectorPosition = Vector(random.randrange(700, 750), random.randrange(100, 500))
            self.newAlien = Alien(self.vectorPosition)
            self.add_alien(self.newAlien)
     
    def add_alien(self, i):
        self.alien_list.append(i)
        
    def spawn_asteroids(self):
        for i in range(0, self.asteroidLimit):
            self.vectorPosition = Vector(random.randrange(500, 650), random.randrange(100, 500))
            self.newAsteroid = Asteroid(self.vectorPosition)
            self.add_asteroids(self.newAsteroid)
     
    def add_asteroids(self, i):
        self.asteroid_list.append(i)
        
    def starRemover(self, i):
        for k in self.star_list:
            if k == i:
                self.star_list.remove(k)
    
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
    def __init__(self,kbd):
        self.kbd = kbd
        self.moon = Moon(Vector((WIDTH-745), (HEIGHT-530)))
        self.background_img = simplegui.load_image("https://i.imgur.com/xOaLyeq.png") #("https://i.imgur.com/j4yZLIh.png") - Old Background
        self.gameover = simplegui.load_image("https://i.imgur.com/T5dL54b.png")
        self.obstacle = ObstacleHandler()
        self.START = False
        self.score = 0
        self.lives = 100
        self.wall = Wall(20, 800, 5, 'Red')
        
    def update(self):
        if self.START == True:
            self.keyboardinp()
            self.moon.gravity = 1
            self.count = 0
            for i in self.obstacle.planets_list:
                if self.hit(self.moon, i):
                    self.lives -= 0.5
            for i in self.obstacle.cloud_list:
                if self.hit(self.moon, i):
                    self.lives -= 0.5
            for i in self.obstacle.alien_list:
                if self.hit(self.moon, i):
                    self.lives -= 0.5
            for i in self.obstacle.asteroid_list:
                if self.hit(self.moon, i):
                    self.lives -= 0.5
            for i in self.obstacle.star_list:
                count = 0
                if self.hit(self.moon, i):
                    self.score += 1
                    self.obstacle.starRemover(i)
                    self.obstacle.spawnSingleStar()
            if self.lives <= 0:
                self.moon.ALIVE = False
            elif self.hit_wall(self.moon, self.wall):
                self.moon.ALIVE = False
                    
                #if count % 300 and self.obstacle.star_list.size() >= 1:
                 #   self.obstacle.starRemover(i)
                  #  self.obstacle.spawnStars()
            #if  self.count % 1000 == 0:
            #    for i in self.obstacle.star_list:
            #        i.pos = Vector(random.randrange(170, 750), random.randrange(100, 500))
            #else:
            #    pass
            #
            #self.count += 1
            
    def introScreen(self, canvas):
        intro = simplegui.load_image('https://i.imgur.com/DOKJ3eO.png')
        if self.kbd.m == False:
            canvas.draw_image(intro, (1144/2, 719/2), (1144, 719), (400, 300), (850, 650))
    
    def hit(self, b1, b2):
        sep_vec = b1.pos.copy().subtract(b2.pos)
        return sep_vec.length() < b1.radius + b2.radius
        #offset1 = b1.pos + b1.radius
        #return b1.pos + b1.radius >= b2.pos+b2.radius or b1.pos + b1.radius <= b2.pos-b2.radius
        
    def hit_wall(self, m1, wall):
         return m1.offset_d() >= self.wall.edge
    
    def startgame(self):
        if self.kbd.space == True:
            self.START = True
            
    def tick(self):
        for i in self.obstacle.star_list:
            i.pos = Vector(random.randrange(170, 600), random.randrange(100, 500))
         
    def keyboardinp(self):
        if self.kbd.right:
            self.moon.vel.add(Vector(1, 0))
        if self.kbd.left:
            self.moon.vel.add(Vector(-1, 0))
        if self.kbd.up:
            self.moon.vel.add(Vector(0, (-3.5)))
                
    def draw(self,canvas):
        self.gameoverscreen = canvas.draw_image(self.gameover, (1144/2, 719/2), (1144, 719), (400, 300), (850, 650))
        if self.moon.ALIVE == True:
            canvas.draw_image(self.background_img, (1564/2, 1123/2), (1564, 1123), (400, 300), (900, 700))
            self.startgame()
            self.obstacle.draw(canvas)
            self.update()
            self.moon.update()
            self.moon.draw(canvas)
            self.wall.draw(canvas)
            canvas.draw_text("START", (10, 25), 25, 'White', 'sans-serif')
            canvas.draw_text("Stars: %s" % self.score, (690, 25), 23, 'White', 'sans-serif')
            canvas.draw_text("Health: %s" % self.lives, (690, 50), 20, 'Red', 'sans-serif')
            self.introScreen(canvas)
        else:
            self.gameoverscreen
            canvas.draw_text("Total Stars: %s" % self.score, (350, 475), 20, 'White', 'sans-serif')

interval = 5000
kbd = Keyboard()
interaction = Interaction(kbd)
#nameInp = input("Welcome to HOPPY MOON! What is your name?")
frame = simplegui.create_frame('HOPPY MOON', WIDTH, HEIGHT)

timer = simplegui.create_timer(interval, interaction.tick)
frame.set_draw_handler(interaction.draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()
timer.start()
