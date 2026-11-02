from pico2d import load_image


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        self.layer = 0

    def draw(self,x,y,layer = 0):
        self.image.draw(x, y)
        self.image.draw(layer)

    def update(self):
        pass
