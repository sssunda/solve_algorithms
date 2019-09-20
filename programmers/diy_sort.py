def solution(strings, n):
    answer = []

    strings.sort()
    string_dict = {}

    for s in strings:
        string_dict[s[n]] = string_dict.get(s[n], []) + [s]
    
    string_key = sorted(string_dict.keys())
    
    for k in string_key:
        answer += string_dict[k]

    return answer
if __name__ == '__main__':
    strings = ['sun', 'bed', 'car']
    # strings = ['abce', 'abcd', 'cdx']
    n = 1
    print(solution(strings, n))
    