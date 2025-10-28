import itertools as it
import random
from fractions import Fraction as f

E = {0,1,2,3,4,5}
#a
three_digit_numbers = list(it.product(E, repeat=3))
print("a) 3 digits numbers",three_digit_numbers)
print()
#b
four_digit_numbers = list(it.permutations(E, 4))
print("b) 4 digits numbers with pairwise different digits:", four_digit_numbers)