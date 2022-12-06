import turtle as t

yes_or_no = False
Loop = False


def initialize():
    ''' Sets turtle settings to desired settings
    Worked on by Collin Alexander, collinjalex@tamu.edu'''
    t.screensize(canvwidth=750, canvheight=750, bg="#a1cfae")
    #screen = t.Screen()
    #screen.setup(width = 1.0, height = 1.0)
    t.shape("circle")
    t.width(width=2)
    t.pensize(width=2)
    t.color("#3c8051")
    t.fillcolor("#52a36b")
    t.shapesize(.2, .2)


def stamp_circle():
    '''Worked on by Collin Alexander, collinjalex@tamu.edu'''
    t.width(width=2)
    t.pensize(width=2)
    t.color("#3c8051")
    t.fillcolor("#3c8051")
    t.stamp()

    # fixing back to normal
    t.fillcolor("#52a36b")
    t.width(width=2)
    t.pensize(width=2)


def draw_rectangle(length1,length2):
    ''' Creates a filled rectangle, parameters are length1 and length2
    Worked on by Gretta Weich, gretkatwei@tamu.edu'''
    t.begin_fill()
    t.forward(length1)
    t.left(90)
    t.forward(length2)
    t.left(90)
    t.forward(length1)
    t.left(90)
    t.forward(length2)
    t.left(90)
    t.end_fill()


def position(x, y):
    '''sets the position of turtle, parameters are desired x and y position
    Worked on by Ashley Brown, ashbrown@tamu.edu'''
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()


def gui_main():
    '''loads up the gui
    Worked on by Ashley Brown, ashbrown@tamu.edu'''
    t.speed(0)
    # title
    position(0, 200)
    t.write("Map Generator",
            move=False,
            align="center",
            font=("Fixedsys", 150, "bold"))

    # exit program button
    position(-400, -300)
    draw_rectangle(900, 150)
    position(0, -275)
    t.write("Exit Program",
            move=False,
            align="center",
            font=("Fixedsys", 75, "normal"))

    # generate map button
    position(-400, 0)
    draw_rectangle(900, 150)
    position(0, 25)
    t.write("Generate Map",
            move=False,
            align="center",
            font=("Fixedsys", 75, "normal"))

def write_directions(direct):
    angle = t.heading()
    t.setheading(0)
    t.speed(0)
    currentpos = t.pos()
    position(-800,-450)
    draw_rectangle(3000, 100)
    position(0,-400)
    t.write(direct, move=False, align="center", font=("Fixedsys", 12, "normal"))
    position(currentpos[0], currentpos[1])
    t.speed(1)
    t.setheading(angle)

def create_map():
    '''Worked on by Gretta Weich, gretkatwei@tamu.edu'''
    position(0,350)
    t.write(filename, move=False, align="center", font=("Fixedsys", 55, "normal"))
    position(0, 0)
    t.write("Start", move=False, align="center", font=("Fixedsys", 5, "bold"))
    for direct in eachdirect:
        write_directions(direct)
        if ' min ' in direct:
            nummi = direct.split('(')
            nummiles = nummi[1].split()
            miles = float(nummiles[0])
            feet = miles * 5280
            units = feet / 50
        elif ' ft' in direct:
            if '(' in direct:
                numfeet = direct.split('(')
                numfeet2 = numfeet[1].split()
                feet = int(str(numfeet2[0]))
                units = feet / 50
            else:
                directsplit = direct.split()
                feet = int(directsplit[-2])
                units = feet / 50
        else:
            directsplit = direct.split()
            miles = float(directsplit[-2])
            feet = miles * 5280
            units = feet / 50
        if 'Head' in direct:
            if ' east' in direct:
                t.left(0)
            elif 'northeast' in direct:
                t.left(45)
            elif 'north ' in direct:
                t.left(90)
            elif 'northwest' in direct:
                t.left(135)
            elif ' west' in direct:
                t.left(180)
            elif 'southwest' in direct:
                t.left(225)
            elif 'south ' in direct:
                t.left(270)
            else:
                t.left(315)
        if 'Turn right' in direct:
            t.right(90)
            stamp_circle()
            t.forward(units)
        if 'Slight right' in direct:
            t.right(45)
            stamp_circle()
            t.forward(units)
        if 'Turn left' in direct:
            t.left(90)
            stamp_circle()
            t.forward(units)
        if 'Slight left' in direct:
            t.left(45)
            stamp_circle()
            t.forward(units)
        if 'Continue' in direct:
            if 'and' not in direct:
                t.forward(units)  # will need distance based on conversions and such
            else:
                pass  # harcode

        if 'Drive' in direct:
            if 'and' in direct:
                pass  # harcode
            elif 'Crow' in direct:
                pass
            else:
                t.forward(
                    units)  # will need distance based on conversions and such
        if 'Take' in direct:
            t.forward(
                units)  # will need distance based on conversions and such
        if 'Pass' in direct:
            pass
    t.write("End", move=False, align="center", font=("Fixedsys", 5, "bold"))
    # resetting turtle
    t.speed(6)


def read_file(filename):
    '''Worked on by Connor McGuire, connormcguire02@tamu.edu'''
    global directions
    directions = open(filename, 'r+')
    global read
    read = directions.read()
    global eachdirect
    eachdirect = read.split('\n\n')


def button_click(x, y):
    '''Worked on by Connor McGuire, connormcguire02@tamu.edu'''
    if (y >= 0 and y <= 150):
        global filename
        global yes_or_no
        yes_or_no = True
        filename = t.textinput("Text File", "Enter a Text File")
        global Loop
        Loop = True
        t.clear()
        read_file(filename)
        create_map()
    if (y >= -300 and y <= -150):
        t.bye()


initialize()
gui_main()
t.onscreenclick(button_click)
'''directions = open(filename, 'r+')
read = directions.read()
eachdirect = read.split('\n\n')
print(eachdirect)
print("it worked again!")'''

t.done()
