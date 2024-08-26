class Line:
    def __init__(self, _point1, _point2):
        self._point1 = _point1
        self._point2 = _point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self._point1.x,
            self._point1.y,
            self._point2.x,
            self._point2.y,
            fill=fill_color,
            width=2,
        )
