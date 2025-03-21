#1)섭씨를 화씨로 변환하는 프로그램 (input 이용)
temp_c=int(input("섭씨를 입력하시오:"))
temp_f=(temp_c*9/5)+32

print("{}℃ => {}Ｆ". format(temp_c, temp_f))



#2)BMI를 구하기 (input 이용, math 이용)
import math

height=int(input("키를 입력하시오:"))/100 #cm->m
weight=int(input("몸무게를 입력하시오:"))
BMI=weight/math.pow(height,2)

print("키는 {}, 몸무게는 {}, BMI는 {}".format(height, weight, BMI))



#3)원의 면적을 구하는 프로그램 (input 이용, math 이용)
import math
r=int(input("반지름을 입력하시오:"))
pi=math.pi
area=pi * r ** 2
print("반지름이 {}인 원의 면적은 {}입니다". format(r, area))



#4)사다리꼴의 면적을 구하는 프로그램 (input 이용)
import math

upper=int(input("윗변을 입력하시오:"))
lower=int(input("아랫변을 입력하시오:"))
height=int(input("높이를 입력하시오:"))

area=math.sqrt(((upper+lower)*height)**2)/2

print("윗변={}, 아랫변={}, 높이={} 일때". format(upper, lower, height))
print("사다리꼴의 면적은 = {}". format(area))



#5)칼로리 구하기 (과일마다 섭취 g를 입력받아서 칼로리 출력하기)
hallabong_cal = 50  # 한라봉 100g당 칼로리
strawberry_cal = 34  # 딸기(설향) 100g당 칼로리
banana_cal = 77  # 바나나 100g당 칼로리

hallabong_weight = float(input("한라봉의 섭취량을 입력하시오: "))
strawberry_weight = float(input("딸기의의 섭취량을 입력하시오: "))
banana_weight = float(input("바나나의 섭취량을 입력하시오: "))

hallabong_total_cal = (hallabong_weight / 100) * hallabong_cal
strawberry_total_cal = (strawberry_weight / 100) * strawberry_cal
banana_total_cal = (banana_weight / 100) * banana_cal

print("한라봉 칼로리: {}".format(hallabong_total_cal))
print("딸기 칼로리: {}".format(strawberry_total_cal))
print("바나나 칼로리: {}".format(banana_total_cal))



#6)두 지점 사이 거리 구하기(x1, y1, x2, y2를 각각 입력 받아서 두 지점의 거리를 출력하기)
import math

x1=int(input("x1의 좌표를 입력하시오:"))
x2=int(input("x2의 좌표를 입력하시오:"))
y1=int(input("y1의 좌표를 입력하시오:"))
y2=int(input("y2의 좌표를 입력하시오:"))

distance=math.sqrt((x2-x1)**2 +(y2-y1)**2)
print("거리는 : {}".format(distance))