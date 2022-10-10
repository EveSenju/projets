import turtle


def triangle_equilateral(long):
    turtle.reset()
    turtle.home()
    turtle.up()
    turtle.goto(-50,-50)
    turtle.down()
    turtle.forward(long)
    turtle.left(120)
    turtle.forward(long)
    turtle.left(120)
    turtle.forward(long)

long = 100
#triangle_equilateral(long)

def hexagones(long):
    for i in range(6):
        turtle.forward(long)
        turtle.left(60)
        

for _ in range(4) :
    hexagones(long)
    turtle.left(90)





