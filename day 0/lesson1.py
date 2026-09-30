from turtle import *

# we want to draw a house

# walls

width(7)
color("red")
speed(10)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#end wall

#door ask teacher about overlap

penup()
goto(70, 0)
pendown()
color("green")
left(90)
forward(80)
right(90)
forward(60)
right(90)
forward(80)

#end door

#roof
penup()
goto(200, 200)
pendown()

color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end roof

#window
color("purple")
penup()
goto(30, 120)
pendown()
right(240)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
#start win lines
penup()
goto(30, 150)
pendown()
left(90)
forward(60)
penup()
goto(60, 180)
pendown()
right(90)
forward(60)

#win 2

penup()
goto(170, 180)
pendown()
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
penup()
goto(170, 150)
pendown()
left(180)
forward(60)
penup()
goto(140, 180)
pendown()
left(90)
forward(60)
#end win

#end house


exitonclick()





