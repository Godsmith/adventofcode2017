from util import input_rows

INPUT = input_rows(9)[0]


def score(s):
    return score_and_garbage_count(s)[0]


def score_and_garbage_count(s):
    level = 0
    result = 0
    garbage_count = 0
    in_garbage = False
    iterator = iter(s)
    for c in iterator:
        if c == '!':
            next(iterator, None)
            continue
        elif c == '>':
            in_garbage = False
        elif not in_garbage:
            if c == '{':
                level += 1
            elif c == '}':
                result += level
                level -= 1
            if c == '<':
                in_garbage = True
        else:  # in_garbage == True
            garbage_count += 1
    return result, garbage_count


if __name__ == '__main__':
    print(score_and_garbage_count(INPUT))
