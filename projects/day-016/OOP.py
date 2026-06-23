import turtle
import another_module
print(another_module.another_variable)

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red", "green")
# timmy.forward(100)
# timmy.position()
# (100, 0.00)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
#
# table = PrettyTable()
# table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# table.add_row(["Adelaide", 1295, 1158259, 600.5])
# print(table)
#

table2 = PrettyTable()
table2.field_names = ["Pokemon Name", "Type"]
table2.add_row(["Pikachu", "Electric"])
print(table2)