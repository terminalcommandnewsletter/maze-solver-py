from Cell import Cell
import random


class Maze:
    def __init__(
        self,
        _x1,
        _y1,
        _num_rows,
        _num_cols,
        _cell_size_x,
        _cell_size_y,
        _win=None,
        _seed=None,
    ):
        self._x1 = _x1
        self._y1 = _y1
        self._num_rows = _num_rows
        self._num_cols = _num_cols
        self._cell_size_x = _cell_size_x
        self._cell_size_y = _cell_size_y
        self._win = _win
        if _seed is not None:
            random.seed(_seed)
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):
        for i in range(self._num_cols):
            _list = []
            for j in range(self._num_rows):
                _list.append(
                    Cell(
                        True,
                        True,
                        True,
                        True,
                        self._x1 + (i * self._cell_size_x),
                        self._x1 + ((i + 1) * self._cell_size_x),
                        self._y1 + (j * self._cell_size_y),
                        self._y1 + ((j + 1) * self._cell_size_y),
                        self._win,
                    )
                )
            self._cells.append(_list)
            for j in range(self._num_rows):
                self._draw_cell(int(i), int(j))

    def _draw_cell(self, i, j):
        if self._win:
            self._cells[i][j].draw()
            self._animate()

    def _animate(self):
        self._win.redraw()

    def _break_entrance_and_exit(self):
        self._cells[0][0]._has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1]._has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            cells_to_visit = []
            if i < self._num_cols - 1:  # Find cell to the right
                if not self._cells[i + 1][j].visited:
                    cells_to_visit.append((i + 1, j))
            if i > 0:  # Find cell to the left
                if not self._cells[i - 1][j].visited:
                    cells_to_visit.append((i - 1, j))
            if j < self._num_rows - 1:  # Find cell below
                if not self._cells[i][j + 1].visited:
                    cells_to_visit.append((i, j + 1))
            if j > 0:  # Find cell above
                if not self._cells[i][j - 1].visited:
                    cells_to_visit.append((i, j - 1))
            if len(cells_to_visit) == 0:
                self._draw_cell(i, j)
                return
            else:
                dir = random.randrange(0, len(cells_to_visit))
                if cells_to_visit[dir][0] == i + 1:
                    self._cells[i][j]._has_right_wall = False
                    self._cells[i + 1][j]._has_left_wall = False
                if cells_to_visit[dir][0] == i - 1:
                    self._cells[i][j]._has_left_wall = False
                    self._cells[i - 1][j]._has_right_wall = False
                if cells_to_visit[dir][1] == j + 1:
                    self._cells[i][j]._has_bottom_wall = False
                    self._cells[i][j + 1]._has_top_wall = False
                if cells_to_visit[dir][1] == j - 1:
                    self._cells[i][j]._has_top_wall = False
                    self._cells[i][j - 1]._has_bottom_wall = False
                self._draw_cell(i, j)
                self._break_walls_r(cells_to_visit[dir][0], cells_to_visit[dir][1])

    def _reset_cells_visited(self):
        for i in self._cells:
            for j in i:
                j.visited = False

    def solve(self):
        self._reset_cells_visited()
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        cell = self._cells[i][j]
        cell.visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        cells_to_visit = []
        if i < self._num_cols - 1:  # Find cell to the right
            if (
                not self._cells[i + 1][j].visited
                and not self._cells[i + 1][j]._has_left_wall
            ):
                cells_to_visit.append((i + 1, j))
        if i > 0:  # Find cell to the left
            if (
                not self._cells[i - 1][j].visited
                and not self._cells[i - 1][j]._has_right_wall
            ):
                cells_to_visit.append((i - 1, j))
        if j < self._num_rows - 1:  # Find cell below
            if (
                not self._cells[i][j + 1].visited
                and not self._cells[i][j + 1]._has_top_wall
            ):
                cells_to_visit.append((i, j + 1))
        if j > 0:  # Find cell above
            if (
                not self._cells[i][j - 1].visited
                and not self._cells[i][j - 1]._has_bottom_wall
            ):
                cells_to_visit.append((i, j - 1))
        if len(cells_to_visit) == 0:
            self._draw_cell(i, j)
            return False
        for c in cells_to_visit:
            self._cells[i][j].draw_move(self._cells[c[0]][c[1]])
            if self._solve_r(c[0], c[1]) == True:
                return True
                break
            else:
                self._cells[i][j].draw_move(self._cells[c[0]][c[1]], undo=True)
