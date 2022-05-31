import random
from turtle import Turtle , Screen

colors = ["red", "blue", "purple", "orange", "black", "green", "turquoise", "violet"]

orchid = Turtle()
my_screen = Screen()
orchid.speed(15)
orchid.width(7)



for x in range(0, 300):
	orchid.forward(15)
	directions = [90, 180, 270, 360]
	random_dir = random.choice(directions)
	orchid.right(random_dir)
	rand_color = random.choice(colors)
	orchid.color(rand_color)


















my_screen.exitonclick()