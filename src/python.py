import turtle
import time

screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.title("Bouncy Ball!")
screen.bgcolor("#32CD32")
screen.tracer(0)

tuna = turtle.Turtle()
tuna.hideturtle()
tuna.color("Black")
tuna.fillcolor("White")
tuna.penup()

x, y = 0, 0
dx, dy = 2, 2
radius = 20

screen_width = 600 / 2
screen_height = 400 / 2

def drawcircle():
    tuna.goto(x, y - radius)
    tuna.begin_fill()
    tuna.circle(radius)
    tuna.end_fill()

def travel(new_x, new_y):
    global x, y
    x = new_x
    y = new_y

screen.listen()
screen.onkey(lambda: travel(0, 0), "w")

while True:
    tuna.clear()
    drawcircle()
    screen.update()

    x += dx
    y += dy

    if x + radius >= screen_width or x - radius <= -screen_width:
        dx *= -1
    if y + radius >= screen_height or y - radius <= -screen_height:
        dy *= -1

    time.sleep(0.01)