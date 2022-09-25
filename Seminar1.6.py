# n V y - V-or /\ and    not(1)
print('x y z F')

for x in range(2):
    for y in range(2):
        for z in range(2):
            f = x or y or z
            print(x, y, z, bool(f))