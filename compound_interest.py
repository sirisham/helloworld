'''
Pretend that you have just opened a new savings account that earns 4 percent interest per year. The interest that you earn is paid at the end of the year, 
and is added to the balance of the savings account. 
Write a program that begins by reading the amount of money deposited into the account from the user. 
Then your program should compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places.
'''
deposit = int(input("Please enter the deposit amount:"))

# interest calculated for 3 years .Year after year
amt_1_year = deposit+(deposit*0.04)
amt_2_year = amt_1_year+(amt_1_year*0.04)
amt_3_year = amt_2_year+(amt_2_year*0.04)

print(f"Amount in Savings account after 1st year:{amt_1_year}")
print(f"Amount in Savings account after 2nd year:{amt_2_year}")
print(f"Amount in Savings account after 3rd year:{amt_3_year}")