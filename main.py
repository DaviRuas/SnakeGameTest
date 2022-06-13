import turtle

#CONSTANTS
WIDTH = 500
HEIGHT = 500
DELAY = 400

#SCREEN:
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Game")
screen.bgcolor("cyan")
screen.tracer(False)

#STAMPER:
stamper = turtle.Turtle()
stamper.shape("square")
stamper.color()
stamper.penup()


#MAKE SNAKE REPRESENTATION:
snake = [[0,20],[0,40],[0,60],[0,80]]

#DRAW SNAKE:
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()






turtle.done()


