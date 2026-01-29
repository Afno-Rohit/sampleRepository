import turtle, time, random

delay, score, high = 0.1, 0, 0
wn = turtle.Screen(); wn.title("Snake"); wn.bgcolor("black"); wn.setup(600,600); wn.tracer(0)

head = turtle.Turtle(); head.shape("square"); head.color("green"); head.penup(); head.direction="stop"
food = turtle.Turtle(); food.shape("circle"); food.color("red"); food.penup(); food.goto(0,100)
pen = turtle.Turtle(); pen.hideturtle(); pen.color("white"); pen.penup(); pen.goto(0,260)
segments=[]

def move(): 
    x,y=head.xcor(),head.ycor()
    if head.direction=="up": head.sety(y+20)
    if head.direction=="down": head.sety(y-20)
    if head.direction=="left": head.setx(x-20)
    if head.direction=="right": head.setx(x+20)

def go(d):
    if (d=="up" and head.direction!="down") or (d=="down" and head.direction!="up") or (d=="left" and head.direction!="right") or (d=="right" and head.direction!="left"): 
        head.direction=d

for k,v in {"w":"up","s":"down","a":"left","d":"right"}.items(): wn.onkeypress(lambda d=v: go(d), k)
wn.listen()

while True:
    wn.update()
    if abs(head.xcor())>290 or abs(head.ycor())>290 or any(seg.distance(head)<20 for seg in segments):
        time.sleep(1); head.goto(0,0); head.direction="stop"; [s.goto(1000,1000) for s in segments]; segments.clear(); score=0
    if head.distance(food)<20:
        food.goto(random.randint(-290,290), random.randint(-290,290))
        seg=turtle.Turtle(); seg.shape("square"); seg.color("lightgreen"); seg.penup(); segments.append(seg)
        score+=10; high=max(high,score)
    for i in range(len(segments)-1,0,-1): segments[i].goto(segments[i-1].pos()) 
    if segments: segments[0].goto(head.pos())
    move()

    pen.clear(); pen.write(f"Score:{score} High:{high}", align="center", font=("Courier",20,"normal"))
    time.sleep(delay)
    
  