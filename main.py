from turtle import Turtle,Screen
from random import randint

screen = Screen()
screen.setup(width = 500,height = 400)

user_bet = screen.textinput(title = "Bet", prompt= "Which turtle would you like to bet on?")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []
for turtle_index in range (0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-250, y=60 - (turtle_index * 30))
    all_turtles.append(new_turtle)

print(all_turtles)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_colour = turtle.pencolor()
            print(f"The winner is {winning_colour}")
            is_race_on = False
        rand_distance = randint(0,10)
        turtle.forward(rand_distance)












screen.exitonclick()












