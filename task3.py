import turtle

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()


lines = [
    ("Hello, World!", 60, "Calibri", "red"),
    ("Hello, World!", 0, "Arial", "blue"),
    ("Hello, World!", -60, "Poppins", "green")
]

for text, y, font, color in lines:
    pen.goto(-100, y)
    pen.color(color)
    pen.write(text, font=(font, 24, "normal"))

turtle.done()