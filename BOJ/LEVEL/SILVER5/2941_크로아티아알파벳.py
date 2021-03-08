s = input()


def countChroatia(s):
    tmp = s
    answer = 0
    check = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    for c in check:
        answer += tmp.count(c)
        tmp = tmp.replace(c, ',')
        # print(tmp, c, answer)
    answer += len(tmp.replace(',', ''))

    return answer


print(countChroatia(s))
