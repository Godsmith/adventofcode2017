import pytest

from day13 import Layers, Layer

INPUT = """0: 3
1: 2
4: 4
6: 4""".split('\n')


class TestLayers:
    def test_create_layers(self):
        layers = Layers(INPUT)
        assert len(layers._dict) == 4
        assert layers._dict[0].depth == 3

    def test_step(self):
        layers = Layers(INPUT)
        layers.step()
        assert layers._dict[0]._scanner_location == 1

    def test_last_layer(self):
        layers = Layers(INPUT)
        assert layers.last_layer == 6

    def test_total_severity(self):
        layers = Layers(INPUT)
        assert layers.total_severity() == 24

    def test_total_severity_delay_10(self):
        layers = Layers(INPUT)
        assert layers.total_severity(delay=10) == 0

    def test_first_delay_without_being_caught(self):
        assert Layers.first_delay_without_being_caught(INPUT) == 10


class TestLayer:
    @pytest.mark.parametrize('steps, location',
                             [(3, 1), (6, 2)])
    def test_step(self, steps, location):
        layer = Layer(3)
        for i in range(steps):
            layer.step()
        assert layer._scanner_location == location

    def test_scanner_location(self):
        layer = Layer(3)
        assert layer.scanner_location(0) == 0
        assert layer.scanner_location(2) == 2
        assert layer.scanner_location(4) == 0
