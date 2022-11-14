import turtle
import os

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(1)

# Score
score_one = 0
score_two = 0

racket_one = turtle.Turtle() #racket of the first player
racket_one.speed(0)
racket_one.shape("square")
racket_one.color("red")
racket_one.shapesize(stretch_wid=5, stretch_len=1)
racket_one.penup()
racket_one.goto(-350, 0)

racket_two = turtle.Turtle() #racket of the second player
racket_two.speed(0)
racket_two.shape("square")
racket_two.color("blue")
racket_two.shapesize(stretch_wid=5, stretch_len=1)
racket_two.penup()
racket_two.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player One: 0  Player Two: 0", align="center", font=("Comic Sans MS", 30, "normal"))

def racket_one_up():
    y = racket_one.ycor()
    y += 30
    racket_one.sety(y)

def racket_one_down():
    y = racket_one.ycor()
    y -= 30
    racket_one.sety(y)

def racket_two_up():
    y = racket_two.ycor()
    y += 30
    racket_two.sety(y)

def racket_two_down():
    y = racket_two.ycor()
    y -= 30
    racket_two.sety(y)

wn.listen()
wn.onkeypress(racket_one_up, "w")
wn.onkeypress(racket_one_down, "s")
wn.onkeypress(racket_two_up, "Up")
wn.onkeypress(racket_two_down, "Down")

while True:
    wn.update()
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.xcor() > 350:
        score_one += 1
        score.clear()
        score.write(f"Player One: {score_one}  Player Two: {score_two}", align="center", font=("Comic Sans MS", 30, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_two += 1
        score.clear()
        score.write(f"Player One: {score_one}  Player Two: {score_two}", align="center", font=("Comic Sans MS", 30, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.ycor() < racket_one.ycor() + 50 and ball.ycor() > racket_one.ycor() - 50:
        ball.dx *= -1
        ball.dx *= 1.1
        ball.dy *= 1.1
        os.system("afplay bounce.wav&")
    
    elif ball.xcor() > 340 and ball.ycor() < racket_two.ycor() + 50 and ball.ycor() > racket_two.ycor() - 50:
        ball.dx *= -1
        ball.dx *= 1.1
        ball.dy *= 1.1
        os.system("afplay bounce.wav&")