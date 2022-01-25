# Script to generate the random strings of random length 
from datetime import datetime
import random
import string

letters_set = string.ascii_letters+string.digits+string.punctuation #String will have combination of a-z,A-Z,0-9,Special characters
# current date and time
now = datetime.now()

timestamp = datetime.timestamp(now)
print("timestamp =", timestamp)
with open(f'/Users/sirisha/Python_practice/python_scripts/list_{timestamp}.txt','a') as f: # Output File
    for i in range(500): # 500 strings
        length = random.randint(10,1000) # random length
        str = ''.join(random.choice(letters_set) for j in range(length))  #string join function to concatenate each randomly generated letter
        f.write(str) #write string to the file
        f.write('\n') # Newline character
       

    