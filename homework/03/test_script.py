from robotcz import *
from moum02_moudry import *

#3, 3
#4, 4
new_world(3, 3)
k = Karel()
"""
ensure_markers(k, 5)
step(k)

fill_in(k)

fill_in(k, False)

fill_the_board(k)

my_function_3(k, 1, True)
turn_right(k)
step(k)
"""
#print(test_ensure_markers(k))
#print(test_my_function_3(k))
#print(test_fill_the_board(k))
fill_in(k, True)

input("Press Enter to exit...")