'''
Exercise 11: Fuel Efficiency
(13 Lines) In the United States, fuel efficiency for vehicles is normally expressed in miles-per- gallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred kilometers (L/100 km). Use your research skills to determine how to convert from MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.

'''
#1mpg = 235.2l/100Km

ame_mpg_val = int(input('Please enter the fue efficency for vehicle in miles-per- gallon (MPG):'))

#This formula will convert the miles per gallon to liters per 100 kilometers
can_lt_per_100km = 235//ame_mpg_val

print(f'Equivalent Fuel efficency in canadian units:{can_lt_per_100km}')