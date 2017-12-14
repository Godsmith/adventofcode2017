from util import input_rows


class Program:
    def __init__(self, id_, connections):
        self.id = id_
        self.connections = connections

    @classmethod
    def from_string(cls, s):
        list_ = s.split(' <-> ')
        id_ = int(list_[0])
        connections = list(map(int, list_[1].split(', ')))
        return Program(id_, connections)

    def __hash__(self):
        return self.id


def programs_from_strings(strings):
    return list(map(Program.from_string, strings))


def group_including_program(strings, id_):
    program_from_id = programs_from_strings(strings)

    interior_programs = set()
    edge_programs = {program_from_id[id_]}
    next_edge_programs = set()
    while edge_programs:
        for edge_program in edge_programs:
            interior_programs.add(edge_program)
            for connection_id in edge_program.connections:
                connected_program = program_from_id[connection_id]
                if connected_program not in interior_programs | \
                        edge_programs:
                    next_edge_programs.add(connected_program)
        edge_programs = next_edge_programs
        next_edge_programs = set()
    return interior_programs


def groups(strings):
    ids = set()
    output = []
    for id_, _ in enumerate(strings):
        if id_ not in ids:
            group = group_including_program(strings, id_)
            group_ids = {program.id for program in group}
            output.append(group)
            ids = ids | group_ids
    return output


if __name__ == '__main__':
    print(len(group_including_program(input_rows(12), 0)))
    print(len(groups(input_rows(12))))
