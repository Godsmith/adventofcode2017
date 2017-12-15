import pytest

from day13 import Layers, Layer


@pytest.fixture
def layers():
    input_ = """0: 3
    1: 2
    4: 4
    6: 4""".split('\n')
    return Layers(input_)


class TestLayers:
    def test_create_layers(self, layers):
        assert len(layers._dict) == 4
        assert layers._dict[0].depth == 3

    def test_total_severity(self, layers):
        assert layers.total_severity() == 24

    def test_total_severity_delay_10(self, layers):
        assert layers.total_severity(delay=10) == 0

    def test_first_delay_without_being_caught(self, layers):
        assert layers.first_delay_without_being_caught() == 10


class TestLayer:
    def test_scanner_location(self):
        layer = Layer(3)
        assert layer.scanner_location(0) == 0
        assert layer.scanner_location(2) == 2
        assert layer.scanner_location(4) == 0
