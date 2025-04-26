def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            weather_datas.append(float(tokens[col_idx]))
    return weather_datas

def get_weather_date(fname):
    weather_dates = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            weather_dates.append([int(tokens[0]), int(tokens[1]), int(tokens[2])])
    return weather_dates

def main():
    filename = "./weather(146)_2001-2022.csv"
    dates = get_weather_date(filename)
    tavg = get_weather_data(filename, 4)  # 평균기온은 4번 열

    years = []
    gdd_sums = []

    year = dates[0][0]
    gdd_sum = 0
    base_temp = 5

    for i in range(len(dates)):
        this_year = dates[i][0]
        month = dates[i][1]
        temp = tavg[i]

        if this_year != year:
            years.append(year)
            gdd_sums.append(gdd_sum)
            year = this_year
            gdd_sum = 0

        if 5 <= month <= 9:  # 5월~9월
            if temp > base_temp:
                gdd_sum += (temp - base_temp)

    # 마지막 연도 저장
    years.append(year)
    gdd_sums.append(gdd_sum)

    # 출력
    for i in range(len(years)):
        print(f"{years[i]} {gdd_sums[i]:.1f}")

if __name__ == "__main__":
    main()
