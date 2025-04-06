import turtle
import time
import cv2
import numpy as np

turtle.colormode(255)
turtle.getscreen()
screen = turtle.Screen()
screen.clear()

screen.bgcolor("#0A0A0A")
screen.tracer(0)
screen.screensize(900, 900)
screen.setup(900, 900)


t = turtle.Turtle()
t.hideturtle()
t.pensize(1)
# FROM HERE TO DOWN THERE, CHATGPT HELPED A LOT


def draw(water, body1, shading2):
    # Swans
    # Load and preprocess image
    image = cv2.imread(body1)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Scales to 900x900
    def scale_points(contours, width=900, height=900):
        points = []
        for contour in contours:
            for point in contour:
                x, y = point[0]
                # Flip y and center (turtle uses center as (0,0))
                new_x = x - width // 2
                new_y = height // 2 - y
                points.append((new_x, new_y))
        return points

    points = scale_points(contours)

    for contour in contours:
        t.penup()

        # Move to the first point in the contour
        first_point = contour[0][0]
        x, y = first_point
        new_x = x - 450
        new_y = 450 - y
        t.goto(new_x, new_y)
        t.begin_fill()
        t.pendown()

        # Draw the rest of the contour
        for point in contour[1:]:
            x, y = point[0]
            new_x = x - 450
            new_y = 450 - y
            t.goto(new_x, new_y)

        # trying to make a shape so i can use fill
        first_point = contour[0][0]
        x, y = first_point
        new_x = x - 452
        new_y = 452 - y
        t.goto(new_x, new_y)

        for point in contour[1:]:
            x, y = point[0]
            new_x = x - 452
            new_y = 452 - y
            t.goto(new_x, new_y)
        t.end_fill()
        t.penup()  # Important: lift pen after each contour

    # Load and preprocess image
    image = cv2.imread(shading2)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Scales to 900x900
    def scale_points(contours, width=900, height=900):
        points = []
        for contour in contours:
            for point in contour:
                x, y = point[0]
                # Flip y and center (turtle uses center as (0,0))
                new_x = x - width // 2
                new_y = height // 2 - y
                points.append((new_x, new_y))
        return points

    points = scale_points(contours)

    for contour in contours:
        t.penup()

        # Move to the first point in the contour
        first_point = contour[0][0]
        x, y = first_point
        new_x = x - 450
        new_y = 450 - y
        t.goto(new_x, new_y)
        t.begin_fill()
        t.pendown()

        # Draw the rest of the contour
        for point in contour[1:]:
            x, y = point[0]
            new_x = x - 450
            new_y = 450 - y
            t.goto(new_x, new_y)

        # trying to make a shape so i can use fill
        first_point = contour[0][0]
        x, y = first_point
        new_x = x - 452
        new_y = 452 - y
        t.goto(new_x, new_y)

        for point in contour[1:]:
            x, y = point[0]
            new_x = x - 452
            new_y = 452 - y
            t.goto(new_x, new_y)
        t.end_fill()
        t.penup()  # Important: lift pen after each contour

    # Lake
    # Load and preprocess image
    image = cv2.imread(water)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Scales to 900x900
    def scale_points(contours, width=900, height=900):
        points = []
        for contour in contours:
            for point in contour:
                x, y = point[0]
                # Flip y and center (turtle uses center as (0,0))
                new_x = x - width // 2
                new_y = height // 2 - y
                points.append((new_x, new_y))
        return points

    points = scale_points(contours)

    for contour in contours:
        t.penup()

        # Move to the first point in the contour
        first_point = contour[0][0]
        x, y = first_point
        new_x = x - 450
        new_y = 450 - y
        t.goto(new_x, new_y)
        t.begin_fill()
        t.pendown()

        # Draw the rest of the contour
        for point in contour[1:]:
            x, y = point[0]
            new_x = x - 450
            new_y = 450 - y
            t.goto(new_x, new_y)
        t.end_fill()
        t.penup()  # Important: lift pen after each contour

# DOWN HERE

def draw_simple(water, body1, shading2):
    # Swans
    # Load and preprocess image
    image = cv2.imread(body1)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Scales to 900x900
    def scale_points(contours, width=900, height=900):
        points = []
        for contour in contours:
            for point in contour:
                x, y = point[0]
                # Flip y and center (turtle uses center as (0,0))
                new_x = x - width // 2
                new_y = height // 2 - y
                points.append((new_x, new_y))
        return points

    points = scale_points(contours)

    for contour in contours:
        t.penup()

        # Move to the first point in the contour
        first_point = contour[0][0]
        x, y = first_point
        new_x = x - 450
        new_y = 450 - y
        t.goto(new_x, new_y)
        t.pendown()

        # Draw the rest of the contour
        for point in contour[1:]:
            x, y = point[0]
            new_x = x - 450
            new_y = 450 - y
            t.goto(new_x, new_y)
        t.penup()  # Important: lift pen after each contour

    # Load and preprocess image
    image = cv2.imread(shading2)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Scales to 900x900
    def scale_points(contours, width=900, height=900):
        points = []
        for contour in contours:
            for point in contour:
                x, y = point[0]
                # Flip y and center (turtle uses center as (0,0))
                new_x = x - width // 2
                new_y = height // 2 - y
                points.append((new_x, new_y))
        return points

    points = scale_points(contours)

    for contour in contours:
        t.penup()

        # Move to the first point in the contour
        first_point = contour[0][0]
        x, y = first_point
        new_x = x - 450
        new_y = 450 - y
        t.goto(new_x, new_y)
        t.pendown()

        # Draw the rest of the contour
        for point in contour[1:]:
            x, y = point[0]
            new_x = x - 450
            new_y = 450 - y
            t.goto(new_x, new_y)

        t.penup()  # Important: lift pen after each contour

    # Lake
    # Load and preprocess image
    image = cv2.imread(water)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Scales to 900x900
    def scale_points(contours, width=900, height=900):
        points = []
        for contour in contours:
            for point in contour:
                x, y = point[0]
                # Flip y and center (turtle uses center as (0,0))
                new_x = x - width // 2
                new_y = height // 2 - y
                points.append((new_x, new_y))
        return points

    points = scale_points(contours)

    for contour in contours:
        t.penup()

        # Move to the first point in the contour
        first_point = contour[0][0]
        x, y = first_point
        new_x = x - 450
        new_y = 450 - y
        t.goto(new_x, new_y)
        t.pendown()

        # Draw the rest of the contour
        for point in contour[1:]:
            x, y = point[0]
            new_x = x - 450
            new_y = 450 - y
            t.goto(new_x, new_y)
        t.penup()  # Important: lift pen after each contour

def tcolor(color):
    t.color(color)
    t.pencolor(color)
    t.fillcolor(color)

def wait(seconds):
    start = time.time()
    while time.time() - start < seconds:
        turtle.update()  # Keeps the window responsive



def get_color_at_position():
    # Get turtle position and screen coordinates
    c = turtle.Screen().getcanvas()
    x, y = t.position()
    items = c.find_overlapping(x, -y, x, -y) # omg its working
    if len(items) > 0:
        coloratpixel = c.itemcget(items[-1], "fill")
        return coloratpixel
    else:
        return "1, 1, 1"  # Return fallback color, is background color
def draw_or_not():
    color_beneath = get_color_at_position()
    if color_beneath == "black":
        t.pendown()
    else:
        t.penup()
def bg_lines():
    t.pencolor("#0A0A0A")
    for i in range(200):
        t.penup()
        t.setposition(-450,300-3*i)
        t.pendown()
        t.forward(900)
        t.setposition(-450, 301-3*i)
        t.forward(900)


def frame(water, body1, shading2):
    t.clear()
    t.pencolor("white")
    t.pensize(2)
    draw_simple(water, body1, shading2)
    t.pensize(1)
    bg_lines()
    screen.update()
    wait(0.2)


t.pencolor("black")
draw("images/lake_final.png","images/final_swans.png", "images/swans_shading.png")
screen.update()

t.pencolor("white")
for i in range(100):
    t.penup()
    t.setposition(-450, 150-3*i)
    for i in range(900):
        draw_or_not()
        t.forward(1)
    screen.update()
    wait(0.1)
wait(2)
t.clear()




frame("images/One.png","images/One 1.png", "images/One 2.png")
wait(1)
frame("images/Two.png","images/Two 1.png","images/Two 2.png")
frame("images/Three.png","images/Three 1.png","images/Three 2.png")
frame("images/Four.png","images/Four 1.png", "images/Four 2.png")
frame("images/Five.png","images/Five 1.png", "images/Five 2.png")
frame("images/Six.png","images/Six 1.png", "images/Six 2.png")
frame("images/Seven.png","images/Seven 1.png", "images/Seven 2.png")
frame("images/Eight.png","images/Eight 1.png", "images/Eight 2.png")
frame("images/Nine.png","images/Nine 1.png", "images/Nine 2.png")
frame("images/Ten.png","images/Ten 1.png", "images/Ten 2.png")
frame("images/Eleven.png","images/Eleven 1.png", "images/Eleven 2.png")
frame("images/Twelve.png","images/Twelve 1.png", "images/Twelve 2.png")
frame("images/Thirteen.png","images/Thirteen 1.png", "images/Thirteen.png")
frame("images/Fourteen.png","images/Fourteen 1.png", "images/Fourteen.png")

frame("images/Fifteen.png","images/Fifteen.png", "images/Fifteen.png")


for i in range(20):
    t.clear()
    t.pencolor("white")
    # Load and preprocess image
    image = cv2.imread("images/Fifteen.png")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Scales to 900x900
    def scale_points(contours, width=900, height=900):
        points = []
        for contour in contours:
            for point in contour:
                x, y = point[0]
                # Flip y and center (turtle uses center as (0,0))
                new_x = x - width // 2
                new_y = height // 2 - y
                points.append((new_x, new_y))
        return points

    points = scale_points(contours)

    for contour in contours:
        t.penup()

        # Move to the first point in the contour
        first_point = contour[0][0]
        x, y = first_point
        new_x = x - 450
        new_y = 450 - y
        t.goto(new_x, new_y+40*i)
        t.pendown()

        # Draw the rest of the contour
        for point in contour[1:]:
            x, y = point[0]
            new_x = x - 450
            new_y = 450 - y
            t.goto(new_x, new_y+40*i)
        t.penup()  # Important: lift pen after each contour

    bg_lines()
    screen.update()
    wait(0.1)


def shell_things():
    t.setx(-450)
    for i in range(8):
        t.begin_fill()
        t.circle(60)
        t.end_fill()
        t.forward(120)

t.pensize(10)
for i in range(200):
    tcolor("#021012")
    t.penup()
    t.setposition(-450, -450+10*i)
    t.pendown()
    shell_things()
    tcolor("#03131a")
    t.penup()
    t.setposition(-450, -600+10*i)
    t.pendown()
    shell_things()
    tcolor("#04141f")
    t.penup()
    t.setposition(-450, -750+10*i)
    t.pendown()
    shell_things()
    tcolor("#051e26")
    t.penup()
    t.setposition(-450, -900+10*i)
    t.pendown()
    shell_things()
    tcolor("#082937")
    t.penup()
    t.setposition(-450, -1050+10*i)
    t.pendown()
    shell_things()
    screen.update()
    wait(0.01)


# delete this later
screen.bgcolor("#082937")
t.penup()
t.setposition(0,0)
screen.tracer(1)
t.speed(0)


t.pensize(3)


t.pencolor("white")
def B():
    t.left(180)
    t.pendown()
    t.circle(20,90)
    t.forward(100)
    t.circle(20,90)
    t.forward(20)
    t.circle(40,160)
    t.right(140)
    t.circle(33,162)
    t.forward(20)
    t.left(88)
    t.penup()
    t.forward(33)
    t.left(90)
    t.forward(10)
    t.pendown()
    t.circle(10,70)
    t.circle(10,-70)
    t.circle(-10,70)
    t.right(20)
    t.penup()
    t.forward(50)
    t.right(20)
    t.pendown()
    t.circle(-10,70)
    t.right(180)
    t.circle(-10,70)
    t.right(200)
    t.penup()
    t.forward(30)
    t.right(90)
    t.forward(10)
    t.right(25)
    t.pendown()
    t.circle(-33,30)
    t.circle(-33,-30)
    t.penup()
    t.left(115)
    t.forward(65)
    t.right(115)
    t.pendown()
    t.circle(-33,30)


def L():
    t.left(180)
    t.pendown()
    t.circle(20,90)
    t.forward(100)
    t.circle(20,90)
    t.forward(50)
    t.circle(20,180)
    t.forward(30)
    t.right(90)
    t.forward(80)
    t.circle(20,90)
    t.penup()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.pendown()
    t.circle(10,-90)
    t.right(180)
    t.penup()
    t.forward(90)
    t.left(90)
    t.forward(40)
    t.pendown()
    t.circle(-10,90)


def H():
    t.left(180)
    t.pendown()
    t.circle(20,90)
    t.forward(100)
    t.circle(20,180)
    t.forward(50)
    t.right(180)
    t.circle(15,180)
    t.right(180)
    t.forward(50)
    t.circle(20,180)
    t.forward(100)
    t.circle(20,180)
    t.forward(25)
    t.left(180)
    t.circle(15,180)
    t.right(180)
    t.forward(25)
    t.circle(20,180)
    t.penup()
    t.backward(10)
    t.left(90)
    t.forward(20)
    t.pendown()
    t.circle(-10,90)
    t.penup()
    t.forward(100)
    t.pendown()
    t.circle(-10,90)
    t.penup()
    t.backward(70)
    t.left(180)
    t.pendown()
    t.circle(10,90)
    t.penup()
    t.forward(100)
    t.pendown()
    t.circle(10,90)


def two():
    t.pendown()
    t.left(180)
    t.circle(40,90)
    t.circle(20,180)
    t.right(110)
    t.circle(20,20)
    t.right(110)
    t.forward(100)
    t.circle(20,120)
    t.forward(50)
    t.circle(20,180)
    t.forward(25)
    t.right(120)
    t.forward(70)
    t.circle(40,110)
    t.left(90)
    t.penup()
    t.forward(10)
    t.right(90)
    t.pendown()
    t.circle(30,-55)
    t.penup()
    t.right(200)
    t.forward(1)

def five():
    t.left(180)
    t.pendown()
    t.circle(20,90)
    t.forward(50)
    t.circle(20,90)
    t.forward(10)
    t.circle(-15,210)
    t.circle(20,180)
    t.circle(53,200)
    t.right(80)
    t.forward(15)
    t.right(90)
    t.forward(20)
    t.circle(20,180)
    t.forward(40)
    t.penup()
    t.backward(40)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.pendown()
    t.circle(10,-90)

def apos():
    t.pendown()
    t.circle(20)
    t.penup()
    t.left(90)
    t.forward(30)
    t.right(90)
    t.pendown()
    t.circle(-10,90)


def BLH_25(y, h, x):
    t.penup()
    t.setx(-280+x)
    t.setheading(h)
    t.sety(y)
    B()
    t.penup()
    t.sety(y)
    t.setheading(h)
    t.setx(-190+x)
    L()
    t.penup()
    t.sety(y)
    t.setheading(h)
    t.setx(-90+x)
    H()
    t.penup()
    t.sety(y-20)
    t.setheading(h)
    t.setx(60+x)
    apos()
    t.penup()
    t.sety(y+5)
    t.setheading(h-10)
    t.setx(130+x)
    two()
    t.penup()
    t.sety(y+5)
    t.setheading(h)
    t.setx(200+x)
    five()

screen.tracer(0)

nua = -450
for i in range(5):
    aa = 0
    bb = 0
    for i in range(3):
        t.clear()
        a = aa + 3*i
        b = bb + 10+i
        BLH_25(nua, a, b)
        nua = nua + 10
        screen.update()
        wait(0.2)

    for i in range(3):
        t.clear()
        a = aa - 3*i
        j = a
        b = bb - 10*i
        BLH_25(nua, a, b)
        nua = nua +10
        screen.update()
        wait(0.2)
    for i in range(3):
        t.clear()
        a = aa - 3 * i
        b = bb - 10 + i
        BLH_25(nua, a, b)
        nua = nua + 10
        screen.update()
        wait(0.2)
    for i in range(3):
        t.clear()
        a = aa + 3 * i
        j = a
        b = bb + 10 * i
        BLH_25(nua, a, b)
        nua = nua + 10
        screen.update()
        wait(0.2)
t.clear()
t.penup()
y = t.ycor()
BLH_25(y,0,0)
screen.update()

wait(0.2)

t.clear()
h = 0
p = t.heading()
print(p)
for i in range(30):
    h = h + 1
    for i in range (10):
        t.pendown()
        t.circle(200+h,1)
        t.penup()
        t.circle(200+h,35)
wait(0.2)
t.clear()

turtle.done()
