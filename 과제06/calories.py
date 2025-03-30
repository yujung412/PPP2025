#1)메인 함수를 이용하여 칼로리 계산 프로그램(과제#04-03)를 수정하여, 총 칼로리를 계산하는 프로그램 (반복문, 사전 활용)
def main():
    fruit_cal = {"한라봉": 50 / 100, "딸기": 34 / 100, "바나나": 77 / 100}
    fruit_eat = {"한라봉": 150, "딸기": 200, "바나나": 120}

    total_calories = 0
    for fruit, weight in fruit_eat.items():
        total_cal = weight * fruit_cal[fruit]
        print(f"{fruit} 칼로리: {total_cal:.2f} kcal")
        total_calories += total_cal

    print(f"총 칼로리: {total_calories:.2f} kcal")

if __name__ == "__main__":
    main()
