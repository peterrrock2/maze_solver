from time import sleep
from cell import Cell, CellWall
from graphics import Point, Line, Window 
import random


class Maze:
    def __init__(
        self,
        n_rows: int,
        n_cols: int,
        cell_width: int,
        cell_height: int,
        x_offset: int = 0,
        y_offset: int = 0,
        window = None,
        seed: int = None,
    ):
        
        self._window = window
        self._x_offset = x_offset
        self._y_offset = y_offset
        self._n_rows = n_rows
        self._n_cols = n_cols
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._cells = [[None for i in range(n_cols)] for j in range(n_rows)]
        if seed is not None:
            random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        for i in range(self._n_rows):
            for j in range(self._n_cols):
                cell = Cell(self._window)
                self._cells[i][j] = cell
                self._draw_cell(i, j)
    
    def _draw_cell(self, i: int, j: int):
        if self._window is None:
            return
        ul = Point(j * self._cell_width, i * self._cell_height) \
            + Point(self._x_offset, self._y_offset)
        lr = Point((j + 1) * self._cell_width, (i + 1) * self._cell_height) \
            + Point(self._x_offset, self._y_offset)
        self._cells[i][j].draw(ul, lr)
        self._animate()
        
    def _animate(self):
        if self._window is None:
            return
        self._window.redraw()
        sleep(0.02)
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].walls[CellWall.LEFT.value] = False
        self._cells[-1][-1].walls[CellWall.RIGHT.value] = False
        self._draw_cell(0,0)
        self._draw_cell(self._n_rows - 1, self._n_cols - 1)
        self._animate()
        
    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True
        while True:
            next_lst = []
            
            if i > 0 and not self._cells[i - 1][j].visited:
                next_lst.append((i - 1, j))

            if i < self._n_rows - 1 and not self._cells[i + 1][j].visited:
                next_lst.append((i + 1, j))

            if j > 0 and not self._cells[i][j - 1].visited:
                next_lst.append((i, j - 1))

            if j < self._n_cols - 1 and not self._cells[i][j + 1].visited:
                next_lst.append((i, j + 1))

            if len(next_lst) == 0:
                self._draw_cell(i, j)
                return

            direction_index = random.randrange(len(next_lst))
            next_index = next_lst[direction_index]
            
            if next_index[0] == i + 1:
                self._cells[i][j].walls[CellWall.BOTTOM.value] = False
                self._cells[i+1][j].walls[CellWall.TOP.value] = False

            if next_index[0] == i - 1:
                self._cells[i][j].walls[CellWall.TOP.value] = False
                self._cells[i-1][j].walls[CellWall.BOTTOM.value] = False

            if next_index[1] == j + 1:
                self._cells[i][j].walls[CellWall.RIGHT.value] = False
                self._cells[i][j+1].walls[CellWall.LEFT.value] = False

            if next_index[1] == j - 1:
                self._cells[i][j].walls[CellWall.LEFT.value] = False
                self._cells[i][j-1].walls[CellWall.RIGHT.value] = False

            self._break_walls_r(next_index[0], next_index[1])       
       
    def _reset_cells_visited(self):
        for i in range(self._n_rows):
            for j in range(self._n_cols):
                self._cells[i][j].visited = False
                

    def solve(self):
        self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._cells[i][j].visited = True
        self._animate()

        if i == self._n_rows - 1 and j == self._n_cols - 1:
            return True

        walls = self._cells[i][j].walls
        
        # Top, Right, Bottom, Left
        valid_directions = [False]*4
        
        if i == 0 and j == 0:
            valid_directions = [not v for v in walls[:3]]+[False]
            loser = False
        else:
            valid_directions[0] = not (walls[CellWall.TOP.value] or self._cells[i - 1][j].visited)
            valid_directions[1] = not (walls[CellWall.RIGHT.value] or self._cells[i][j + 1].visited)
            valid_directions[2] = not (walls[CellWall.BOTTOM.value] or self._cells[i + 1][j].visited)
            valid_directions[3] = not (walls[CellWall.LEFT.value] or self._cells[i][j - 1].visited)
            loser = not any(valid_directions)  
       
        
        if loser:
            return False
        
        
        if valid_directions[0]:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i - 1][j], undo=True)
        
        if valid_directions[1]:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j + 1], undo=True)
        
        if valid_directions[2]:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i + 1][j], undo=True)
            
        if valid_directions[3]:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j - 1], undo=True)
         
            