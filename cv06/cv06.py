from collections import namedtuple

xyz = namedtuple("XYZ", "x y z")
t1 = xyz(1, 2, 3)
print(type(t1), "-", t1[1])
t2 = xyz(11, z=33, y=22)
print(t2.z)