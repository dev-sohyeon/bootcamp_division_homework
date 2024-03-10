"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    def calculate_sum_and_factorial(n):
        # 1부터 n까지의 정수의 합 계산
        total_sum = sum(range(1, n+1))
        
        # n! 계산
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
        
        # 결과 출력
        print(total_sum)
        print(factorial)

    # 사용자로부터 정수 n 입력 받기
    n = int(input(""))

    # 함수 호출하여 결과 출력
    calculate_sum_and_factorial(n)

    return


if __name__ == '__main__':
    main()
