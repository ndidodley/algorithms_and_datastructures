def solution(s):
    i = len(s)
    if i == 1:
        return int(s)
    else:
        part = int(s[0]) * (1*10**(i-1))
        rest = solution(s[1:])
        return part + rest


if __name__ == '__main__':
    s = input('Please enter number to convert to string\n')
    print('The number represented is {}'.format(solution(s)))
