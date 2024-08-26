from Point import Point
from Line import Line


class Cell:
    def __init__(
        self,
        _has_left_wall,
        _has_right_wall,
        _has_top_wall,
        _has_bottom_wall,
        _x1,
        _x2,
        _y1,
        _y2,
        _win=None,
    ):
        self._has_left_wall = True
        self._has_right_wall = True
        self._has_top_wall = True
        self._has_bottom_wall = True
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2
        self._win = _win
        self.visited = False

    def draw(self):
        if self._has_top_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "black"
            )
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "white"
            )
        if self._has_left_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "black"
            )
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "white"
            )
        if self._has_right_wall:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "black"
            )
        else:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "white"
            )
        if self._has_bottom_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "black"
            )
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "white"
            )

    def draw_move(self, to_cell, undo=False):
        self._win.draw_line(
            Line(
                Point(
                    self._x1
                    + (0.5 * (max(self._x1, self._x2) - min(self._x1, self._x2))),
                    self._y1
                    + (0.5 * (max(self._y1, self._y2) - min(self._y1, self._y2))),
                ),
                Point(
                    to_cell._x1
                    + (
                        0.5
                        * (
                            max(to_cell._x2, to_cell._x1)
                            - min(to_cell._x2, to_cell._x1)
                        )
                    ),
                    to_cell._y1
                    + (
                        0.5
                        * (
                            max(to_cell._y2, to_cell._y1)
                            - min(to_cell._y2, to_cell._y1)
                        )
                    ),
                ),
            ),
            "red" if not undo else "gray",
        )
