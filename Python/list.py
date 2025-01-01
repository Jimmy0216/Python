# 리스트의 요소 추가 및 제거
my_list = []
my_list.append(10)
my_list.append(11)
my_list.append(12)
# print(my_list) # [10, 11, 12]

my_list.extend([13, 14, 15])
# print(my_list) # [10, 11, 12, 13, 14, 15]
# del my_list[0]
# print(my_list)

max_value = max(my_list)
min_vlaue = min(my_list)
print(f"최대 값은 {max_value}, 최소 값은 {min_vlaue}이다.")


# # my_list.append([16, 17])
# # print(my_list) # [10, 11, 12, 13, 14, 15, [16, 17]]

# print(my_list[-1]) # [16, 17]

# 리스트 연산 (+,*)
# new_list = my_list + [0, 1, 2]
# print(new_list)

# multi_list = [0, 1, 3] * 3
# print(multi_list)

# 리스트의 정렬
# numbers = [4, 2, 1, 3, 8, 6, 7, 5]
# print("unsorted:", numbers)

# numbers.sort()
# print("sorted:", numbers)

# numbers.sort(reverse=True)
# print("sorted(revers):", numbers)

# fruits = ["banana", "apple", "blueberry", "cherry"]

# # 바나나가 포함됨?
# is_banana_included =  "banana" in fruits
# print(is_banana_included)

# # 체리는 어디있나?
# index_cherry = fruits.index("cherry")
# print(index_cherry)

# my_list = [30, 40, 50]
# my_list.append(10)
# my_list.append(15)
# my_list.append(20)

# sliced = my_list[3:]
# print(sliced)

# element = my_list[4]
# print(element)

# print(my_list)
# print(len(my_list))