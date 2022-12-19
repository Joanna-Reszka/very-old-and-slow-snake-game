from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)


turtles = []
for _ in range(0, 3):
    new_turtle = Turtle("square")
    new_turtle.color('white')
    new_turtle.penup()
    turtles.append(new_turtle)
print(len(turtles))

x = 0
for turtle in turtles:
    turtle.goto(x, 0)
    x -= 20

screen.update()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for index in range(len(turtles)-1, 0,-1):
        new_x = turtles[index - 1].xcor()
        new_y = turtles[index - 1].ycor()
        turtles[index].goto(new_x, new_y)
    turtles[0].fd(20)





screen.exitonclick()



