import turtle

def draw_figure():
	window = turtle.Screen()
	window.bgcolor("aquamarine2")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("red")
	brad.speed(9)

	for i in range(37):
		brad.right(10)
		for i in range(4):
			brad.forward(100)
			brad.right(90)

	window.exitonclick()

draw_figure()