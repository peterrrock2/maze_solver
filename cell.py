from graphics import Point, Line, Window
from enum import Enum

CellWall = Enum("CellWall", "TOP RIGHT BOTTOM LEFT", start=0)

class Cell:
    def __init__(self, window: Window, walls=None):
        self._ul = None
        self._lr = None
        self._window = window
        # 0: top, 1: right, 2: bottom, 3: left
        self.walls = [True, True, True, True] if walls is None else walls
        self.visited = False
    
    def draw(self, ul: Point, lr: Point):
        self._ul = ul
        self._lr = lr
        self._window.draw_line(
            Line(self._ul, Point(self._lr.x, self._ul.y)),
            fill_color="black" if self.walls[0] else "#d9d9d9"
        )
        self._window.draw_line(
            Line(Point(self._lr.x, self._ul.y), self._lr),
            fill_color="black" if self.walls[1] else "#d9d9d9"
        )
        self._window.draw_line(
            Line(self._lr, Point(self._ul.x, self._lr.y)),
            fill_color="black" if self.walls[2] else "#d9d9d9"
        )
        self._window.draw_line(
            Line(Point(self._ul.x, self._lr.y), self._ul),
            fill_color="black" if self.walls[3] else "#d9d9d9"
        )
            
    @property
    def center(self):
        return (self._ul + self._lr) // 2

    def draw_move(self, to_cell: "Cell", undo=False):
        if undo:
            self._window.draw_line(Line(self.center, to_cell.center), "grey")
        else:
            self._window.draw_line(Line(self.center, to_cell.center), "red")
