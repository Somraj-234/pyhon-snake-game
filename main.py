from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

# canvas
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# keyboard key mapping
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# detection of snake colliding food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

# detection of snake colliding wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        is_game_on = False

    # detection of snake colliding tail
    # slicing. it will check every segment other than first (index 0)
    for segments in snake.segment[1:]:
        if snake.head.distance(segments) < 10:
            is_game_on = False
            scoreboard.game_over()


screen.exitonclick()