word = input("Enter a string: ")

if word.endswith("ing"):
    print(word + "ly")
else:
    print(word + "ing")