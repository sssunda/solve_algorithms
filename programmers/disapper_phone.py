def solution(phone_number):
    len_phone_number = len(phone_number)
    answer = '*' * (len_phone_number-4) + phone_number[len_phone_number - 4:]
    return answer

if __name__ == '__main__':
    phone_number = "01033334444"
    print(solution(phone_number))
    