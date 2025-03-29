#3)섭씨를 화씨로 바꾸는 함수 c2f(t_c) 함수를 만드는 프로그램
def c2f(tc):
    return (tc * 9/5) + 32

def main():
    temp_c = float(input("섭씨 온도를 입력하세요: "))  # 사용자로부터 섭씨 값 입력 받기
    temp_f = c2f(temp_c)

    print(f"{temp_c}℃ => {temp_f}F")

if __name__ == "__main__":
    main()