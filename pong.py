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
left.goto(-380, 0)
left.penup()

# right paddle
right = turtle.Turtle()
right.speed(0)  # to move the paddle to right position immediately
right.shape("square")
right.color("white")
right.shapesize(stretch_wid=5, stretch_len=1)
right.goto(380, 0)
right.penup()

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("cirle")
ball.color("white")


while True:  # for  constantly display screen
    win.update()
