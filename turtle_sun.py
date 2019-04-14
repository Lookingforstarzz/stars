import turtle

def draw_squares(some_squares):
    for i in range(36):
         some_squares.forward(100)
         some_squares.right(90)
         some_squares.forward(100)
         some_squares.right(90)
         some_squares.forward(100)
         some_squares.right(90)
         some_squares.forward(100)
         some_squares.right(90)
         some_squares.right(10)
         


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(10)
    draw_squares(brad)


    window.exitonclick()


draw_art()
