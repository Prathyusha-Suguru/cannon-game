import random
import turtle
from random import randrange
from turtle import *
from freegames import vector


wn=turtle.Screen()
wn.bgcolor("black")
wn.title("cannon game")
ball=vector(-200,-200)
speed=vector(0,0)
targets = []
list=['orange','yellow','gold']



def tap(x,y):
    " respond to screen tap"
    if not inside(ball):
        ball.x=-199
        ball.y=-199
        speed.x=(x+250)/25
        speed.y=(y+250)/25

def inside(xy):
    "return true if xy witin screen"
    return -200 < xy.x < 200 and -200 < xy.x < 200

def draw():
    "draw ball and targets"
    clear()

    for target in targets:
        goto(target.x,target.y)
        dot(25,random.choice(list))

    if inside(ball):
        goto(ball.x,ball.y)
        dot(10,'white')
    
    update()

def move():
    " move ball and targets"
    if randrange(40)==0:
        y=randrange(-150,150)
        target= vector(200,y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5
    
    if inside(ball):
        speed.y-=0.35
        ball.move(speed)
    
    dupe = targets.copy()
    targets.clear()
    
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return
    ontimer(move,50)
setup(420,420,500,0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()







