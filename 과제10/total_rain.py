def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))
    return weather_datas


def get_weather_data_int(fname, col_idx):  # 년도를 읽는 함수
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(int(tokens[col_idx]))
    return weather_datas


def sumifs(rainfalls, years, selected=[2021, 2022]):  # 2021년, 2022년 강수량 합산
    total = 0
    for i in range(len(rainfalls)):
        rain = rainfalls[i]
        year = years[i]
        if year in selected:
            total += rain
    return total


def main():
    filename = "./weather(146)_2001-2022.csv"
    rainfalls = get_weather_data(filename, 9)
    years = get_weather_data_int(filename, 0)
    
    # 2021년과 2022년 강수량 합산
    total_rainfall_2021 = sumifs(rainfalls, years, selected=[2021])
    total_rainfall_2022 = sumifs(rainfalls, years, selected=[2022])
    
    print(f"2021년 총 강수량은 {total_rainfall_2021:.1f}mm 입니다.")
    print(f"2022년 총 강수량은 {total_rainfall_2022:.1f}mm 입니다.")


if __name__ == "__main__":
    main()
