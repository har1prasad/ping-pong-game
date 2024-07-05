from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Impact', 14, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"Left: {self.left_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"Right: {self.right_score}", align=ALIGNMENT, font=FONT)

    def increase_left_score(self):
        self.left_score += 1
        self.update_scoreboard()

    def increase_right_score(self):
        self.right_score += 1
        self.update_scoreboard()