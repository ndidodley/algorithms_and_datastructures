def solution(n):
    if n == 1:
        return float(1)

    else:
        curr = float(1/n)
        rest = solution(n-1)
        return rest + curr


if __name__ == '__main__':
    n = input('Please enter the ith harmonic number your want to find, \n')
    ans = solution(int(n))
    print('The {}th Harmonic number is {}'.format(n, ans))
