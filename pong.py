import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width= 800, height = 600)
wn.tracer(0)

score_a = 0
score_b = 0



player_a = turtle.Turtle()
player_a.speed(0)
player_a.penup()
player_a.color("white")
player_a.shape("square")
player_a.shapesize(stretch_wid =5, stretch_len =1)
player_a.goto(-350,0)


player_b = turtle.Turtle()
player_b.speed(0)
player_b.penup()
player_b.color("white")
player_b.shape("square")
player_b.shapesize(stretch_wid =5, stretch_len =1)
player_b.goto(350,0)

ball = turtle.Turtle()
ball.speed(0)
ball.penup()
ball.shape("circle")
ball.color("grey")
ball.goto(0,0)
ball.dx = 0.85
ball.dy = 0.85



pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color("white")
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0",align = "center",font=("Courier",24,"normal"))


#Functions

def move_a_up():
    y = player_a.ycor()
    y+= 20
    player_a.sety(y)

def move_a_down():
    y = player_a.ycor()
    y-= 20
    player_a.sety(y)

def move_b_down():
    y = player_b.ycor()
    y-= 20
    player_b.sety(y)

def move_b_up():
    y = player_b.ycor()
    y+= 20
    player_b.sety(y)
    
    


wn.listen()
wn.onkeypress(move_a_up,"w")
wn.onkeypress(move_a_down,"s")
wn.onkeypress(move_b_down,"k")
wn.onkeypress(move_b_up,"i")






#Main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b),align = "center",font=("Courier",24,"normal"))

    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b),align = "center",font=("Courier",24,"normal"))
        
    #Check for paddle collison


    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player_b.ycor()+40 and ball.ycor() > player_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    
    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player_a.ycor()+40 and ball.ycor() > player_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        
        


wn.mainloop()

