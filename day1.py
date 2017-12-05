from util import input_rows


def main():
    print(solve_captcha(input_rows(1)[0]))
    print(solve_captcha_part_two(input_rows(1)[0]))


def solve_captcha(input_):
    return calculate_sum(input_, 1)


def solve_captcha_part_two(input_):
    offset = int(len(input_) / 2)
    return calculate_sum(input_, offset)


def calculate_sum(input_, offset):
    digits = [int(current) for current, halfway in current_and_offset(
        input_, offset) if current == halfway]
    return sum(digits)


def current_and_offset(collection, offset):
    length = len(collection)
    for i, element in enumerate(collection):
        yield (element, collection[(i + offset) % length])


if __name__ == '__main__':
    main()
