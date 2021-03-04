from user304_rsf8mD0BOQ_1 import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
class UFO:
    def __init__(self):
        self.vector = Vector()
        self.IMG = simplegui.load_image()#imgur url

    def draw(self):
        canvas.draw_image(self.IMG, self.IMG_CENTRE, self.IMG_DIMS, self.pos.get_p(), self.img_dest_dim, self.img_rot)

    def update(self):
        None
    def get_p(self):
        return self.pos.get_p()
