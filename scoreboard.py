from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        """ This function updates the scoreboard entry but without cleaning the previous value, see increase_score() for the full scoreboard update function. """
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """ Make the words game over appear when the user loses """
        self.goto(0, 0)
        self.write(arg="Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """ Updating the user's score every time the food is eaten """
        self.score += 1
        self.clear()
        self.update_scoreboard()