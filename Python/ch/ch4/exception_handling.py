while True:
    try:
        num1= int(input("첫 번째 숫자를 입력해주세요."))
        num2= int(input("두 번째 숫자를 입력해주세요."))
        result = num1 / num2

        print(f"나누기 결과는 {result} 입니다.")
    except ValueError:
        print(f"정상적인 숫자를 입력하세요.")
        continue
    except ZeroDivisionError:
        print(f"0으로 나눌 수 없습니다.")
        continue
    except:
        pass
        