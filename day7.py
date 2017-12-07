from util import input_rows


class Program:
    def __init__(self, name, weight, children=None):
        self.name = name
        self.weight = weight
        self._children = children
        self.parent = None

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, value):
        self._children = value
        for child in self._children:
            child.parent = self

    def __repr__(self):
        return 'Program("%s", %s, %s)' % (self.name, self.weight, self.children)


def main():
    programs = create_programs(input_rows(7))
    print(bottom_program(programs))


def create_programs(input_rows):
    programs = {}
    for row in input_rows:
        name = row.split()[0]
        weight = int(row.split('(')[-1].split(')')[0])
        program = Program(name, weight)
        programs[name] = program
    for row in input_rows:
        if '->' in row:
            name = row.split()[0]
            child_names = row.split('-> ')[-1].split(', ')
            programs[name].children = [programs[name] for name in child_names]
    return programs


def bottom_program(programs):
    return next(program for program in programs.values() if not program.parent)


if __name__ == '__main__':
    main()
