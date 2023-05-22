from turtle import Turtle
STARTING_POSITION = [(-375, 0), (370, 0)]
PADDLE_WIDTH = 5    # height of paddles
PADDLE_LEN = 1      # thickness of paddles
PADDLE_WALK = 50    # distance paddles walk when button is pressed


class Paddle(Turtle):
    # CREATES PADDLE SHAPE, SIZE AND POSITION
    def __init__(self, side):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(PADDLE_WIDTH, PADDLE_LEN)
        self.speed('fastest')
        if (side == 'right'):
            self.right_paddle()
        else:
            self.left_paddle()

    def right_paddle(self):
        # SETS POSITION OF RIGHT PADDLE
        self.goto(STARTING_POSITION[1])

    def left_paddle(self):
        # SETS POSITION OF LEFT PADDLE
        self.goto(STARTING_POSITION[0])

    def go_up(self):
        # SETS UPWARD MOVEMENT OF PADDLE
        if (self.ycor() < 250):
            up = self.ycor() + PADDLE_WALK
            self.goto(self.xcor(), up)

    def go_down(self):
        # SETS DOWNWARD MOVEMENT OF PADDLE
        if (self.ycor() > -250):
            down = self.ycor() - PADDLE_WALK
            self.goto(self.xcor(), down)
