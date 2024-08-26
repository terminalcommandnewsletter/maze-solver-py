import unittest
from Maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m2._break_walls_r(0, 0)
        m2._reset_cells_visited()
        for col in m2._cells:
            for row in col:
                self.assertFalse(row.visited)


if __name__ == "__main__":
    unittest.main()
