import turtle
from turtle import Turtle
import random

turtle.colormode(255)


def generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    generated_color = (r, g, b)
    return generated_color


FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color(generate_color())
        self.hideturtle()
        self.goto(-240, 275)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_score(self):
        self.level += 1
        self.color(generate_color())
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write(f"GAME OVER\nYour final level was {self.level}", align="center", font=("arial", 30, "bold"))



