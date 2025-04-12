def read_text(filename):
    with open(filename) as f:
        lines = f.readlines()

    nums = []
    for line in lines:
        line = line.strip()
        nums.append(int(line))  

    return nums

def average(nums):
    return sum(nums) / len(nums)

def median(nums):
    sorted_list = sorted(nums)
    return sorted_list[len(sorted_list) // 2]

def main():
    filename = "프원실_과제08_202410094_손유정.py/numbers.txt"
    nums = read_text(filename)

    print(f"1) 총 숫자의 개수: {len(nums)}개")
    print(f"2) 주어진 숫자의 평균: {average(nums):.1f}")
    print(f"3) 주어진 숫자의 최댓값: {max(nums)}")
    print(f"4) 주어진 숫자의 최솟값: {min(nums)}")
    print(f"5) 중앙값: {median(nums)}")

if __name__ == "__main__":
    main()





