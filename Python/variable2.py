# 사용자로부터 문자열 입력받기
inp = input("값을 입력해주세요.")

# 이 값을 1더해서 출력하기
num = int(inp) + 1

print(f"입력받은 값에 1을 더하면, {num}입니다.")
# 깃 테스트

# print("숫자를 입력해주세요.")
# num = input("숫자를 입력해주세요.") # 하지만 이것은 숫자가 아니라 문자임
# print(num)

# Format string
# weather = "흐림"
# temp = 15.8

# % code (%s, %d, %f)
# res = "오늘 날씨는 %s 입니다. 기온은 %f도 입니다." % (weather, temp)
# res = "[%s / %f도] 오늘 날씨는 %s 입니다. 기온은 %f도 입니다." % (weather, temp, weather, temp)
# print(res)

# # .format()
# res = "오늘 날씨는 {} 입니다. 기온은 {}도 입니다.".format(weather, temp)
# res = "기온은 {1}도 입니다. 오늘 날씨는 {0} 입니다.".format(weather, temp)
# res = "[{0} / {1}도] 기온은 {1}도 입니다. 오늘 날씨는 {0} 입니다.".format(weather, temp)

# print(res)

# f"""
# res = f"오늘 날씨는 {weather} 입니다. 기온은 {temp}도 입니다."
# print(res)


# 문자열 변수 선언
# str_var = "This is my python code."

# print(str_var.upper())
# print(str_var.swapcase())
# print(str_var.replace("my", "your"))

# str_var2 = "Thisismypythoncode"
# num_var = "12"
# num_var2 = "12 "

# print(str_var.isalpha())
# print(str_var2.isalpha()) # 오로지 알파뱃만 있을때 True
# print(num_var.isdecimal()) # 오로지 숫자만 있을때 True
# print(num_var2.isdecimal())

# 인덱싱
# print(str_var[11]) # p
# print(str_var[-1]) # .
# print(str_var[-5]) # c

# 슬라이싱
# print(str_var[11:17])
# print(str_var[11:-6])
# print(str_var[:10])

# 문자열 더하기
# inum1 = 12
# inum2 = 23
# print(inum1 + inum2)

# snum1 = "12"
# snum2 = "34"

# print(snum1 + snum2)
# print(snum1 * 3) 

# multi_line = """I'm a devleoper.
# I use python.
# Thang you."""

# print(str_var)
# print(multi_line)

