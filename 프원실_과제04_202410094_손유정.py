#1)BMI 계산결과에 따라 비만 정도를 표시하는 프로그램
import math

height=int(input("키를 입력하시오:"))/100 #cm->m
weight=int(input("몸무게를 입력하시오:"))
BMI=weight/math.pow(height,2)

print("키는 {}, 몸무게는 {}, BMI는 {}".format(height, weight, BMI))

if BMI < 23:
    print("정상 체중")
elif 23<=BMI<=24.9:
    print("비만 전단계")
elif 25<=BMI<=29.9:
    print("1단계 비만")
elif 30<=BMI<=34.9:
    print("2단계 비만")
else:
    print("3단계 비만")



#3)x, y를 입력받아서, 어느 사분면인지 출력하는 프로그램
x=int(input("x의 좌표를 입력하시오:"))
y=int(input("y의 좌표를 입력하시오:"))

if x>0 and y>0:
    print("입력한 좌표는 1사분면 입니다.")
elif x<0 and y>0:
    print("입력한 좌표는 2사분면 입니다.")
elif x<0 and y<0:
    print("입력한 좌표는 3사분면 입니다.")
elif x>0 and y<0:
    print("입력한 좌표는 4사분면 입니다.")