import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

colors = ['pink','green','purple', 'yellow',]

directions = [0,90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.forward(30)
    tim.color(random_color())
    tim.setheading(random.choice(directions))