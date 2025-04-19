def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))
    return weather_datas


def get_rain_event(rainfalls):  # 최장연속강우일수 계산
    events = []
    c_days = 0
    for rain in rainfalls:
        if rain > 0:
            c_days += 1
        else:
            if c_days > 0:
                events.append(c_days)
            c_days = 0
    if c_days > 0:
        events.append(c_days)
    return events


def main():
    filename = "./weather(146)_2022-2022.csv"
    rainfalls = get_weather_data(filename, 9)
    max_consecutive_rain_days = max(get_rain_event(rainfalls))
    print(f"최장연속강우일수 = {max_consecutive_rain_days}일")


if __name__ == "__main__":
    main()
