"""
Section 1.2.1 Encoding (pg 5-7)
"""

# Section 1.2.1 Encoding (pg 5-7)
# To distinguish between message bits and parity bits in the codeword, we 
# re-write the code parity-check constraints so that each one solves for a 
# different codeword bit

# Example 1.4 
# Code constraints from example 1.3: 
# c4 = c1 ⊕ c2
# c5 = c2 ⊕ c3
# c6 = c1 ⊕ c2 ⊕ c3

# The codeword bits c1, c2, and c3 contain the three bit message, c1, c2, and
# c3, while the codeword bits c4, c5 and c6 contain the three parity-check bits.

# Codeword is defined as c = uG where c is the codeword, u represents the 
# message bits, and G is called the generator matrix

