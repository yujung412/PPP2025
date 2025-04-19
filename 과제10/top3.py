def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))
    return weather_datas

def main():
    filename="./weather(146)_2022-2022.csv"

    top3_tmax=sorted(get_weather_data(filename,3),reverse=True)[:3]
    top3_tmax=sorted(get_weather_data(filename,3))[-3:] #리스트를 뒤집는 방법 [::-1]
    print(f"가장 높았던 최고기온 3개는 {top3_tmax}입니다.")



if __name__ == "__main__":
    main()
