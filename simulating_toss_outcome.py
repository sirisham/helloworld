from datascience import *
import numpy as np
import matplotlib.pyplot as plt
# An empty array to collect the simulated values
coin = make_array('Heads', 'Tails')
heads = make_array()

# Repetitions sequence
num_repetitions = 10000
repetitions_sequence = np.arange(num_repetitions)

# for loop
for i in np.arange(1, num_repetitions+1):
    
    # simulate one value
    outcomes = np.random.choice(coin, 100)
    num_heads = np.count_nonzero(outcomes == 'Heads')
    
    # augment the collection array with the simulated value
    heads = np.append(heads, num_heads)  

simulation_results = Table().with_columns(
    'Repetition', np.arange(1, num_repetitions+1),
    'Number of Heads', heads 
)
simulation_results
simulation_results.hist('Number of Heads', bins = np.arange(30.5, 69.6, 1))
plt.savefig('/Users/sirisha/Python_practice/python_scripts/Images/hist.png')