import random

# 초성 리스트 (유니코드 한글 음절 기준)
CHOSUNG_LIST = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ',
    'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ',
    'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

# 한 글자의 초성 반환
def to_chosung_ch(ch):
    if '가' <= ch <= '힣':  # 한글일 때만 처리
        return CHOSUNG_LIST[(ord(ch) - ord('가')) // 588]
    else:
        return ch  # 한글이 아니면 그대로 반환

# 문자열 전체 초성 반환
def to_chosung(text):
    return "".join(to_chosung_ch(ch) for ch in text)

def main():
    problems = ["바나나", "딸기", "토마토", "복숭아"]
    solution = random.choice(problems)
    hint = to_chosung(solution)  # 초성 힌트 만들기

    is_correct = False
    for i in range(3):
        answer = input(f"문제: {hint} → ")
        if answer == solution:
            print("정답입니다.")
            is_correct = True
            break
        else:
            print("오답입니다.")

    if is_correct:
        print("잘하셨습니다.")
    else:
        print(f"게임오버. 정답은 '{solution}'였습니다.")

if __name__ == "__main__":
    main()
