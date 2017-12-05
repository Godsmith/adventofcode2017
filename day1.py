from util import input_rows


def main():
    print(solve_captcha(input_rows(1)[0]))


def solve_captcha(input_):
    digits = [int(current) for current, next_ in current_and_next(input_) if
              current == next_]
    return sum(digits)


def current_and_next(collection):
    for i, element in enumerate(collection):
        yield (element, collection[(i + 1) % len(collection)])


if __name__ == '__main__':
    main()
