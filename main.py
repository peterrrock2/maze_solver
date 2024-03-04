from graphics import Window, Point, Line
from maze import Maze
from cell import Cell

def main():    
    window = Window(800, 600)

    maze = Maze(
        n_rows = 8,
        n_cols = 8,
        cell_width = 50,
        cell_height = 50,
        x_offset = 50,
        y_offset = 50,
        window = window,
        seed=0
    )

    
    maze.solve()
    window.wait_for_close()
    
if __name__ == "__main__":
    main()