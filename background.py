from user304_rsf8mD0BOQ_1 import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    
canvas_width = 800
canvas_height = 600

background_img = simplegui.load_image("https://i.imgur.com/j4yZLIh.png")

def draw(canvas):
    canvas.draw_image(background_img, (2057/2, 1442/2), (2057, 1442), (400, 300), (850, 650))
    
frame = simplegui.create_frame("Backgrounds", canvas_width, canvas_height)
frame.set_draw_handler(draw)
frame.start()
