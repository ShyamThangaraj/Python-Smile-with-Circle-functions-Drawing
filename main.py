import turtle

t1 = turtle.Turtle()

#function defn with 4 parameters
def smileyFace(x,y,l,c): 
  t1.speed(0)
  t1.penup()
  t1.goto(x,y)
  t1.pendown()
  t1.color(c)
  t1.begin_fill()
  t1.circle(l)
  t1.end_fill()
  #smile
    
  t1.seth(120)
  t1.fd(l/2)
  t1.seth(-30)
  t1.fd(-l/3)
  t1.color("black")
  t1.circle(l,90)
  t1.circle(l,-120)
  
  #left eye
  t1.penup()
  t1.seth(0)
  t1.fd(l/2)
  t1.seth(90)
  t1.fd(l/2)
  t1.color("black")
  t1.begin_fill()
  t1.circle(l/9)
  t1.end_fill()
  #call the function and pass
  #it 4 arguments
  
  #right eye
  t1.seth(0)
  t1.fd(l)
  t1.seth(90)
  t1.color("black")
  t1.begin_fill()
  t1.circle(l/9)
  t1.end_fill()

smileyFace(-50,10,90,"orange")
