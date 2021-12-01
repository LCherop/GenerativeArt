from turtle import *

lineLen = 100
spacing = 0.1

color('purple')
fillcolor('black')
hideturtle()

def left_to_right_lines():
    for right in range(24):
        forward(lineLen)
        rt(90)
    for down in range(24):
        fd(10)
        rt(5)
    rt(180)   

begin_fill()
for i in range(150):
    left_to_right_lines()   
    color('purple')
fillcolor('black') 
end_fill()

