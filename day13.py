import itertools

from util import input_rows


class Layer:
    def __init__(self, depth):
        self.depth = depth
        self._indices = list(range(depth)) + list(reversed(range(
            depth)))[1:-1]

    def scanner_location(self, delay):
        return self._indices[delay % len(self._indices)]


class Layers:
    def __init__(self, strings):
        self._dict = {int(s.split(': ')[0]): Layer(int(s.split(': ')[-1]))
                      for s in strings}

    def severity(self, layer_index, delay):
        if self._dict[layer_index].scanner_location(delay + layer_index) == 0:
            return self._dict[layer_index].depth * layer_index
        else:
            return 0

    def total_severity(self, delay=0):
        return sum(self.severity(i, delay) for i in self._dict)

    def caught(self, delay=0):
        for i in self._dict:
            if self._dict[i].scanner_location(delay + i) == 0:
                return True
        return False

    def first_delay_without_being_caught(self):
        for delay in itertools.count():
            if not self.caught(delay):
                return delay


if __name__ == '__main__':
    print(Layers(input_rows(13)).total_severity())
    print(Layers.first_delay_without_being_caught(input_rows(13)))
