import time

def count_down(count):

    count=10
    for n in range(count):
        print(f"{count - n}...", end="\r")
        time.sleep(1)
    print("Bomb!!")

def main():
    count_down(3)

if __name__ == "__main__":
    main()
