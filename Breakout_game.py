import turtle, random, math

# Global Variables
speed = 5
canvas_width = 500
canvas_height = 750
x_edge = canvas_width // 2
y_edge = canvas_height // 2
dy = random.uniform(0.5, 1) * speed
dx = ((speed ** 2) - (dy ** 2)) ** 0.5
score = 0
ball = None
circle_radius = 10
screen = turtle.Screen()
myPen = turtle.Turtle()
col = 7
row = 5
arr = [[0] * col for x in range(row)]
global paddle


def setup():

    global dy, dx, paddle, ball, arr, myPen

    # Create Screen and Turtle object
    #screen.tracer(False)
    myPen = turtle.Turtle()
    screen.setup(canvas_width, canvas_height, startx=None, starty=None)
    #myPen.tracer(False)
    myPen.hideturtle()
    myPen.penup()
    screen.bgcolor("black")
    screen.delay(0)
    sprite = turtle.Turtle()
    sprite.penup()
    sprite.speed(0)
    sprite.hideturtle()

    # Creating the paddle object

    screen.register_shape('paddle', ((-10, -40), (10, -40), (10, 40), (-10, 40)))

    sprite.color("orange")

    paddle = sprite.clone()

    paddle.shape("paddle")

    paddle.showturtle()

    paddle.goto(0, -290)

    screen.onkey(right, "Right")

    screen.onkey(left, "Left")

    screen.listen()
    # Creating the red ball

    ball = sprite.clone()

    ball.shape("circle")

    ball.color("red")

    ball.goto(0, 0)

    ball.seth(0)

    ball.showturtle()

    # Creating the green breakout bricks
    screen.register_shape('brick', ((-10, -30), (10, -30), (10, 30), (-10, 30)))

    sprite.color("green")

    brick_template = sprite.clone()

    brick_template.shape("brick")
    for r in range(row):

        for c in range(col):
            arr[r][c] = brick_template.clone()

            arr[r][c].showturtle()

            arr[r][c].goto(-210 + c * 70, 350 - r * 35)

    # Creating the scoreboard
    #myPen.tracer(False)
    myPen.hideturtle()
    myPen.penup()
    myPen.goto(220, -330)
    myPen.color("white")
    myPen.write(score, None, "center", "20pt bold")


def check_collided(paddle):

    if dy > 0:
        return False
    elif math.fabs(paddle.ycor() - ball.ycor()) < 25 and math.fabs(paddle.xcor() - ball.xcor()) < 45:
        return True
    return False


def right():
    global paddle
    if x_edge-paddle.xcor() > 30:

        paddle.goto(paddle.xcor()+20, paddle.ycor())


def left():
    global paddle
    if x_edge+paddle.xcor() > 30:

        paddle.goto(paddle.xcor()-20, paddle.ycor())


def update():
    global dy, dx, score, myPen

    # Check if the ball is hitting the wall or the paddle
    if ball is not None:
        x = ball.xcor()
        y = ball.ycor()
        if math.fabs(y) > y_edge - circle_radius or check_collided(paddle):
            dy = -dy
        elif math.fabs(x) > x_edge - circle_radius:
            dx = -dx
        # Check if the ball is hitting a brick
        if not (arr[0][0] == 0):
            for r in range(row):
                for c in range(col):
                    if (arr[r][c].isvisible() and math.fabs(y - arr[r][c].ycor()) < 25 and math.fabs(
                            x - arr[r][c].xcor()) < 35):
                        dy = -dy
                        arr[r][c].hideturtle()
                        score += 1
                        myPen.clear()
                        myPen.color("white")
                        myPen.write(score, None, "center", "20pt bold")

        # Check game over
        if y < 0 and math.fabs(y) > y_edge - circle_radius:
            myPen.penup()
            myPen.goto(0, 30)
            myPen.write("Game Over", None, "center", "30pt bold")
        elif score == (row * col):
            myPen.penup()
            myPen.goto(0, 30)
            myPen.write("You Win", None, "center", "30pt bold")
        else:
            ball.goto(x + dx, y + dy)
            screen.ontimer(update, 20)


# The following code runs when the play button is pressed.
setup()
update()