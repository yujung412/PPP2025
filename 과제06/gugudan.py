#2)숫자를 입력받아, 해당하는 구구단을 출력하는 함수 gugudan(dan)를 만드는 프로그램
def main():
    def gugudan(dan):
        for i in range(1, 10):
            print(f"{dan} * {i} = {dan * i}")

    num = int(input("출력할 구구단의 숫자를 입력하시오: "))
    gugudan(num)

# 프로그램 실행
if __name__ == "__main__":
    main()
