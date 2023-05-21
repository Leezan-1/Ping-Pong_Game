import turtle as t
from paddle import Paddle
from ball import Ball
from wall import Wall
from scoreboard import Scoreboard
import time

# SETTING UP THE SCREEN
screen = t.Screen()
screen.setup(width=830, height=610)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
screen.listen()


# GAME START
game_prompt = Scoreboard('center')


def game_start():
    # CREATING LEFT AND RIGHT PADDLES
    right_paddle = Paddle('right')
    left_paddle = Paddle('left')

    # SETTING UP THE CONTROLS FOR RIGHT PADDLE
    screen.onkeypress(fun=right_paddle.go_up, key='Up')
    screen.onkeypress(fun=right_paddle.go_down, key='Down')

    # SETTIING UP THE CONTROLS FOR LEFT PADDLE
    screen.onkeypress(fun=left_paddle.go_up, key='w')
    screen.onkeypress(fun=left_paddle.go_down, key='s')

    # CREATING WALL
    wall = Wall()

    # CREATING BALL
    ball = Ball()

    # CREATING SCORECARD
    right_score = Scoreboard('right')
    left_score = Scoreboard('left')

    game_on = True
    while game_on:
        screen.update()
        ball.move()
        time.sleep(0.1)


screen.onkeypress(game_start, 'Return')
screen.update()


screen.exitonclick()
