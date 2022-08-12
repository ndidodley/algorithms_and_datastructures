def solution(S) -> list:
    if len(S) == 1:
        return [S[0], S[0]]

    else:
        part = S[0]
        rest = solution(S[1:])
        if part > rest[1]:
            rest[1] = part
        if part < rest[0]:
            rest[0] = part
        return rest


if __name__ == '__main__':
    S = input("Please insert comma seperated values of numbers to be compared \n")
    S = S.split(',')
    ans = solution([int(i) for i in S])
    print('The min and max numbers in the sequence respectively are {}'.format(ans))
