import time
from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

scoreboard= Scoreboard()
screen = Screen()

screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with the wall
    if ball.ycor()>280 or ball.ycor()< -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) <50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()< -320:
        ball.bounce_x()

    #detect if ball missed the right paddle
    if ball.xcor()>400 :
        ball.reset_position()
        scoreboard.l_point()

#detect if ball missed the left paddle
    if ball.xcor()< -400 :
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()