import turtle
import time
import cv2
import numpy as np

turtle.colormode(255)
turtle.getscreen()
screen = turtle.Screen()
screen.clear()
screen.tracer(0)
screen.screensize(900, 900)
screen.setup(900, 900)



t = turtle.Turtle()
t.hideturtle()
t.pensize(5)
# FROM HERE TO DOWN THERE, CHATGPT HELPED A LOT

# Swans
# Load and preprocess image
image = cv2.imread("images/the_swans.png")
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
image = cv2.imread("images/lake_outline.png")
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
screen.update()





def tcolor(color):
    t.color(color)
    t.pencolor(color)
    t.fillcolor(color)

def wait(seconds):
    start = time.time()
    while time.time() - start < seconds:
        turtle.update()  # Keeps the window responsive



def hex_to_rgb(hex_color):
    # Strip the '#' character if present
    hex_color = hex_color.lstrip('#')
    # Convert the hex values to RGB
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return (r, g, b)
def get_color_at_position():
    # Get turtle position and screen coordinates
    c = turtle.Screen().getcanvas()
    x, y = t.position()
    items = c.find_overlapping(x, -y, x, -y) # omg its working
    if len(items) > 0:
        coloratpixel = c.itemcget(items[-1], "fill")
        # If the color is a hex string, convert it to an RGB tuple
        if coloratpixel == "":
            # Get the "outline" color (pen color) instead of the fill
            coloratpixel = c.winfo_rgb(c.itemcget(items[-1], "stroke"))
        if coloratpixel.startswith('#'):
            coloratpixel = hex_to_rgb(coloratpixel)
        return coloratpixel
    else:
        return "1, 1, 1"  # Return fallback color, is background color
def draw_or_not():
    t.hideturtle()
    coloratpixel = get_color_at_position()
    t.showturtle()
    if coloratpixel == "0, 0, 0":
        t.pendown()
    else:
        t.penup()




# the lines part
t.pensize(1)
screen.bgcolor(1, 1, 1)
screen.update()
t.speed(10)
tcolor("red")
t.pencolor("red")
t.shape("circle")
t.turtlesize(0.5)
t.showturtle()
screen.tracer(1)
screen.delay(0.1)

for i in range(90):
    t.penup()
    t.setposition(-450, 450-50*i)
    for i in range(900):
        draw_or_not()
        t.forward(1)

















turtle.done()

