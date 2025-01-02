# 점수를 입력 받는다.
score_str = input("점수를 입력해주세요:")
score = int(score_str)

if score <= 99 and score >= 90:
    grade = "A"
elif score <= 89 and score >= 80:
    grade = "B"
elif score <= 79 and score >= 70:
    grade = "C"
elif score <= 69 and score >= 60:
    grade = "D"
elif score <= 59 and score >= 1:
    grade = "F"
else:
    grade = "None"

if grade is not None:
    print(f"등급은 {grade}입니다.")

# # 점수가 비정상 범위이면, 아무것도 실행하지 않는다.
# if score > 99 or score < 1:
#     print("잘못된 입력 값입니다.")

# # 점수의 각 등급에 따른 결과를 출력한다 (a:90-99, b:80-89, c:70-79 d: 60-69 f ~59)
# else:
#     if score >= 90:
#         print("A 등급")
#     elif score >= 80:
#         print("B 등급")
#     elif score >= 70:
#         print("C 등급")
#     elif score >= 60:
#         print("D 등급")
#     else:
#         print("F 등급")


# 사용자로부터 두 개의 값을 입력받는다.
# var1 = input("첫 번째 값을 입력해주세요:")
# var2 = input("두 번째 값을 입력해주세요:")

# # 입력 값을 숫자로 변환하는 과정
# num_val1 = int(var1)
# num_val2 = int(var2)


# 첫 번째 값이 크다면 win, 두 번째 값이 크다면 lose 를 출력
# 두 값이 같다면, draw를 출력
# if num_val1 > num_val2:
#     print("win")
# elif num_val1 < num_val2:
#     print("lose")
# else:
#     print("draw")
