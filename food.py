from turtle import Turtle
import random

color_list = ["red", "blue", "green", "yellow", "brown", "pink", "purple", "lightblue", "lightcyan", "lightgray"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def food_color_update(self):
        """ This function creates a new random color for the each food pieces. """
        random_color = random.choice(color_list)
        self.color(random_color)

    def refresh(self):
        """ This function randomize the appearance of food in the game, once at the beginning and each time after the snake has eaten """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.food_color_update()