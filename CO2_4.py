import math

for n in range(1000, 10000):
    a = str(n)

    if int(a[0]) % 2 == 0 and int(a[1]) % 2 == 0 and int(a[2]) % 2 == 0 and int(a[3]) % 2 == 0:
        x = math.sqrt(n)

        if x == int(x):
            print(n)