import os
import p4_01b_ModuleDemo as m
from robotcz import *
# import turtle

number = 40
print(repr(number))
print(str(number))
print(f"{number=!r}")

print(os.getcwd())
print(m.text)
print(type(1))
print(type(m))
# t = turtle.Turtle()
# t.forward(100)
# input("Press enter to exit...")

# new_world(10,10)
new_world("0123456789", " .:…∷…:. #")
k = Karel()
input("Press Enter to exit...")