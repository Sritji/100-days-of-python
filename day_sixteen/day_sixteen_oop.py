# import turtle

# blaze = turtle.Turtle()

from turtle import Turtle, Screen

blaze = Turtle()

print(blaze) 
blaze.shape("turtle")
blaze.color("pink")
blaze.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()