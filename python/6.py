"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 사용자로부터 알파벳 문자 하나를 입력받습니다.
    user_input = input("")

    # 입력받은 문자가 모음인지 판별합니다.
    if user_input in ['a', 'e', 'i', 'o', 'u']:
        print("O")  # 모음일 경우 'O'를 출력합니다.
    else:
        print("X")  # 그 외의 경우 'X'를 출력합니다.

    return


if __name__ == '__main__':
    main()
