from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 800, height = 500)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #Detect collision with food
    if snake.head.distance(food) < 15: #dist fro  head of snake to food less than 15 pixels
        food.refresh()
        snake.extend()
        scoreboard.count_score()

    # Detect collision with wall
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 230 or snake.head.ycor() < -230:
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) <10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()



