numbers = input("Enter numbers separated by space: ").split()

result = []

for x in numbers:
    x = int(x)

    if x > 100:
        result.append("over")
    else:
        result.append(x)

print(result)