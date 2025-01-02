# 키워드 가변인자 리스트
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Eve", age="36", city="Dubiln")

info = {"name": "Charlie", "age": 35, "City": "Tokyo"}
print_info(**info)

 # 가변 인자 리스트
# def calc_sum(*args):
#     total = 0
#     for arg in args:
#         total += arg    # total = total + arg
#     return total
# print(calc_sum(1, 2, 3, 4))
# print(calc_sum(10, 100))

# 키워드 인자
# def dispaly_info(name, age, city):
#     print(f"Name: {name}, Age: {age}, City: {city}")

# dispaly_info("Alice", 30, "LA")
# dispaly_info(city="Paris", name="Bob", age=22)

# 기본 매개변수
# def welcome(city, name="Guest", room=None):
#     if room == None:
#         room = []

#     room.append(101)
#     print(f"Hello, {name}! This is {city}. You can use {room}.")

# welcome("New York")
# welcome("Seattle", "John")