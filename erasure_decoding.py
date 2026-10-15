import numpy as np
from common import H, tanner_sets

def erasure_decode(y, H, max_iter=50):
    m, n = H.shape # Gets the dimensions of the parity check matrix
    B, A = tanner_sets(H) # Reads H, and builds two lists:
                          # B: for each check j, the bits in that check (the 1s in row j)
                          # A: for each bit i, the checks that bit belongs to (the 1s in column i)
    M = np.array(y) # Current bit values (0, 1, or -1 for erased)
    E = np.full((m, n), -1) # Creates a m x n matrix (same shape as parity check matrix) and fills it with -1

# Step 1: each check tells each of its bits what value it should be
    for j in range(m): # go through every check
        for i in B[j]: # go through every bit in check j
            others = [k for k in B[j] if k != i] # the other bits in check j (everything except bit i)
            if (M[others] != -1).all(): # if none of the other bits are erased...
                E[j, i] = M[others].sum() % 2 # ...bit i must be their XOR (makes the check's parity even)
    return M, E

