from util import input_rows


def count_steps(list_, change_function):
    list_ = list(list_)
    index = 0
    steps = 0
    while index < len(list_):
        value = list_[index]
        list_[index] = change_function(value)
        index += value
        steps += 1
    return steps


list_ = [int(s) for s in (input_rows(5))]
print(count_steps(list_, lambda x: x + 1))
print(count_steps(list_, lambda x: x + 1 if x < 3 else x - 1))
