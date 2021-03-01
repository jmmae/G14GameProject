#Task 5/6 - sprite.py - PROTOTYPE

from user304_rsf8mD0BOQ_1 import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH = 500
HEIGHT = 500
                
class Wheel:
    def __init__(self, pos, radius = 10):
        self.pos = pos
        self.vel = Vector()
        self.radius = max(radius, 10)
        self.IMG = simplegui.load_image('https://i.imgur.com/cuRu9OZ.png')
        self.IMG_CENTRE = (311,294)
        self.IMG_DIMS = (622,588)
        self.img_dest_dim = (128,128)
        self.img_rot = 0
        self.step = 0.5
        self.gravity = 0.1
        
    def draw(self, canvas):
        canvas.draw_image(self.IMG, self.IMG_CENTRE, self.IMG_DIMS, self.pos.get_p(), self.img_dest_dim, self.img_rot) 
        
    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.85)
        if self.pos.get_p() > (WIDTH, 0):
            self.pos = Vector(0, HEIGHT-65)
        elif self.pos.get_p() < (0, 0):
            self.pos = Vector(WIDTH, HEIGHT-65)
            
    def getPos(self):
        return self.pos.get_p()
    
class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down=False
    
    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        if key == simplegui.KEY_MAP['left']:    
            self.left = True
        if key == simplegui.KEY_MAP['up']:    
            self.up = True
            self.down = False
        
    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:    
            self.left = False
        if key == simplegui.KEY_MAP['up']:    
            self.up = False
            self.down = True
        
class Interaction:
    def __init__(self, wheel, keyboard):
        self.wheel = wheel
        self.keyboard = keyboard
        self.flagjump_up = True 
        self.flagjump_down = False
        
    def update(self):
        self.flagjump_up = True 
        self.flagjump_down = False
        if self.keyboard.right:
            self.wheel.vel.add(Vector(1, 0))
            self.wheel.img_rot -= self.wheel.step
        if self.keyboard.left:
            self.wheel.vel.add(Vector(-1, 0))
            self.wheel.img_rot += self.wheel.step
        if self.keyboard.up:
            self.wheel.vel.add(Vector(0, (-2)))# -1 + gravity
        if self.keyboard.down:
            self.wheel.vel.add(Vector(0, (2)))# +1 + gravity
            if self.wheel.pos.get_p()[1] < 490: 
                self.keyboard.keyUp.down = False
                  
kbd = Keyboard()
wheel = Wheel(Vector(WIDTH/2, HEIGHT-65), 40)
inter = Interaction(wheel, kbd)

def draw(canvas):
    inter.update()
    wheel.update()
    wheel.draw(canvas)
    
frame = simplegui.create_frame('Interactions', WIDTH, HEIGHT)
frame.set_canvas_background('#000000')
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()

