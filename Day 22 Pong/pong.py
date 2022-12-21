from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard
from net import Net
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)
ball = Ball()
net = Net()
score = Scoreboard()
r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
screen.listen()

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with upper or lower wall
    if ball.ycor() > 285 or ball.ycor() < -285:  # dist from  wall less than 30 pixels
        ball.bounce_y()

    # Detect collision with right wall = right paddle misses
    if ball.xcor() > 400:
        ball.reset()
        score.l_point()
    # Detect collision left wall = left paddle misses
    if ball.xcor() < -400:
        ball.reset()
        score.r_point()
    #ball.move()
    #game_on = False
    #scoreboard.game_over()
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor()> 330 or ball.distance(l_paddle) < 50 and ball.xcor()< -330:
        ball.bounce_x()


screen.exitonclick()