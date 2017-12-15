from util import input_rows


class Layer:
    def __init__(self, depth, scanner_location=0, direction=1):
        self.depth = depth
        self.scanner_location = scanner_location
        self.direction = direction

    def step(self):
        self.scanner_location += self.direction
        if not 0 <= self.scanner_location < self.depth:
            self.direction *= -1
            self.scanner_location += self.direction * 2

    def reset(self):
        self.scanner_location = 0
        self.direction = 1

    def __repr__(self):
        list_ = ['['] + ['-'] * self.depth + [']']
        list_[self.scanner_location + 1] = 'X'
        return ''.join(list_)


class Layers:
    def __init__(self, strings):
        self._dict = {int(s.split(': ')[0]): Layer(int(s.split(': ')[-1]))
                      for s in strings}

    def severity(self, layer_index):
        return self._dict[layer_index].depth * layer_index

    @property
    def last_layer(self):
        return sorted(self._dict.keys())[-1]

    def step(self):
        for layer in self._dict.values():
            layer.step()

    def _reset(self):
        for layer in self._dict.values():
            layer.reset()

    def total_severity(self, delay=0):
        self._reset()
        for i in range(delay):
            self.step()

        total_severity = 0
        for i in range(self.last_layer + 1):
            if i in self._dict:
                if self._dict[i].scanner_location == 0:
                    total_severity += self.severity(i)
            self.step()
        return total_severity

    def caught(self, delay=0):
        self._reset()
        for i in range(delay):
            self.step()

        for i in range(self.last_layer + 1):
            if i in self._dict:
                if self._dict[i].scanner_location == 0:
                    return True
            self.step()
        return False

    @classmethod
    def first_delay_without_being_caught(cls, strings):
        delay = 0
        while True:
            layers = Layers(strings)
            if not layers.caught(delay):
                break
            delay += 1
        return delay


if __name__ == '__main__':
    print(Layers(input_rows(13)).total_severity())
    print(Layers.first_delay_without_being_caught(input_rows(13)))
