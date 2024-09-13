import turtle as trtl
import random
import time
import math

# Screen Set Up
wn = trtl.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=800)
space = "spaceship.gif"
alien = "alien.gif"
wn.addshape(space)
wn.addshape(alien)

# Player Turtle
Sship = trtl.Turtle()
Sship.penup()
Sship.shape(space)
scorepen = trtl.Turtle()
space_vertical = 0
space_horizontal = 0

# Border
border_pen = trtl.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-350, -300)
border_pen.pendown()
border_pen.pensize(3)
border_pen.hideturtle()
for i in range(4):
    border_pen.fd(700)
    border_pen.lt(90)
    border_pen.hideturtle()

# Scoring Set Up
trtl.penup()
trtl.goto(-350, 390)
trtl.hideturtle()
trtl.pencolor("white")
trtl.write("Score: ", align="center", font=("Academy Engraved LET", 40))
scorepen.penup()
scorepen.goto(-270, 390)
scorepen.color("white")
scorepen.hideturtle()

# Bullet set up
bullet = trtl.Turtle()
bullet.shape("triangle")
bullet.color("yellow")
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bulletspeed = 40
bullet_state = "ready"

# Initial game state
play = True 


def forward():
    global space_vertical
    space_vertical = 10
    print("Forward: ", space_vertical)


def backward():
    global space_vertical
    space_vertical = -10
    print("Backward: ", space_vertical)


def right():
    global space_horizontal
    space_horizontal = 10
    print("Right", space_horizontal)


def left():
    global space_horizontal
    space_horizontal = -10
    print("Left", space_horizontal)


def stop_vertical():
    global space_vertical
    space_vertical = 0
    print("Stop_Vetical", space_vertical)


def stop_horizontal():
    global space_horizontal
    space_horizontal = 0
    print("Stop_Horizontal", space_horizontal)


def move():
    global play
    if play == True:
        Sship.goto(Sship.xcor() + space_horizontal, Sship.ycor() + space_vertical)
        wn.ontimer(move, 6)


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 25:
        print(distance)
        return True
    else:
        return False


def firingbullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        x = Sship.xcor()
        y = Sship.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()




wn.onkeypress(firingbullet, "j")
move()
wn.listen()
wn.onkeypress(backward, "s")
wn.onkeypress(right, "d")
wn.onkeypress(left, "a")
wn.onkeypress(forward, "w")
wn.onkeyrelease(stop_vertical, "w")
wn.onkeyrelease(stop_vertical, "s")
wn.onkeyrelease(stop_horizontal, "a")
wn.onkeyrelease(stop_horizontal, "d")




score = 0
wn.addshape(alien)
enemy_list = []
enemy_speed = 1
number_of_aliens = 4
while play == True:
    print("Start of outer while loop")
    
    if enemy_list == []:
        #creating enemy list 
        for i in range(number_of_aliens):
            enemy = trtl.Turtle()
            enemy.isvisible()
            enemy.shape('alien.gif')
            enemy.up()
            enemy.speed(0)
            randx = random.randint(-300, 300)
            randy = random.randint(150, 390)
            enemy.goto(randx, randy)
            enemy.dx = enemy_speed
            enemy_list.append(enemy)
        #Game function loop
         
        while play == True:
            if bullet_state == "fire":
                y = bullet.ycor()
                y += bulletspeed
                bullet.speed(0)
                bullet.sety(y)
            if bullet.ycor() > 400:
                bullet.hideturtle()
                bullet_state = "ready"
            for enemy in enemy_list:
                x = enemy.xcor()
                x += enemy_speed
                enemy.setx(x)
                #bounce the enemy to the left 
                if enemy.xcor() >= 280:
                    for enemy2 in enemy_list:
                        enemy2.sety(enemy2.ycor() - 20)
                    enemy_speed = -5
                #bounce the enemy to the right 
                if enemy.xcor() <= -280:
                    for e in enemy_list:
                        e.sety(e.ycor() - 30)
                    enemy_speed = 5
                #enemy goes below 400 pixel 
                if enemy.ycor() <= -400:
                    play = False
                    for j in enemy_list: 
                        j.goto(1000000,100000)
                    
                #collision between the bullet and enemy 
                if isCollision(bullet, enemy):
                    scorepen.clear()
                    bullet_state = "ready"
                    bullet.hideturtle()
                    enemy.goto(random.randint(-300, 300), random.randint(150, 390))
                    score += 10
                    print(score)
                    scorepen.write(score, align="center", font=("Academy Engraved LET", 40))
                    #increase difficulty every time you reach a 100th point mark 
                    if score % 100 == 0:
                        enemy_speed += 1
                        bulletspeed += 1
                #Collision between the ship and the enemy
                if isCollision(Sship, enemy):
                    play = False
                    for j in enemy_list: 
                        j.hideturtle()
                    
    print("Broke out of inner while loop")
    playagain = wn.textinput(title="Play Again?", prompt="Play again? (y/n)?")
    if playagain == "y":
        play = True
        score = 0 
        scorepen.clear()
        enemy_list = []
        enemy.hideturtle()
        Sship.goto(0,0)
        move()
        wn.listen()
        wn.onkeypress(backward, "s")
        wn.onkeypress(right, "d")
        wn.onkeypress(left, "a")
        wn.onkeypress(forward, "w")
        wn.onkeyrelease(stop_vertical, "w")
        wn.onkeyrelease(stop_vertical, "s")
        wn.onkeyrelease(stop_horizontal, "a")
        wn.onkeyrelease(stop_horizontal, "d")
    elif playagain == "n":
        play = False 
        wn.clear()
        wn.bgcolor("black")
        trtl.hideturtle()
        trtl.pencolor("White")
        trtl.write("Game Over!", align="center", font=("Academy Engraved LET", 70))
               



wn.mainloop()
