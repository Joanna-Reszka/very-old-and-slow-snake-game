from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.25)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15: #dist fro  head of snake to food less than 15 pixels
        food.refresh()


screen.exitonclick()



