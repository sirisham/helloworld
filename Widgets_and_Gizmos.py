'''
Exercise 8: Widgets and Gizmos
(15 Lines) An online retailer sells two products: widgets and gizmos. Each widget weighs 75 grams. Each gizmo weighs 112 grams. Write a program that reads the number of widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order.
'''
import constant #constant values
#constant.WID_WT)
#constant.GIZ_WT)

#Reads input from the user
n_of_widgets = int(input("please enter the number of widgets:"))
n_of_gizmos = int(input("please enter the number of gizmos:"))

#calculate the weight
Tot = n_of_widgets*constant.WID_WT+n_of_gizmos*constant.GIZ_WT

print(f"Total weight of gazimos and widgets is: {Tot}")