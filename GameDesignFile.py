import turtle as trtl 
import random 
import time
import math 
 

#Design the game
space = "Logo.gif"
ship = "spaceship.gif"
alien = "alien.gif"

wn = trtl.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=800)
font=("Academy Engraved LET",40)
color = "#cab161"
print("Welcome to Space Invader game")
print("=============================")
print("Press j to play")
print("Press x to see the control section")
print("Press z to return to the menu screen")
#The Menu
def screen_setup():
    wn.bgcolor("black")
    wn.setup(width=800, height=800)
    wn.addshape(space)
    wn.addshape(ship) 
    logo = trtl.Turtle()
    logo.shape(space)
    logo.goto(0,100)
    # Play button
    Control = trtl.Turtle()
    Play_button = trtl.Turtle()
    Play_button.hideturtle()
    Play_button.pencolor(color)
    Play_button.penup()
    Play_button.goto(-25,-100)
    Play_button.pendown()
    Play_button.write("Play",font=("Academy Engraved LET",40))
    # Control button
    Control.hideturtle()
    Control.pencolor(color)
    Control.penup()
    Control.goto(-75,-150)
    Control.pendown()
    Control.write("Instuctions", font=("Academy Engraved LET",40))
screen_setup()
def Control_Button():
    wn.clear()
    wn.bgcolor("black")
    instructions = trtl.Turtle()
    instructions.penup()
    instructions.speed(0)
    instructions.color(color)
    instructions.goto(0,115)
    instructions.write("Welcome to Space Invader", align="center", font=("Academy Engraved LET",50))
    instructions.goto(0,90)
    instructions.write("Move with 'w' 'a' 's' 'd', and shoot with j.", align="center", font=("Academy Engraved LET", 24))
    instructions.goto(0,60)
    instructions.write("Enjoy your time",align="center", font=("Academy Engraved LET", 24))
    instructions.hideturtle()
    wn.onkeypress(screen_setup,"z")
    wn.onkeypress(play_button,"j")
    wn.onkeypress(Control_Button,"x")
#The Game 
def play_button():
    wn.clear()
    wn.bgcolor("black")
    import GameFunction
wn.onkeypress(play_button,"j")  
wn.onkeypress(Control_Button,"x")
wn.onkeypress(screen_setup,"z")
wn.listen()
wn.mainloop()

