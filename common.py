# Contains H, syndrome(), tanner_sets()
import numpy as np

# Parity check matrix
H = np.array([[1, 1, 0, 1, 0, 0],
              [0, 1, 1, 0, 1, 0],
              [1, 0, 0, 0, 1, 1],
              [0, 0, 1, 1, 0, 1]])

# Syndrome of y: 
# s = Hy^T 
# Indicates which parity-check constraints are not satisfied
def syndrome(y, H):
    y = np.array(y)
    s = H @ y.transpose() #numpy matrix multiplication operator: @

    return s % 2

def tanner_sets(H):
    m, n = H.shape
    B = [] # Set of bits in check j (the position of the 1s in row j)
    for j in range(m):
        B.append(np.flatnonzero(H[j]).tolist())

    A = [] # Set of checks that include bit i (the positions of the 1s in column i)
    for i in range(n):
        A.append(np.flatnonzero(H[:, i]).tolist())

    return B, A


# Test for the syndrome(y, H) method
# if __name__ == "__main__":
#     # Should return: 0, 0, 0, 0
#     print(syndrome([0, 0, 1, 0, 1, 1], H)) 

#Test for the tanner_sets(H) method
if __name__ == "__main__":
    # Should return B[0] == [0, 1, 3]
    # Should return A[0] == [0, 2]
    B, A = tanner_sets(H)
    print("B =", B)
    print("A =", A)