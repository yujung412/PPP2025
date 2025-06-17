import tkinter as tk

# 퀴즈 목록
quiz_list = [
    ("Q1. 보물지도의 첫 번째 단서! ‘달빛 아래 선반 위에 숨겨진 빛’ 어디를 찾아야 할까?",
     "b", ["a. 등대 꼭대기", "b. 선실의 유리병 선반"]),
    ("Q2. 선실에 들어갔는데, 갑자기 함정이 작동했다! 어떻게 피할까?",
     "a", ["a. 즉시 뒤로 뛰어내린다", "b. 벽을 밀어 함정 해제 버튼을 누른다"]),
    ("Q3. 함정을 빠져나오니 바닥에 오래된 해적일기장이 있다. 어떻게 할까?",
     "b", ["a. 무시하고 앞으로 간다", "b. 일기장을 펼쳐 다음 단서를 찾는다"]),
    ("Q4. 일기장에 적힌 암호를 해독해야 한다! ‘바람과 파도 사이 숨겨진 숫자’ 무엇일까?",
     "a", ["a. 314", "b. 42"])
]

quiz_index = 0
wrong_tries = 0
max_tries = 3

def center(win, width, height):
    screen_w = win.winfo_screenwidth()
    screen_h = win.winfo_screenheight()
    x = (screen_w - width) // 2
    y = (screen_h - height) // 2
    win.geometry(f"{width}x{height}+{x}+{y}")

def get_fail_message(index):
    messages = [
        "등대는 가짜였고 해적들이 우릴 기다리고 있었다... 🫠",
        "함정에 걸려서 바닥에 떨어졌다... 🫠",
        "일기장을 무시하고 길을 잃었다... 🫠",
        "암호를 틀려서 함정이 다시 작동했다... 🫠"
    ]
    return messages[index]

def show_question():
    question, _, choices = quiz_list[quiz_index]
    question_label.config(text=question)
    button1.config(text=choices[0], command=lambda: check_answer('a'))
    button2.config(text=choices[1], command=lambda: check_answer('b'))

def check_answer(user_choice):
    global quiz_index, wrong_tries

    correct = quiz_list[quiz_index][1]

    if user_choice != correct:
        wrong_tries += 1
        remaining = max_tries - wrong_tries

        if remaining > 0:
            msg = f"❌ 실패! {get_fail_message(quiz_index)}\n남은 기회: {remaining}번\n처음부터 다시 시작합니다."
            show_popup("실패", msg, retry=True)
        else:
            msg = f"❌ 실패! {get_fail_message(quiz_index)}\n기회를 모두 사용했습니다.\n게임을 종료합니다."
            show_popup("게임 오버", msg, retry=False)
        return

    quiz_index += 1
    if quiz_index < len(quiz_list):
        show_question()
    else:
        show_popup("성공!", "🏴‍☠️ 성공! 해적 보물을 찾았다! 🎉", retry=False)

def restart(retry_all=False):
    global quiz_index, wrong_tries
    quiz_index = 0
    if retry_all:
        wrong_tries = 0
    show_question()

def show_popup(title, message, retry):
    popup = tk.Toplevel(root)
    popup.title(title)
    popup.configure(bg="#273746")
    center(popup, 440, 210)

    label = tk.Label(popup, text=message, font=("Arial", 15, "bold"), fg="#f0e6d2", bg="#273746",
                     wraplength=400, justify="center")
    label.pack(pady=30)

    def close_popup():
        popup.destroy()
        if retry:
            restart(retry_all=False)
        else:
            root.destroy()

    btn_text = "다시 시도" if retry else "게임 종료"
    button = tk.Button(popup, text=btn_text, font=("Arial", 13, "bold"),
                       bg="#145b6e", fg="#f0e6d2",
                       activebackground="#0f4650", activeforeground="#f0e6d2",
                       command=close_popup, width=15, relief="flat")
    button.pack(pady=10)

    popup.transient(root)
    popup.grab_set()

def main():
    global root, question_label, button1, button2

    root = tk.Tk()
    root.title("Pirate Treasure Hunt")
    center(root, 520, 350)
    root.configure(bg="#1b263b")

    title = tk.Label(root, text="🏴‍☠️ Pirate Treasure Hunt", font=("Arial", 22, "bold"), fg="#f0e6d2", bg="#1b263b")
    title.pack(pady=15)

    question_label = tk.Label(root, text="", font=("Arial", 16), fg="#f0e6d2", bg="#1b263b", wraplength=480, justify="center")
    question_label.pack(pady=30)

    button1 = tk.Button(root, text="", width=42, font=("Arial", 14), bg="#145b6e", fg="#f0e6d2", relief="flat",
                        activebackground="#0f4650", activeforeground="#f0e6d2")
    button1.pack(pady=10)

    button2 = tk.Button(root, text="", width=42, font=("Arial", 14), bg="#145b6e", fg="#f0e6d2", relief="flat",
                        activebackground="#0f4650", activeforeground="#f0e6d2")
    button2.pack(pady=10)

    show_question()
    root.mainloop()

if __name__ == "__main__":
    main()
