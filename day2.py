from itertools import combinations

from util import input_lists


def main():
    print(sum(row_result1(row) for row in input_lists(2)))
    print(sum(row_result2(row) for row in input_lists(2)))


def row_result1(row):
    int_list = [int(n) for n in row]
    return max(int_list) - min(int_list)


def row_result2(row):
    int_list = [int(n) for n in row]
    sorted_list = reversed(sorted(int_list))
    for a, b in combinations(sorted_list, 2):
        if a % b == 0:
            return a / b


if __name__ == '__main__':
    main()
