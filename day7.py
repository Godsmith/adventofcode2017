from collections import Counter

from util import input_rows


class Program:
    def __init__(self, name, weight, children=None):
        self.name = name
        self.weight = weight
        self._children = children if children else []
        self.parent = None
        self._total_weight = None

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, value):
        self._children = value
        for child in self._children:
            child.parent = self

    @property
    def total_weight(self):
        if not self._total_weight:
            self._total_weight = self.weight + sum(child.total_weight
                                                   for child in self.children)
        return self._total_weight

    @property
    def is_balanced(self):
        return all(c.total_weight == self.children[0].total_weight
                   for c in self.children)

    def __repr__(self):
        return 'Program("%s", %s, %s)' % (self.name, self.weight, self.children)


class ProgramParser():
    @classmethod
    def create_programs(cls, input_rows):
        program_from_name = {
            cls.get_name(row): Program(cls.get_name(row), cls.get_weight(row))
            for row in input_rows}
        for row in [row for row in input_rows if '->' in row]:
            program = program_from_name[cls.get_name(row)]
            program.children = [program_from_name[name]
                                for name in cls.get_child_names(row)]
        return program_from_name.values()

    @classmethod
    def get_name(cls, row):
        return row.split()[0]

    @classmethod
    def get_weight(cls, row):
        return int(row.split('(')[-1].split(')')[0])

    @classmethod
    def get_child_names(cls, row):
        return row.split('-> ')[-1].split(', ')


def main():
    programs = ProgramParser.create_programs(input_rows(7))
    p = bottom_program(programs)
    print(p.name)
    print(correct_weight_of_faulty_program(programs))


def bottom_program(programs):
    return next(program for program in programs if not program.parent)


def faulty_program(programs):
    parents = {program.parent for program in programs
               if program.is_balanced and
               not program.parent.is_balanced}
    for parent in parents:
        child = program_with_unique_total_weight(parent.children)
        if child not in parents:
            return child


def correct_weight_of_faulty_program(programs):
    program = faulty_program(programs)
    for child in program.parent.children:
        adjustment = child.total_weight - program.total_weight
        if adjustment != 0:
            return program.weight + adjustment


def program_with_unique_total_weight(programs):
    weights = [program.total_weight for program in programs]
    counter = Counter(weights)
    unique_weight = key_with_value(counter, 1)
    weight_from_program = {program: program.total_weight
                           for program in programs}
    return key_with_value(weight_from_program, unique_weight)


def key_with_value(dict, value):
    for key, val in dict.items():
        if value == val:
            return key


if __name__ == '__main__':
    main()
