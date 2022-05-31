import random
import turtle
from turtle import Turtle , Screen

colors = ["red", "blue", "purple", "orange", "black", "green", "turquoise", "violet"]

orchid = Turtle()
my_screen = Screen()
orchid.speed(15)

for x in range(0, 75):
	orchid.circle(100)
	orchid.color(random.choice(colors))
	orchid.right(5)


my_screen.exitonclick()