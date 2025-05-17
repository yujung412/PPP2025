def str2int(text: str, default_value: int = -999) -> int:
    try:
        return int(text)
    except ValueError:
        print(f"무시된 입력: {text}")
        return default_value

def main():
    numbers = []
    user_input = input("X=? ")

    while user_input != "-1":
        num = str2int(user_input)

        if num > 0:
            numbers.append(num)

        user_input = input("X=? ")

    print(f"\n입력된 값은 {numbers} 입니다.")
    print(f"총 {len(numbers)}개의 자연수가 입력되었고,", end=" ")

    if len(numbers) > 0:
        average = sum(numbers) / len(numbers)
        print(f"평균은 {average}입니다.")
    else:
        print("평균은 계산할 수 없습니다.")

if __name__ == "__main__":
    main()
