import random, colorgram
from random import randint, choice
from turtle import Turtle, Screen


WIDTH, HEIGHT = 1000, 1000

screen = Screen()
screen.setup(WIDTH + 4, HEIGHT + 4)
screen.colormode(255)

tim = Turtle()

def random_color():
    rand_color = (randint(1, 255), randint(1, 255), randint(1, 255))
    return rand_color

def draw_dotted_line():
    tim.teleport(-450)
    for step in range(15): # Draws a dotted line
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


def draw_shapes(num_sides_min, num_sides_max):
    tim.teleport(-5, 300)
    kantenzahl = list(range(num_sides_min, num_sides_max + 1))
    for kanten in kantenzahl:
        tim.pencolor(random_color())
        innenwinkel = 360 / kanten

        for _ in range(kanten):
            tim.forward(100)
            tim.right(innenwinkel)

def draw_random_walk(num):
    tim.speed(10)
    tim.shape('circle')
    tim.pensize(10)
    for _ in range(num):
        tim.pencolor(random_color())
        if (-450 < tim.xcor() < 450) and ( -450 < tim.ycor() < 450):
            direction = [0, 90, 180, 270]
            tim.right(random.choice(direction))
            tim.forward(50)
        else:
            tim.right(180)
            tim.forward(50)

def draw_spirograph(anzahl_kreise, kreis_radius):
    tim.speed("fastest")
    drehwinkel = 360 / anzahl_kreise
    for _ in range(anzahl_kreise):
        tim.pencolor(random_color())
        tim.circle(kreis_radius)
        tim.left(drehwinkel)

def test_colorgram():
    # hier kommt noch code
    colors = colorgram.extract('image.png', 100)
    color_list = []
    for elements in colors:
        red = elements.rgb.r
        green = elements.rgb.g
        blue = elements.rgb.b
        new_tuple = (red, green, blue)
        color_list.append(new_tuple)
    color_list = color_list[4:]
    return color_list

def project_spot_painting():
    color_list = test_colorgram()
    tim.teleport(-225, -225)
    tim.hideturtle()

    for column in range(10):
        for line in range(10):
            tim.dot(20, random.choice(color_list))
            tim.penup()
            tim.forward(50)
            tim.pendown()
        y = -225 + (column + 1) * 50
        tim.teleport(-225, y)


project_spot_painting()

screen.exitonclick()