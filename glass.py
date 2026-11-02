from pico2d import get_canvas_width, get_time, load_image
import game_world

class grass:
    def __init__(self):
        self.image = load_image('animation_sheet.png')
        self.layer = 0
    
