# --------------------------------- EL PYTHONCITO XD 🐍🐍🐍🐍
# -------------------- Import modules
import random
from turtle import Turtle, Screen
from data import my_colors
from art import logo

# ------------------------- Turtle
pythoncito = Turtle()
my_screen = Screen()

pythoncito.speed("fastest")
my_screen.colormode(255)


# -------------------------------------------- Functions
def move():
    # DO something
    for i2 in range(20):
        pythoncito.color(random.choice(my_colors))
        pythoncito.begin_fill()
        pythoncito.circle(5)
        pythoncito.end_fill()
        pythoncito.teleport(pythoncito.xcor() + 20, pythoncito.ycor())


pythoncito.teleport(-175, 200)
pythoncito.write(f"{logo}", font=("Times new roman", 12, "normal"))

x = -200
y = -200

for i in range(20):
    pythoncito.teleport(x, y)
    move()
    y += 20

my_screen.exitonclick()
