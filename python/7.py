"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    def get_days_in_month(year, month):
        if month == 2:  # 2월인 경우
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                return 29  # 윤년인 경우 29일
            else:
                return 28  # 평년인 경우 28일
        elif month in [4, 6, 9, 11]:  # 4, 6, 9, 11월인 경우
            return 30  # 30일
        else:
            return 31  # 나머지 달은 31일

    year = int(input(""))
    month = int(input(""))

    days = get_days_in_month(year, month)
    print(days)


    return


if __name__ == '__main__':
    main()
