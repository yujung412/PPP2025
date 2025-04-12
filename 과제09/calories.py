def read_db(filename):
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

    kcal_dict = {}
    for line in lines[1:]:
        name, kcal, gram = line.strip().split(",")
        kcal_per_gram = float(kcal) / float(gram)
        kcal_dict[name] = kcal_per_gram

    return kcal_dict


def main():
    db = read_db("calorie_db.csv")

    print("작물 이름과 양(g)을 입력하세요 (예: 바나나,100):")
    user_input = input()

    name, gram = user_input.split(",")
    gram = float(gram)

    if name in db:
        result = db[name] * gram
        print(f"{name} {gram}g의 열량은 {round(result, 1)}kcal 입니다.")
    else:
        print("그 작물은 목록에 없습니다.")


# 메인 함수 실행
if __name__ == "__main__":
    main()
