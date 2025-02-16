import turtle
pen1  = turtle.Turtle()
pen2  = turtle.Turtle()
pen3  = turtle.Turtle()
pen4  = turtle.Turtle()

pen1.up()
pen1.goto(100,100)
pen1.down()
pen1.color("blue","green")


pen2.up()
pen2.goto(-100,100)
pen2.down()
pen2.color("yellow","red")


pen3.up()
pen3.goto(100,-100)
pen3.down()
pen3.color("black","orange")


pen4.up()
pen4.goto(-100,-100)
pen4.down()
pen4.color("purple","pink")

def box(pen):
  pen.begin_fill()
  for i in range(4):
    pen.forward(100)
    pen.left(90)
  pen.end_fill()
    
    
pens=[pen1,pen2,pen3,pen4]

for i in range(36):
  for pen in pens:
    box(pen)
    pen.right(10)
    
    

turtle.done()



  
    