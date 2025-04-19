def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))
    return weather_datas


def get_max_rain_event_amount(rainfalls):  # 강우 이벤트 중 최대 강수량
    max_sum = 0
    current_sum = 0

    for rain in rainfalls:
        if rain > 0:
            current_sum += rain
        else:
            if current_sum > max_sum:
                max_sum = current_sum
            current_sum = 0

    if current_sum > max_sum:
        max_sum = current_sum

    return max_sum


def main():
    filename = "./weather(146)_2022-2022.csv"
    rainfalls = get_weather_data(filename, 9)
    max_rain_event = get_max_rain_event_amount(rainfalls)
    print(f"강우 이벤트 중 최대 강수량 = {max_rain_event:.1f}mm")


if __name__ == "__main__":
    main()
