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
    tmax = get_weather_data(filename, 3)
    tmin = get_weather_data(filename, 5)

    years = []
    max_gap_dates = []
    max_gaps = []

    year = dates[0][0]
    max_gap = tmax[0] - tmin[0]
    max_gap_date = dates[0]

    for i in range(1, len(dates)):
        this_year = dates[i][0]
        this_gap = tmax[i] - tmin[i]

        if this_year != year:
            years.append(year)
            max_gap_dates.append(max_gap_date)
            max_gaps.append(max_gap)

            year = this_year
            max_gap = this_gap
            max_gap_date = dates[i]
        else:
            if this_gap > max_gap:
                max_gap = this_gap
                max_gap_date = dates[i]

    years.append(year)
    max_gap_dates.append(max_gap_date)
    max_gaps.append(max_gap)

    for i in range(len(years)):
        print(f"{max_gap_dates[i][0]}/{max_gap_dates[i][1]:02d}/{max_gap_dates[i][2]:02d} {max_gaps[i]:.1f}")

if __name__ == "__main__":
    main()


