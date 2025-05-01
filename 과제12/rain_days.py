import requests

def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))
    return weather_datas

def count_rain_days_over_5mm(rainfalls):
    count = 0
    for rain in rainfalls:
        if rain >= 5:
            count += 1
    return count

def main():
    URL = "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"
    filename = "./weather(146)_2020-2020.csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)

    rainfalls = get_weather_data(filename, 9)
    count = count_rain_days_over_5mm(rainfalls)
    with open("result_rain_over5mm_2020.txt", "w", encoding="utf-8") as f:
        print(f"5mm 이상 강우일수는 {count}일입니다.")

if __name__ == "__main__":
    main()

