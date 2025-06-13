import turtle
import time
import random

# Set up screen
screen = turtle.Screen()
screen.title("Chiara's Snake Game 🐍")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, -40)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Score display
score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# Game Over display
game_over_pen = turtle.Turtle()
game_over_pen.speed(0)
game_over_pen.color("white")
game_over_pen.penup()
game_over_pen.hideturtle()

# Welcome screen
welcome_pen = turtle.Turtle()
welcome_pen.speed(0)
welcome_pen.color("white")
welcome_pen.penup()
welcome_pen.hideturtle()
welcome_pen.goto(0, 0)
welcome_pen.write("Benvenuto! Premi SPAZIO per iniziare", align="center", font=("Courier", 20, "normal"))

segments = []
game_running = False

# Movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

def reset_game():
    global score, segments, game_running
    head.goto(0, -40)
    head.direction = "stop"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    score = 0
    pen.clear()
    pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
    game_running = False

def start_game():
    global game_running
    welcome_pen.clear()
    game_running = True
    head.goto(0, 0)
    head.direction = "stop"
    run_game_loop()

def run_game_loop():
    global score

    if not game_running:
        return

    screen.update()
    move()

    # Check border collision
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        game_over()
        return

    # Check self collision
    for segment in segments[1:]:
        if segment.distance(head) < 20:
            game_over()
            return

    # Check food collision
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

    # Move segments
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    screen.ontimer(run_game_loop, 100)

def game_over():
    global game_running
    game_running = False
    game_over_pen.clear()
    game_over_pen.goto(0, 0)
    game_over_pen.write("GAME OVER", align="center", font=("Courier", 28, "bold"))
    screen.update()
    time.sleep(2)
    game_over_pen.clear()
    reset_game()

# Controls
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")
screen.onkey(start_game, "space")

screen.mainloop()
