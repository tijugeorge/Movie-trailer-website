import turtle

def draw_figures():
	window = turtle.Screen()
	window.bgcolor("aquamarine2")
	
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("red")   #https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm
	brad.speed(1)

	for i in range(4):
		brad.forward(100)
		brad.right(90)

	george = turtle.Turtle()
	george.shape("arrow")
	george.color("yellow")   #https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm
	george.speed(1)
	george.circle(100)

	angie = turtle.Turtle()
	angie.shape("turtle")
	angie.color("red")   #https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm
	angie.speed(1)
	
	for i in range(3):
		angie.backward(100)
		angie.left(120)

	window.exitonclick()


draw_figures()