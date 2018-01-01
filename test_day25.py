from day25 import TuringMachine, State, Action


class TestAction:
    def test_eq(self):
        a = Action(1, 1, 'A')
        b = Action(1, 1, 'A')
        assert a == b


class TestTuringMachine:
    state_dict = {'A': State(action_when_0=Action(1, 1, 'B'),
                             action_when_1=Action(0, -1, 'B')),
                  'B': State(action_when_0=Action(1, -1, 'A'),
                             action_when_1=Action(1, 1, 'A'))}

    def test_run(self):
        machine = TuringMachine(self.state_dict)
        machine.run(6)
        assert machine.checksum() == 3

    def test_state_dict_from_strings(self):
        text = """Begin in state A.
        Perform a diagnostic checksum after 6 steps.

        In state A:
          If the current value is 0:
            - Write the value 1.
            - Move one slot to the right.
            - Continue with state B.
          If the current value is 1:
            - Write the value 0.
            - Move one slot to the left.
            - Continue with state B.

        In state B:
          If the current value is 0:
            - Write the value 1.
            - Move one slot to the left.
            - Continue with state A.
          If the current value is 1:
            - Write the value 1.
            - Move one slot to the right.
            - Continue with state A.""".split('\n')
        assert TuringMachine.from_strings(text).state_dict == self.state_dict
