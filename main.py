# import modules
import turtle as turtle
import random

# console view
print("Welcome to your drawing app! Select a shape you want to draw. After typing the number and hitting enter, go to the result tab!")

turtle.penup()
turtle.left(90)
turtle.forward(250)
turtle.left(90)
turtle.forward(300)
turtle.pendown()

# result view
turtle.write("Drawing App!", font=("Arial", 16, "normal"))

turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.pendown()

turtle.write("To draw a shape, go to the Console tab and choose an option!", font=("Arial", 16, "normal"))

turtle.penup()
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.pendown()

def star():
  # Star
  for i in range(0, 5):
    turtle.pencolor("yellow")
    turtle.forward(110)
    turtle.left(216)

def square():
  # Square
  for i in range(0, 4):
    turtle.pencolor("orange")
    turtle.forward(100)
    turtle.right(90)

def hexagon():
  # Hexagon
  for i in range(0, 6):
    turtle.pencolor("red")
    turtle.forward(100)
    turtle.right(60)

def circle():
  # Circle
  for i in range(0, 20):
    turtle.pencolor("green")
    turtle.forward(20)
    turtle.right(20)

selection = input("1. Star\n2. Square\n3. Hexagon\n4. Circle\nSelect a number: ")
if selection == "1":
  print("Excellent choice! Go to the result tab to see your creation.")
  star()
elif selection == "2":
  print("Excellent choice! Go to the result tab to see your creation.")
  square()
elif selection == "3":
  print("Excellent choice! Go to the result tab to see your creation.")
  hexagon()
elif selection == "4":
  print("Excellent choice! Go to the result tab to see your creation.")
  circle()