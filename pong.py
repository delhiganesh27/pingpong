import turtle
import winsound

score_a = 0
score_b = 0

win = turtle.Screen()
win.setup(800, 600)  # screen size
win.bgcolor("blue")
win.title("pingPong")
win.tracer(0)  # to display the paddle in desired position initially

# left paddle
left = turtle.Turtle()
left.speed(0)  # to move the paddle to left position immediately
left.shape("square")
left.color("white")
left.shapesize(stretch_wid=5, stretch_len=1)
left.penup()
left.goto(-380, 0)


# right paddle
right = turtle.Turtle()
right.speed(0)  # to move the paddle to right position immediately
right.shape("square")
right.color("white")
right.shapesize(stretch_wid=5, stretch_len=1)
right.penup()
right.goto(380, 0)


# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx = 0.8  # ball movement
ball.dy = 0.8

# score
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.write("Player A : 0 Player B : 0", align="center", font=("Ariel", 24, "normal"))


# moving paddles
def left_up():
    left.sety(left.ycor() + 20)


def right_up():
    right.sety(right.ycor() + 20)


def left_down():
    left.sety(left.ycor() - 20)


def right_down():
    right.sety(right.ycor() - 20)


win.listen()
win.onkeypress(left_up, "w")
win.onkeypress(left_down, "s")
win.onkeypress(right_up, "Up")
win.onkeypress(right_down, "Down")


while True:  # for  constantly display screen
    win.update()
    # ball movement in trajectory
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # ball -wall collision

    # top wall
    if ball.ycor() > 290:
        ball.sety(
            290
        )  # optional incase if sys is slow it will check after crossing 290
        ball.dy *= -1

    # bottom wall

    if ball.ycor() < -280:
        ball.sety(
            -280
        )  # optional incase if sys is slow it will check after crossing 290
        ball.dy *= -1

    # right wall

    if ball.xcor() > 380:
        ball.setx(
            380
        )  # optional incase if sys is slow it will check after crossing 290
        ball.dx *= -1
        pen.clear()
        score_a += 1
        pen.write(
            f"Player A : {score_a} Player B : {score_b}",
            align="center",
            font=("Ariel", 24, "normal"),
        )

    # left wall
    if ball.xcor() < -390:
        ball.setx(
            -390
        )  # optional incase if sys is slow it will check after crossing 290
        ball.dx *= -1
        pen.clear()
        score_b += 1
        pen.write(
            f"Player A : {score_a} Player B : {score_b}",
            align="center",
            font=("Ariel", 24, "normal"),
        )

    # collision with paddles
    # for right paddle
    if ball.xcor() > 360 and right.ycor() - 50 < ball.ycor() < right.ycor() + 50:
        ball.setx(360)
        ball.dx *= -1
    # for left paddle
    if ball.xcor() < -360 and left.ycor() - 50 < ball.ycor() < left.ycor() + 50:
        ball.setx(-360)
        ball.dx *= -1
    if score_a == 5:
        pen.write("Player A wins", align="center", font=("Ariel", 30, "normal"))

        break
    if score_b == 5:
        pen.write("Player B wins", align="center", font=("Ariel", 30, "normal"))
        break
