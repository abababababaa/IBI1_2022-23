# The goal of this code is to determine the total number of components in 5 situations using a formula.
# With n being the sequence number and h being the outcome in each instance, a loop was configured to handle 5 cases.

# Create a loop from 1 to 5
for n in range(1,6):
    # Create formulas using known rules
    h = 2*n*(2*n-1)/2
    print(h)
  
""" output:   1.0
              6.0
              15.0
              28.0
              45.0
"""
