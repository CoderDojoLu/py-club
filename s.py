import turtle
turtle.speed(9)
turtle.setpos(0,0)
distance = 120
angle = 10
for i in range(1000):
	turtle.forward(distance)
	turtle.left(angle)
	angle = angle + 5