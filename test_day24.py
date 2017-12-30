from day24 import Component, Bridge


class TestComponent:
    def test_from_string(self):
        component = Component.from_string('0/1')
        assert component.ports == [0, 1]
        assert component._available_ports == [0, 1]

    def test_str(self):
        component = Component.from_string('0/1')
        assert str(component) == '0/1'


COMPONENT_STRINGS = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10""".split('\n')


class TestBridge:
    def test_str(self):
        bridge = Bridge()
        bridge = bridge.add(Component.from_string('0/1'))
        bridge = bridge.add(Component.from_string('10/1'))
        assert str(bridge) == '0/1--10/1'

    def test_compatible(self):
        bridge = Bridge()
        assert bridge.compatible(Component.from_string('0/1'))
        assert not bridge.compatible(Component.from_string('1/1'))

        bridge = bridge.add(Component.from_string('0/1'))
        assert bridge.compatible(Component.from_string('2/1'))
        assert bridge.compatible(Component.from_string('1/2'))


class TestAllBridgesFromComponents:
    def test_empty(self):
        assert list(Bridge._all_bridges_from_components([])) == []

    def test_single(self):
        assert set(map(str, Bridge._all_bridges_from_components([
            Component.from_string('0/1')]))) == {'0/1'}

    def test_single_incompatible(self):
        assert set(map(str, Bridge._all_bridges_from_components([
            Component.from_string('1/1')]))) == set()

    def test_two_parallel(self):
        assert set(map(str, Bridge._all_bridges_from_components([
            Component.from_string('0/1'), Component.from_string('0/2')]))) == \
               {'0/1', '0/2'}

    def test_example(self):
        assert set(map(str, Bridge.all_bridges_from_component_strings(
            COMPONENT_STRINGS))) == {'0/1', '0/1--10/1', '0/1--10/1--9/10',
                                     '0/2', '0/2--2/3', '0/2--2/3--3/4',
                                     '0/2--2/3--3/5', '0/2--2/2',
                                     '0/2--2/2--2/3', '0/2--2/2--2/3--3/4',
                                     '0/2--2/2--2/3--3/5'}


class TestStrongestBridgeFromComponentsStrings:
    def test_strongest_bridge_from_components_strings(self):
        assert Bridge.strongest_bridge_from_component_strings(
            COMPONENT_STRINGS) == 31
