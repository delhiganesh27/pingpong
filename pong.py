import turtle

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
ball.dx = 0.3  # ball movement
ball.dy = 0.3


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

    if ball.xcor() < -390:
        ball.setx(
            -390
        )  # optional incase if sys is slow it will check after crossing 290
        ball.dx *= -1
