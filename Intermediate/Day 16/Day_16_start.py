from turtle import Turtle, Screen
from prettytable import PrettyTable

timmy = Turtle()
print(timmy)
# timmy.shape("circle")
# timmy.color("cyan")
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# myScreen = Screen()
# print(myScreen.canvheight)
# myScreen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)
