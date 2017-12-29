from day22 import Virus, Grid, Virus2, Grid2


class TestVirus:
    def test_is_current_node_is_infected(self):
        grid = Grid('... .#. ...'.split())
        virus = Virus(grid, (1, 1))
        assert virus._is_current_node_infected()
        virus = Virus(grid, (0, 0))
        assert not virus._is_current_node_infected()

    def test_infect(self):
        grid = Grid('... .#. ...'.split())
        virus = Virus(grid, (0, 0))
        assert not virus._is_current_node_infected()
        virus._infect()
        assert virus._is_current_node_infected()

    def test_move_forward(self):
        virus = Virus(None, (0, 0))
        virus._move_forward()
        assert virus._position == (0, -1)

    def test_turn_right(self):
        virus = Virus(None, (0, 0))
        for _ in range(4):
            virus._move_forward()
            virus._turn_right()
        assert virus._position == (0, 0)

    def test_example_short(self):
        grid = Grid('..# #.. ...'.split())
        virus = Virus(grid, (1, 1))
        for _ in range(7):
            virus._burst()
        assert virus._infect_count == 5

    def test_example(self):
        grid = Grid('..# #.. ...'.split())
        virus = Virus(grid, (1, 1))
        for _ in range(70):
            virus._burst()
        assert virus._infect_count == 41

    def test_example_long(self):
        grid = Grid('..# #.. ...'.split())
        virus = Virus(grid, (1, 1))
        for _ in range(10000):
            virus._burst()
        assert virus._infect_count == 5587


class TestVirus2:
    def test_example_short(self):
        grid = Grid2('..# #.. ...'.split())
        virus = Virus2(grid, (1, 1))
        for _ in range(100):
            virus._burst()
        assert virus._infect_count == 26

    def test_print(self):
        grid = Grid2('..# #.. ...'.split())
        virus = Virus2(grid, (1, 1))
        for _ in range(8):
            print(grid)
            print()
            virus._burst()

            # Passes, but too slow.
            # def test_example_long(self):
            #     grid = Grid2('..# #.. ...'.split())
            #     virus = Virus2(grid, (1, 1))
            #     for _ in range(10000000):
            #         virus._burst()
            #     assert virus._infect_count == 2511944


class TestGrid:
    def test_is_infected(self):
        grid = Grid('... .#. ...'.split())
        assert grid.is_infected((1, 1))
        assert not grid.is_infected((2, 2))

    def test_infect(self):
        grid = Grid('... .#. ...'.split())
        assert not grid.is_infected((2, 2))
        grid.infect((2, 2))
        assert grid.is_infected((2, 2))

    def test_clean(self):
        grid = Grid('... .#. ...'.split())
        assert grid.is_infected((1, 1))
        grid.clean((1, 1))
        assert not grid.is_infected((1, 1))
