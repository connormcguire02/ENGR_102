import turtle
class Path(turtle.Turtle):
    def __init__(self):
        self.t = self.turtle.Turtle()
    
    def right(self, deg, distance):
        deg += 90
        Path.t.right(deg)
        Path.t.forward(distance)
        input()
        return deg

    def slight_right(self, deg, distance):
        deg += 45
        Path.t.right(deg)
        Path.t.forward(distance)
        input()
        return deg

    def slight_left(self, deg, distance):
        deg += 45
        Path.t.left(deg)
        Path.t.forward(distance)
        input()
        return deg

    def left(self, deg, distance):
        deg += 90
        Path.t.left(deg)
        Path.t.forward(distance)
        input()
        return deg

    def forward(self, distance):
        Path.t.forward(distance)
        input()
    
    def direction(self):
        pass
if __name__=='__main__':
    from math import pi
    pth = Path(pi, 5)
    pth.set_distance(10)

    