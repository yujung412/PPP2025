def caesar_encode_ch(ch, shift):
    if 'A' <= ch <= 'Z':
        return chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
    elif 'a' <= ch <= 'z':
        return chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
    else:
        return ch

def caesar_encode(text: str, shift: int = 3) -> str:
    return "".join(caesar_encode_ch(ch, shift) for ch in text)

def caesar_decode(text: str, shift: int = 3) -> str:
    return caesar_encode(text, -shift)

def main():
    text = input("암호화할 문자열을 입력하세요: ")
    encoded = caesar_encode(text, 3)
    decoded = caesar_decode(encoded, 3)

    print(f'caesar_encode("{text}") == "{encoded}"')
    print(f'caesar_decode("{encoded}") == "{decoded}"')

if __name__ == "__main__":
    main()
