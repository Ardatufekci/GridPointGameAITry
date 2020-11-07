class Filler:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
    def draw(self,can):
        can.create_rectangle(self.x, self.y, self.x + 64, self.y + 64, fill=self.color)
