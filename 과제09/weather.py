def read_db(filename):
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

    temp_list = []
    rain_list = []

    for line in lines[1:]:
        parts = line.strip().split(",")
        rain_list.append(float(parts[1]))
        temp_list.append(float(parts[4]))

    return temp_list, rain_list


def main():
    temp, rain = read_db("weather(146)_2022-2022.csv")

    total_temp = sum(temp)
    avg_temp = total_temp / len(temp)

    total_rain = sum(rain)
    rain_days = 0
    for r in rain:
        if r >= 5:
            rain_days += 1

    print(f"연 평균 기온: {round(avg_temp, 1)}도")
    print(f"5mm 이상 비 온 날: {rain_days}일")
    print(f"총 강우량: {round(total_rain, 1)}mm")


if __name__ == "__main__":
    main()
