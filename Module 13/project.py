import turtle

class Path(turtle.Turtle):
    def __init__(self):
        pass
    
    def right(self, deg):
        super().right(deg)

    def slight_right(self):
        super().right(45)

    def slight_left(self):
        super().left(45)

    def left(self, deg):
        super().left(deg)

    def forward(self, distance):
        super.forward(distance)
    
    def direction(self):
        super.heading()
    
    def east():
        super.left(0-super.heading())
    
    def northEast():
        super.left(45-super.heading())
    
    def north():
        super.left(90-super.heading())
    
    def northWest():
        super.left(135-super.heading())
    
    def west():
        super.left(180-super.heading())
    
    def southWest():
        super.left(225-super.heading())
    
    def south():
        super.left(270-super.heading())
    
    def southEast():
        super.left(315-super.heading())

if __name__=='__main__':
    from math import pi
    pth = Path(pi, 5)
    pth.set_distance(10)

    