#program tp generate a raondom hexa decimal lnumber
import random
chars = '0123456789ABCDEF'
cont_color = ['#'+''.join(random.sample(chars,6)) for i in range(275)]
print(cont_color)
