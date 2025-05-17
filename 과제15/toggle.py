def toggle_text(text: str) -> str:
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            result.append(chr(ord(ch) - 32))
        elif 'A' <= ch <= 'Z':
            result.append(chr(ord(ch) + 32))
        else:
            result.append(ch)
    return ''.join(result)

def main():
    user_input = input("문자열을 입력하세요: ")
    toggled = toggle_text(user_input)
    print("변환 결과:", toggled)

if __name__ == "__main__":
    main()
