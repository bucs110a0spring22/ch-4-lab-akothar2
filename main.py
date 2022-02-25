import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
y = math.sin(math.radians(270))
print(y)
z = math.sin(math.radians(360))
print(z)

wn = turtle.Screen()
fred = turtle.Turtle()
fred.goto(50,50)
fred.goto(-100,60)
fred.goto(-100,-75)
fred.goto(250,-75)
fred.goto(0,0)
wn.exitonclick()










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

