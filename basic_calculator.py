'''
Exercise 10: Arithmetic
(Solved—20 Lines) Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• Thesumofaandb
• The difference when b is subtracted from a 
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of ab

'''
#import modules
import math as ma

a = int(input('please enter a first number to compute:'))
b = int(input('please enter a second number to compute:'))

# addition
sum = a+b
print(f'Sum of {a} + {b} is: {sum}')

#subtraction
sub = a-b
print(f'Subtraction of {a} - {b} is: {sub}')

#product
prod = a*b
print(f'product of {a} * {b} is: {prod}')

#quotient // returns the integer value
quo = a//b
print(f'Quotient of {a} // {b} is: {quo}')

#remainder
rem = a%b 
print(f'Remainder of {a} % {b} is: {rem}')

#log value
log_10 = ma.log10(a)
print(f'Log to the base 10 value of {a}: {log_10}')

#expoent
expo = a**b
print(f'Exponent of {a} ** {b} :{expo}')

