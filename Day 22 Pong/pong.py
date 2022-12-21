from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)
ball = Ball()
r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Detect collision with upper or lower wall
    if ball.ycor() > 285 or ball.ycor() < -285:  # dist fro  wall less than 30 pixels
        ball.bounce()

    # Detect collision side walls
    if ball.xcor() > 400 or ball.xcor() < -400:
        game_on = False
        #scoreboard.game_over()


screen.exitonclick()