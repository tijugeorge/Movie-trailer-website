import turtle

def draw_figure():
	window = turtle.Screen()
	window.bgcolor("aquamarine2")

	george = turtle.Turtle()
	george.shape("turtle")
	george.color("red")
	george.speed(10)

	for i in range(72):
		george.right(5)
		for i in range(2):
			george.forward(50)
			george.right(30)
			george.forward(100)
			george.right(150)

	george.right(90)
	george.forward(200)

	window.exitonclick()


draw_figure()

