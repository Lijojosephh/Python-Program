list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

# Same length
if len(list1) == len(list2):
    print("Both lists have same length")
else:
    print("Lists have different length")

# Same sum
if sum(list1) == sum(list2):
    print("Both lists have same sum")
else:
    print("Lists have different sum")

# Common value
common = False

for x in list1:
    if x in list2:
        common = True
        break

if common:
    print("A value occurs in both lists")
else:
    print("No common value")