import random

def check(solution, answer, input_ch):

    is_correct=False
    for i in range(len(solution)):
        if solution[i] == input_ch:
            answer[i]= solution[i]
            is_correct=True

    return is_correct
            



def main():
    problems =["apple", "banana"]


    solution =problems[random.randrange(len(problems))]
    is_correct = False

    answer = ["_" for n in range(len(solution))]
    
    lives=5
    while True:
        input_ch= input(f"{''.join(answer)}?")

        if check(solution, answer, input_ch):
            print(f"{input_ch}가 포함되어 있습니다.")
        else:
            lives -= 1

        if "_" not in answer:
            is_correct = True
            break


        if lives<0:
            break

        if is_correct:
            print("잘하셨습니다.")
        else:
            print("게임오버, 다시해보세요")
    


        if answer == solution:
            print("정답입니다.")
            is_correct=True
            break
        else:
            print("오답입니다.")




if __name__ == "__main__":
    main()