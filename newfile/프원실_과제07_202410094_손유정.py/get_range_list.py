def get_range_list(n):
    return list(range(1, n+1))

def main():
    n = 10  
    result = get_range_list(n)
    print(f"1부터 {n}까지의 리스트: {result}")

if __name__ == "__main__":
    main()
