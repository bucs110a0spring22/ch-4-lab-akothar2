import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
xmin = -360
xmax = 360
ymin = -1
ymax = 1

def drawSineCurve(dart):
  dart.color("blue")
  dart.down()
  for z in range (xmin, xmax+1, 1):
    dart.goto(z, math.sin(math.radians(z)))
  dart.up()
  dart.goto(xmin, 0)
  
def setupWindow(wn):
  wn.setworldcoordinates(xmin, ymin, xmax, ymax)
  wn.bgcolor("white")

def setupAxis(dart):
  dart.up()
  dart.color("brown")
  for z in (ymin, ymax):
    dart.goto(xmin, 0)
    dart.down()
    dart.goto(xmax, 0)
  dart.goto(xmin - 20, 0)
  dart.write("X")

  for z in range (xmin, xmax + 1, 45):
    if z==0 or z==xmin or z==xmax:
            dart.color("black")
    else:
      dart.color("grey")
      dart.goto(z, ymax)
      dart.down()
      dart.goto(z, ymin)
      dart.up()
      dart.goto(0, ymax)
      dart.write("Y")
      dart.goto(xmin, 0)
  dart.down()

def drawCosineCurve(dart):
  dart.color("red")
  dart.down()
  for z in range(xmin, xmax+1, 1):
    dart.goto(z, math.cos(math.radians(z)))
  dart.up()
  dart.goto(xmin, 0)
  
def drawTangentCurve(dart):
  dart.color("green")
  dart.down()
  for z in range(xmin, xmax+1, 1):
    dart.goto(z, math.tan(math.radians(z)))
  dart.up()
  dart.goto(xmin, 0)
      
##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()

main()

