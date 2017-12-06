BANKS = tuple(map(int, '4	1	15	12	0	9	9	5	'
                       '5	8	7	3	14	5	12	3'.split()))


def cycle(banks):
    banks = list(banks)
    index_of_first_max = banks.index(max(banks))
    blocks = banks[index_of_first_max]
    banks[index_of_first_max] = 0
    for index in range(index_of_first_max + 1, index_of_first_max + blocks + 1):
        banks[index % len(banks)] += 1
    return tuple(banks)


def cycle_count_and_loop_size(banks):
    previous_banks = []
    count = 0
    while banks not in previous_banks:
        previous_banks.append(banks)
        banks = cycle(banks)
        count += 1
    return count, len(previous_banks) - previous_banks.index(banks)


if __name__ == '__main__':
    print(cycle_count_and_loop_size(BANKS))
