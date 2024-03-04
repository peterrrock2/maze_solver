from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other: "Point"):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: "Point"):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other: "Point"):
        return self.x == other.x and self.y == other.y
    
    def __truediv__(self, other: int):
        return Point(self.x / other, self.y / other)
    
    def __floordiv__(self, other: int):
        return Point(self.x // other, self.y // other)

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
    
    def draw(self, canvas: Canvas, fill_color="black"):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color)
        

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        
        while self.__running:
            self.redraw()
            
    def close(self):
        self.__running = False

    def draw_line(self, line: Line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

