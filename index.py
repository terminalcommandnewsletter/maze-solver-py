from Window import Window
from Maze import Maze

win = Window(_width=800, _height=600)

maze = Maze(
    _x1=10,
    _y1=10,
    _num_rows=30,
    _num_cols=30,
    _cell_size_x=50 / 3,
    _cell_size_y=50 / 3,
    _win=win,
)

maze.solve()

win.wait_for_close()
