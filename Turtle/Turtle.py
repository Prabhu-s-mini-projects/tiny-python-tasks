# from turtle import  Turtle, Screen
#
# t_jack = Turtle()
# t_jack.shape("turtle")
# t_jack.color("azure")
# t_jack.forward(50)
# print(t_jack)
#
# # Game Area
# window  = Screen()
# #print(window.window_height())
# window.exitonclick()


from prettytable import PrettyTable

table  = PrettyTable()

#
# table.field_names = ["PokeMon Name", "Type"]
# table.add_rows(["Pikachu", "Electric"])
# table.add_rows(["Squirtle", "Water"])
# table.add_rows(["Charmander", "Fire"])

table.add_column("PokeMon",["pikachu", "squritle", "Charmander"])
table.add_column("type",["electric", "water", "Fire"])
table.align = 'l'



print(table)
