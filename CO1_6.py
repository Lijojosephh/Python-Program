names = input("Enter names separated by space: ").split()

count = 0

for name in names:
    count = count + name.lower().count("a")

print("Number of a:", count)