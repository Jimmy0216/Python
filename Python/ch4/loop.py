# 팩토리얼 구하기
# n! = n * (n -1) * ... * 2 * 1
# 5! = 5 * 4 * 3 * 2 * 1
num = 10
result = 1

for i in range(1, num+1):
    result = result * i

print(f"{num}! 은 {result}입니다.")

# enumerate 활용
# fruits = ["Apple", "Banana", "Blueberry", "Peach"]

# index = 1
# for index, fruit in enumerate(fruits, start=1):
#     print(f"{index}번째 과일은 {fruit}입니다.")

# 구구단 프로그램
# # 1~9단, n * 1 ~ n * 9
# for x in range(1, 10):
#     for y in range(1, 10):
#         print(f"{x} * {y} = { x * y}")

# while True:
#     user_input = input("명령어를 입력해주세요:")
#     if user_input == "exit":
#         break
#     else:
#         pass # todo: 차후 개발 예정


# fruits = ["사과", "딸기", "복숭아", "참외"]

# for fruit in fruits:
#     if fruit == "사과":
#         print(f"사과는 맛있습니다.")

#     print(f"{fruit}이(가) 과일 바구니에 있습니다.")

# for loop
# for i in range(1, 5):
#     print(i)
# else:
#     print("반복이 완료되었습니다.")

# while
# i = 0 # 겂을 초기화 해줘야함
# while i < 5:
    # print(i)
    # i = i + 1