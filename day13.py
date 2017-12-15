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

    def severity(self, layer_index):
        return self._dict[layer_index].depth * layer_index

    @property
    def last_layer(self):
        return sorted(self._dict.keys())[-1]

    def total_severity(self, delay=0):
        total_severity = 0
        for i in range(self.last_layer + 1):
            if i in self._dict:
                if self._dict[i].scanner_location(delay + i) == 0:
                    total_severity += self.severity(i)
        return total_severity

    def caught(self, delay=0):
        for i in self._dict:
            if self._dict[i].scanner_location(delay + i) == 0:
                return True
        return False

    @classmethod
    def first_delay_without_being_caught(cls, strings):
        layers = Layers(strings)
        for delay in itertools.count():
            if not layers.caught(delay):
                return delay


if __name__ == '__main__':
    print(Layers(input_rows(13)).total_severity())
    print(Layers.first_delay_without_being_caught(input_rows(13)))
