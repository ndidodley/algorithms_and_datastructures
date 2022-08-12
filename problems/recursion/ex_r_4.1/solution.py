def solution(S):
    if len(S) == 1:
        return S[0]
    max = S[0]
    rest = solution(S[1:])
    if max > rest:
        return max
    else:
        return rest


if __name__ == '__main__':
    S = input('Please enter a comma, seperated list of values, \n')
    S = S.split(',')
    print(S)
    ans = solution([int(i) for i in S])
    print('\n The maximum number in the list is {} \n'.format(ans))
