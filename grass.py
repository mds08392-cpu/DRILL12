from pico2d import load_image


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def setPos(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        pass
