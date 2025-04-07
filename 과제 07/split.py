def average(nums):
    return sum(nums) / len(nums)

def main():
    numbers_input = input("숫자를 구분하여 입력하세요: ")
    
    nums = numbers_input.split(",")
    
    num_list = []
    for num in nums:
        num_list.append(int(num)) 
    
  
    print(f"평균은 {average(num_list)}입니다.")

if __name__ == "__main__":
    main()
