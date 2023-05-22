from turtle import Turtle


class Ball(Turtle):
    # CREATES BALL SHAPE, SPEED
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.setheading(45)

        self.x_dis = 10
        self.y_dis = 10
        self.ball_speed = 0.1

    # MOVES BALL IN HORIZONTAL DIRECTION
    def move(self):
        ball_xcor = self.xcor() + self.x_dis
        ball_ycor = self.ycor() + self.y_dis
        self.goto(ball_xcor, ball_ycor)

    # MAKES BALL BOUNCE THE HORIZONTAL WALLS
    def bounce_y(self):
        self.y_dis *= -1

    # MAKES BALL BOUNCE OFF THE PADDLES
    def bounce_x(self):
        self.x_dis *= -1
        self.ball_speed *= 0.9

    # RESETS THE BALL POSITION AND DIRECTION IF BALL IS OUT OF THE BOUNDS
    def ball_reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.ball_speed = 0.1
