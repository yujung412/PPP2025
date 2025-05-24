import random

def get_lotto():
     lotto_list = []
     while True:
        n= random.randint(1,45)
        if n not in lotto_list:
            lotto_list.append(n)
        if len(lotto_list)==6:
            break
     return sorted(lotto_list)



def main():
        lotto_num=get_lotto()
        print(lotto_num)


if __name__ == "__main__":
     main()