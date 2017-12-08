from util import input_rows


def largest_value(instructions):
    largest_ever = 0
    for name in register_names(instructions):
        locals()[name] = 0
    for instruction in instructions:
        exec(translate(instruction))
        largest_ever = max(largest_ever, _largest_int(locals().values()))
    locals_copy = locals().copy()
    locals_copy.pop('largest_ever')
    largest_at_end = _largest_int(locals_copy.values())
    return largest_at_end, largest_ever


def _largest_int(values):
    ints = [value for value in values if isinstance(value, int)]
    return max(ints) if ints else 0


def register_names(instructions):
    return {instruction.split()[0] for instruction in instructions}


def translate(instruction):
    instruction = instruction.replace('inc', '+=').replace('dec', '-=')
    left, right = instruction.split(' if ')
    return f'if {right}: {left}'


if __name__ == '__main__':
    print(largest_value(input_rows(8)))
