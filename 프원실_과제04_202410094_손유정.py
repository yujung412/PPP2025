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



#2)x, y를 입력받아서, 어느 사분면인지 출력하는 프로그램
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



#4)칼로리 계산 프로그램을 사전형(딕셔너리)를 이용하여 구현하는 프로그램램
fruit_calories = {
    "한라봉": 50,    # 한라봉 100g당 칼로리
    "딸기": 34,      # 딸기(설향) 100g당 칼로리
    "바나나": 77     # 바나나 100g당 칼로리
}

fruit_weights = {
    "한라봉": float(input("한라봉 섭취량 (g): ")),
    "딸기": float(input("딸기 섭취량 (g): ")),
    "바나나": float(input("바나나 섭취량 (g): "))
}

for fruit, weight in fruit_weights.items():
    total_cal = (weight / 100) * fruit_calories[fruit]
    print(f"{fruit} 칼로리: {total_cal:.2f} kcal")



#4)반지름을 입력받아서, 원의 둘레와 원의 면적을 출력하는 프로그램
import math

r = int(input("반지름을 입력하시오: "))
pi = math.pi

circumference = 2 * pi * r
area = pi * r ** 2

print("반지름이 {}인 원의 둘레는 {}입니다.".format(r, circumference))
print("반지름이 {}인 원의 면적은 {}입니다.".format(r, area))