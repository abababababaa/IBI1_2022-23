# The goal of this code is to determine how many generations it will take to breed 100 rabbits.
# There were two initial generations (N) and there were one original number of rabbits (N).
# The number of rabbits doubles (N = N * 2) with each subsequent generation (G = G + 1).
# As a consequence, generation(G) will be printed.

N = 2 # The original number of rabbits 
G = 1 # Generation of rabbits
# when rabbits number is larger than 100, end loop
while N <= 100:
    # every new generation the number of rabbits doubles
    G = G + 1
    N = N * 2
print(G)

# answer: it takes 7 generations
