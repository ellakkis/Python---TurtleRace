from turtle import Turtle, Screen
import random

all_turtles = []
screen = Screen()
screen.setup(500, 400)
winning_color = ""
user_bet = screen.textinput("User Bet", "Which turtle will win? Enter color: ").lower()
rainbow_colors = ["red", "orange", "green", "blue", "yellow", "purple", "brown"]
counter = 0
positionx = -230
positiony = -110

for color in rainbow_colors:
  counter += 1
  name = "tim" + str(counter)
  name = Turtle()
  all_turtles.append(name)
  name.shape("turtle")
  name.color(color)
  name.penup()
  name.goto(positionx, positiony)
  positiony += 40
  name.pendown()

end_position_reached = False
all
while not end_position_reached:
  for turtle in all_turtles:
    speed = random.randint(1, 10)
    turtle.forward(speed)
    if turtle.xcor() >= 230:
      winning_color = turtle.color()
      end_position_reached = True
print(f"Winner is {winning_color}")
if user_bet == winning_color:
  print("You Win!")
else:
  print("You Lose!")
  



screen.exitonclick()