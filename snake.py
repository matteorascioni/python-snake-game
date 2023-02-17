from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20 
UP = 90
DOWN = 270 
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """ This function creates the snake's segments """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position): 
        """ This function adds a new segment to the snake """
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """ This function extends the length of the snake when eats food """
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        """ Track the cordinates of the previous segment starting from the last one, to make follow the head of the snake (segments[0]) """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Handling the snake's onkey movements events
    def up(self):
        if self.head.heading() != DOWN:
            return self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            return self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            return self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            return self.head.setheading(RIGHT)