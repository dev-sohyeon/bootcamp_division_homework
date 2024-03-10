"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    while True:
        n = input("")
        if not n.isdigit():
            print("X")
            continue
        else:
            n = int(n)
            if n <= 0:
                print("X")
                continue
            else:
                break

    total = 0
    for i in range(1, n+1):
        total += i

    print(total)

    return


if __name__ == '__main__':
    main()
