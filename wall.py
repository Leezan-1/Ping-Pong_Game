from turtle import Turtle
WALL_WIDTH = 1.5
WALL_LENGTH = 0.5
WALL_POSITION = []
for i in range(-300, 350, 50):
    x_cor = 0
    y_cor = i
    position = (x_cor, y_cor)
    WALL_POSITION.append(position)


class Wall:
    def __init__(self) -> None:
        self.walls = []

        for position in WALL_POSITION:
            self.wall = Turtle('square')
            self.wall.penup()
            self.wall.shapesize(WALL_WIDTH, WALL_LENGTH)
            self.wall.color('white')
            self.wall.goto(position)
            self.walls.append(self.wall)
