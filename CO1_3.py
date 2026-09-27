#positive number
numbers=[-10,15,-3,8,0,22,-5]
positive_numbers=[x for x in numbers if x>0]
print("Positive numbers:",positive_numbers)

#Square of N numbers
n=5
squares=[x*x for x in range(1,n+1)]
print("squares of n numbers:",squares)

#list of vowels from given word
word="python programming"
vowels=[char for char in word if char in "aeiouAEIOU"]
print("vowels in the word",vowels)

#list of ordinal value of each elements of a word
word="hello"
ordinal_Values=[ord(char)for char in word]
print("ordinal values:",ordinal_Values)