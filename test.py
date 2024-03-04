import unittest

from cell import CellWall
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        n_cols = 12
        n_rows = 10
        m1 = Maze(
            n_rows = n_rows,
            n_cols = n_cols,
            cell_width = 10,
            cell_height = 10,
        )
        
        self.assertEqual(
            len(m1._cells),
            n_rows
        )
        
        self.assertEqual(
            len(m1._cells[0]),
            n_cols
        )
    
    def test_break_entrance_exit(self):
        n_cols = 12
        n_rows = 10
        m1 = Maze(
            n_rows = n_rows,
            n_cols = n_cols,
            cell_width = 10,
            cell_height = 10,
        )        
        
        self.assertEqual(
            m1._cells[0][0].walls[CellWall.LEFT.value],
            False
        )
    
        self.assertEqual(
            m1._cells[-1][-1].walls[CellWall.RIGHT.value],
            False
        )

    def test_reset_cells_visited(self):
        n_cols = 12
        n_rows = 10
        m1 = Maze(
            n_rows = n_rows,
            n_cols = n_cols,
            cell_width = 10,
            cell_height = 10,
        )
        for i in range(n_rows):
            for j in range(n_cols):
                self.assertEqual(
                    m1._cells[i][j].visited,
                    False
                )           

if __name__ == "__main__":
    unittest.main()