from turtle import Turtle
FONT = ('Courier', 60, 'normal')
PROMPT_FONT = ('Courier', 30, 'normal')
ALIGNMENT = 'center'
SCORECARD_POSITION = [(100, 230), (-100, 230), (0, 0)]


class Scoreboard(Turtle):
    def __init__(self, side) -> None:
        super().__init__()
        self.score = 0

        # TURTLE VISIBILITY IS OFF SO THAT WE CAN WRITE ON SCORECARD
        self.hideturtle()
        self.color('grey')
        self.pu()
        if (side == 'right'):
            self.goto(SCORECARD_POSITION[0])
            self.update_score()
        elif (side == 'left'):
            self.goto(SCORECARD_POSITION[1])
            self.update_score()
        elif (side == 'center'):
            self.goto(SCORECARD_POSITION[2])
            self.start_prompt()

    def update_score(self):
        self.write(f"{self.score}", False, ALIGNMENT, FONT)

    def got_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def start_prompt(self):
        self.write("Press Enter to START", False, ALIGNMENT, PROMPT_FONT)
