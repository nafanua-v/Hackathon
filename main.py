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

def clear_the_screen():
    t.pencolor("#0A0A0A")
    t.pensize(10)
    t.penup()
    for i in range(450):
        t.setposition(-450, 450-2*i)
        t.forward(900)
    t.pensize(1)
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

t.pencolor("white")
draw_simple("images/lake_final.png","images/final_swans.png", "images/swans_shading.png")
screen.update()

"""


def draw_lines(water, body1, shading2):
    clear_the_screen()
    t.pencolor("red")
    draw(water, body1, shading2)

    rasterize_canvas()  # Preprocess once

    t.pencolor("white")
    for j in range(300):
        y = 3 * j
        t.penup()
        t.setposition(-450, 450 - y)
        for i in range(900):
            draw_or_not_fast(i, y)
            t.forward(1)
    screen.update()


screen.tracer(0)
draw_lines("images/One.png", "images/One 1.png", "images/One 2.png")

"""

turtle.done()
