from util import input_rows


class Component:
    def __init__(self, ports, available_ports=None):
        ports_list = list(ports)
        if available_ports is None:
            self._available_ports = list(ports_list)
        else:
            self._available_ports = list(available_ports)
        self.ports = list(ports_list)

    def __str__(self):
        return '/'.join([str(port) for port in self.ports])

    @property
    def strength(self):
        return sum(self.ports)

    @property
    def available_port(self):
        try:
            return self._available_ports[0]
        except IndexError:
            self = self

    @classmethod
    def from_string(cls, s):
        return Component(map(int, s.split('/')))

    @classmethod
    def connect(self, component1, component2):
        common_port = list(set(component1.ports) & set(component2.ports))[0]
        new_available_ports1 = list(component1._available_ports)
        new_available_ports2 = list(component2._available_ports)
        new_available_ports1.remove(common_port)
        new_available_ports2.remove(common_port)
        return [Component(component1.ports, new_available_ports1),
                Component(component2.ports, new_available_ports2)]


class Bridge:
    def __init__(self, components=None):
        if components is None:
            self.components = []
        else:
            self.components = list(components)

    def __str__(self):
        return '--'.join(str(component) for component in self.components)

    @property
    def strength(self):
        return sum(c.strength for c in self.components)

    @property
    def port(self):
        if not self.components:
            return 0
        else:
            return self.components[-1].available_port

    def add(self, component):
        components = list(self.components)
        if components:
            components[-1:] = Component.connect(self.components[-1],
                                                component)
        else:
            components.append(component)
            component._available_ports.remove(0)
        return Bridge(components)

    def compatible(self, component):
        return self.port in component._available_ports

    @classmethod
    def all_bridges_from_component_strings(cls, strings):
        components = list(map(Component.from_string, strings))
        return Bridge._all_bridges_from_components(components)

    @classmethod
    def _all_bridges_from_components(cls, components_left, bridge=None):
        print(bridge)
        if not bridge:
            bridge = Bridge()
            bridges = []
        else:
            bridges = [bridge]
        for component in components_left:
            if bridge.compatible(component):
                new_bridge = bridge.add(component)
                new_components_left = list(components_left)
                new_components_left.remove(component)
                bridges.extend(cls._all_bridges_from_components(
                    new_components_left, new_bridge))
        return bridges

    @classmethod
    def strongest_bridge_from_component_strings(cls, strings):
        return max(b.strength for b in cls.all_bridges_from_component_strings(
            strings))


if __name__ == '__main__':
    print(Bridge.strongest_bridge_from_component_strings(input_rows(24)))
