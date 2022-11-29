class Path:
    def __init__(self):
        pass
    
    def right(self, rad, distance):
        import turtle
        t = turtle.Turtle()
        rad += 90
        t.right(rad)
        t.forward(distance)
        return rad
        
    def slight_right(self, rad, distance):
        import turtle
        t = turtle.Turtle()
        rad += 45
        t.right(rad)
        return rad

    def left(self, rad, distance):
        import turtle
        t = turtle.Turtle()
        rad += 90
        t.left(rad)
        t.forward(distance)
        return rad

    def forward(self, distance):
        import turtle
        t = turtle.Turtle()
        t.forward(distance)
    