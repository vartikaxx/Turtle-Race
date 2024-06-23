from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color")
colors=["red","blue","green","yellow","orange","purple"]
y_coordinates=[-70,-40,-10,20,50,80]

all_turtles=[]

for turtle_index in range(6):
    myturtle = Turtle(shape="turtle")
    myturtle.color(colors[turtle_index])
    myturtle.penup()
    myturtle.goto(x=-230,y=y_coordinates[turtle_index])
    all_turtles.append(myturtle)


if user_bet:
    is_race_on= True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on= False
            winning_turtle= turtle.pencolor()
            if winning_turtle==user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner")
        distance=random.randint(0,10)
        turtle.forward(distance)

screen.exitonclick()
