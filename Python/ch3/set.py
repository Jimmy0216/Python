# fruits = {"apple", "banana", "blueberry"}
# print(fruits)

# fruits.add("orange")
# print(fruits)

# fruits.remove("banana")
# print(fruits)

frutis1 = {"apple", "strawberry", "peach"}
frutis2 = {"banana", "strawberry", "orange"}

# 합집합
union = frutis1.union(frutis2)
print("합집합:", union)
# print(frutis1 | frutis2)

# 교집합
intersection = frutis1.intersection(frutis2)
print("교집합:", intersection)

# 차집합
diff1 = frutis1.difference(frutis2)
diff2 = frutis2.difference(frutis1)
print("차집합 f1 - f2", diff1)
print("차집합 f2 - f1", diff2)

# empty_set = set() # {}이라고하면 set이 아니라 dictionary로 인식함
# my_set = {1,2,3,3} # {1,2,3}

# print(my_set)