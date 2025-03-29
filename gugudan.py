#1) 숫자를 입력받아, 입력받은 숫자의 구구단을 출력하는 프로그램
num=int(input("출력할 구구단의 숫자를 입력하시오:"))

for i in range(1,10):
    print(f"{num}*{i}={num*i}")