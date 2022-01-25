'''
Write a program that reads a positive integer, n, from the user and then displays the sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:
sum = (n)(n + 1) 2
'''

#read input n value from the user
Num = int(input("please enter a positive integer to compute the sum of first n integers:"))

#Calculate the sum 
sum = ((Num)*(Num+1))/2

#print the sum of integers
print(f'The sum of first {Num} positive integers is:{ sum}')