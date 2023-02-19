from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        """ This function updates the scoreboard entry but without cleaning the previous value, see increase_score() for the full scoreboard update function. """
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def reset(self):
        """ This function keeps track of the user's highest score achieved in the previous game and resets the score variable to 0 as the scoreboard updates """
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """ Updating the user's score every time the food is eaten """
        self.score += 1
        self.update_scoreboard()