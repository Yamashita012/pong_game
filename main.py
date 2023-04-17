from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard 
import time


screen = Screen()
screen.title("Pong")
screen.setup(width=1000, height=700)
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()
ball =Ball()
r_paddle = Paddle((460, 0))
l_paddle = Paddle((-460, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on =True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 330 or ball.ycor() < -330 :
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 435 or ball.distance(l_paddle) < 50 and ball.xcor() < -435:
        ball.bounce_x()

    if ball.xcor() > 490:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -490:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()