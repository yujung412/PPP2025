import pandas as pd

file_path = r"C:\code\ppp2025\weather_jeonju_1980_2024.csv"

# 문제 해결을 위한 설정
df = pd.read_csv(file_path, encoding='cp949', skiprows=7)

# 날짜 변환
df['날짜'] = pd.to_datetime(df['날짜'])


import matplotlib.pyplot as plt
import koreanize_matplotlib

birth_month = 11
birth_day = 28

df['월'] = df['날짜'].dt.month
df['일'] = df['날짜'].dt.day
df['연도'] = df['날짜'].dt.year

birthdays = df[(df['월'] == birth_month) & (df['일'] == birth_day)]

# 생일 날 기온 추이 시각화
plt.figure(figsize=(12,6))
plt.plot(birthdays['연도'], birthdays['평균기온(℃)'], marker='o', label='평균기온')
plt.plot(birthdays['연도'], birthdays['최저기온(℃)'], linestyle='--', label='최저기온')
plt.plot(birthdays['연도'], birthdays['최고기온(℃)'], linestyle='--', label='최고기온')

plt.title(f"{birth_month}월 {birth_day}일 생일 기온 변화")
plt.xlabel("연도")
plt.ylabel("기온 (℃)")
plt.legend()
plt.grid(True)
plt.show()