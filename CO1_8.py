text = input("Enter a string: ")

first = text[0]

result = first + text[1:].replace(first, "$")

print(result)