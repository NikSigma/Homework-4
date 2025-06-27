import turtle

first_name = input("Введіть ваше ім'я: ")
last_name = input("Введіть ваше прізвище: ")
favorite_color = input("Введіть ваш улюблений колір(англійською):")


screen = turtle.Screen()
screen.title("Привітання")


pen = turtle.Turtle()
pen.hideturtle()     
pen.penup()          
pen.goto(0, 0)      


pen.color(favorite_color)
pen.write(f"{first_name} {last_name}", align="center", font=("Arial", 24, "bold"))


turtle.done()