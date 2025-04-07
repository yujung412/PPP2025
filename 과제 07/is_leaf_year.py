def is_leaf_year(y):
    if y%4==0:
        return True
    else:
        False

def main():
    y = 2024
    print(f"{y}년은 윤년인가? {is_leaf_year(y)}")

if __name__ == "__main__":
    main()
