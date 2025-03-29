#4) 삼각함수 표를 만드는 프로그램램

import math

print("각도  | sin     | cos     | tan")
print("-" * 40)

for angle in [0, 30, 45, 60, 90]:
    radian = math.radians(angle)
    
    sin = math.sin(radian)
    cos = math.cos(radian)
    tan = math.tan(radian) if cos != 0 else 'undefined'
    
    print(f"{angle:5}° | {sin:7.4f} | {cos:7.4f} | {tan:7.4f}")
