import turtle

for distance in range(1, 100, 4):
    turtle.forward(distance)
    turtle.left(90)

turtle.forward(94)
turtle.left(90)
turtle.forward(4)
turtle.left(90)

for distance in range(90, 0, -4):
    turtle.forward(distance)
    turtle.right(90)

turtle.done()

# print(*dir(__builtins__))
