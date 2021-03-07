from user304_rsf8mD0BOQ_1 import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH = 800
HEIGHT = 600

class Wheel:
    def __init__(self, pos, radius = 10):
        self.pos = pos
        self.vel = Vector()
        self.radius = max(radius, 10)
        self.IMG = simplegui.load_image('https://i.imgur.com/cuRu9OZ.png') #MOON
        self.IMG_CENTRE = (311,294)
        self.IMG_DIMS = (622,588)
        self.img_dest_dim = (100, 100)
        self.gravity = 0

    def draw(self, canvas):
        canvas.draw_image(self.IMG, self.IMG_CENTRE, self.IMG_DIMS, self.pos.get_p(), self.img_dest_dim)

    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.85)
        self.vel.add(Vector(0, (self.gravity)))

    def getPos(self):
        return self.pos.get_p()

class Planet: #WIP
    def __init__(self, pos, radius = 10):
        self.pos = pos
        self.vel = Vector()
        self.radius = max(radius, 10)
        self.IMG = simplegui.load_image('https://i.imgur.com/nh8zRKw.png') #PLANET
        self.IMG_CENTRE = (273/2, 188/2)
        self.IMG_DIMS = (273, 188)
        self.img_dest_dim = (165, 128)

    def draw(self, canvas):
        canvas.draw_image(self.IMG, self.IMG_CENTRE, self.IMG_DIMS, self.pos.get_p(), self.img_dest_dim)

class Star: #WIP
    def __init__(self, pos, radius = 10):
        self.pos = pos
        self.vel = Vector()
        self.radius = max(radius, 10)
        self.IMG = simplegui.load_image('https://i.imgur.com/MsKwX7I.png ') #STAR
        self.IMG_CENTRE = (113/2, 112/2)
        self.IMG_DIMS = (113, 112)
        self.img_dest_dim = (58, 58)

    def draw(self, canvas):
        canvas.draw_image(self.IMG, self.IMG_CENTRE, self.IMG_DIMS, self.pos.get_p(), self.img_dest_dim)
        
class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down=False
        self.space = False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        if key == simplegui.KEY_MAP['left']:
            self.left = True
        if key == simplegui.KEY_MAP['up']:
            self.up = True
        if key == simplegui.KEY_MAP['space']:
            self.space = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False
        if key == simplegui.KEY_MAP['up']:
            self.up = False
        if key == simplegui.KEY_MAP['space']:
            self.space = False

class Interaction:
    def __init__(self, wheel, keyboard):
        self.wheel = wheel
        self.keyboard = keyboard
        self.START = False

    def update(self):
        if self.START == True:
            self.keyboardinp()
            self.wheel.gravity = 1.5

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
wheel = Wheel(Vector((WIDTH-745), (HEIGHT-530)), 40)
inter = Interaction(wheel, kbd)
planet = Planet(Vector((WIDTH-400), (HEIGHT-400)), 40) ## test planet spawn
background_img = simplegui.load_image("https://i.imgur.com/j4yZLIh.png")

def draw(canvas):
    canvas.draw_image(background_img, (2057/2, 1442/2), (2057, 1442), (400, 300), (850, 650))
    inter.startgame()
    inter.update()
    wheel.update()
    wheel.draw(canvas)
    planet.draw(canvas)

frame = simplegui.create_frame('HOPPY MOON', WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()
