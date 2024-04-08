import turtle as tt
import tkinter as tk
import time
import random

window = tt.Screen()
window.title("Ping Pong !")
window.bgcolor("#F5F5DC")
window.setup(width=800,height=600)
window.tracer(0)
window.cv._rootwindow.resizable(False, False)

getScoreToWin = tt.Screen()
score = getScoreToWin.textinput("Ping Pong!","Enter score to win:")
print(score)


# Mid dashed line
mid_line = tt.Turtle()
mid_line.speed(0)
mid_line.color("#191970")
mid_line.width(width=2)
mid_line.penup()
mid_line.goto(0, 300)
mid_line.setheading(270)

while(mid_line.ycor()>=-300):
    mid_line.pendown()
    mid_line.forward(20)
    mid_line.penup()
    mid_line.forward(20)


#Score Tracking
score_a = 0
score_b = 0


#Paddle A
paddle_a = tt.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("#191970")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = tt.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("#191970")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


#Ball
ball = tt.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#FA8072")
ball.penup()
ball.goto(0,0)
ball.dx = 0.28
ball.dy = -0.28



def ScoreBoard():
    spc = "  "
    pen.write(f"Player{spc}A - {score_a}\tPlayer{spc}B - {score_b}", align = "center", font = ("Karmatic Arcade",15,"normal"))

#Scoreboard
pen = tt.Turtle()
pen.speed(0)
pen.color("#191970")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
ScoreBoard()




##------------- Paddle A controls -----------##
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    if(paddle_a.ycor() > 350):
        paddle_a.sety(-300)

#Keyboard binding
window.listen()
window.onkeypress(paddle_a_up,"w")

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    if(paddle_a.ycor() < -350):
        paddle_a.sety(300)

#Keyboard binding
window.listen()
window.onkeypress(paddle_a_down,"s")
#----------------------------------------------#


##------------- Paddle B controls -----------##

def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)
    if(paddle_b.ycor() > 350):
        paddle_b.sety(-300)

#Keyboard binding
window.listen()
window.onkeypress(paddle_b_up,"Up")

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)
    if(paddle_b.ycor() < -350):
        paddle_b.sety(+300)

#Keyboard binding
window.listen()
window.onkeypress(paddle_b_down,"Down")
#----------------------------------------------#





flag = True
l1 = []
winner = ""
game_over_msg = None

def CheckWin():
    global winner,flag
    if score_a == int(score):
        winner = "A"
        #flag = False
        return [winner,False]
    if score_b == int(score):
        winner = "B"
        #flag = False
        return [winner,False]


def restart(x, y):
    # Clear scores
    global score_a, score_b,l1,winner,game_over_msg
    score_a = 0
    score_b = 0
    l1 = []
    winner = ""
    
    # Clear the scoreboard
    pen.clear()
    ScoreBoard()
    
    if game_over_msg != None:
        game_over_msg.clear()
    
    # Reset paddle positions
    paddle_a.goto(-350, 0)
    paddle_b.goto(350, 0)
    
    # Reset ball position and direction
    ball.goto(0, 0)
    ball.dx = 0.28
    ball.dy = -0.28
    return


def game_over(winner):
    global game_over_msg
    spc = "  "
    if game_over_msg is None:
        game_over_msg = tt.Turtle()
    game_over_msg.speed(0)
    game_over_msg.color("#191970")
    game_over_msg.penup()
    game_over_msg.hideturtle()
    game_over_msg.goto(0,0)
    game_over_msg.write(f"{spc*13}Player {winner} Wins!\n\n{spc*4}Click anywhere to play again.", align="center", font=("Karmatic Arcade", 20, "normal")) 
    window.listen()
    window.onclick(restart)
    return
    

while True:
    while flag == True:
        time.sleep(0.001) 
        window.update()
        
        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        
        # Window Constraints
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            
        if ball.xcor() > 390:
            ball.goto(0, random.randrange(-290, 290))
            ball.dx *= -1
            score_a += 1
            pen.clear()
            ScoreBoard()
            l1 = CheckWin()
        if ball.xcor() < -390:
            ball.goto(0, random.randrange(-290, 290))  
            ball.dx *= -1
            score_b += 1
            pen.clear()
            ScoreBoard()
            l1 = CheckWin()
            
        if l1 is not None and False in l1 :
            break
            
            
        # Handling Collisions for PaddleA
        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1
            

            
        # Handling Collisions for PaddleB
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1
    game_over(l1[0])
            
    
    

        