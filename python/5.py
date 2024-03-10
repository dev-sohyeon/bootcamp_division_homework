"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 사용자로부터 나이와 키를 입력받음
    age = int(input(""))
    height = int(input(""))

    # 나이가 14세 이상이거나 키가 160cm 이상인 경우 입장 불가
    if age >= 14 or height >= 160:
        print("X")
    else:
        print("O")


    return


if __name__ == '__main__':
    main()
