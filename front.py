import curses
from defines import *

class View:
    def __init__(self) -> None:
        self.__stdscr = curses.initscr()
        curses.curs_set(0)
        curses.noecho()
        curses.raw()
        self.__stdscr.keypad(True)
        self.__stdscr.nodelay(True)
        self.init_variables()
        self.game_on = True
        
    def init_variables(self):
        self.x_left = 0
        self.x_right = BOARD_X + 1
        self.y_top = 0
        self.y_bottom = BOARD_Y + 1

        
    def print_rectangle(self):
        self.__stdscr.addch(self.y_top, self.x_left, curses.ACS_ULCORNER)
        self.__stdscr.addch(self.y_top, self.x_right, curses.ACS_URCORNER)
        
        for i in range(self.x_left + 1, self.x_right):
            self.__stdscr.addch(self.y_top, i, curses.ACS_HLINE)
            self.__stdscr.addch(self.y_bottom, i, curses.ACS_HLINE)
        
        for i in range(self.y_top + 1, self.y_bottom):
            self.__stdscr.addch(i, self.x_left, curses.ACS_VLINE)
            self.__stdscr.addch(i, self.x_right, curses.ACS_VLINE)
        
        self.__stdscr.addch(self.y_bottom, self.x_left, curses.ACS_LLCORNER)
        self.__stdscr.addch(self.y_bottom, self.x_right, curses.ACS_LRCORNER)
        self.__stdscr.addstr(self.y_bottom + 1, 0, "")
        
    
    def game_update(self):
        self.print_rectangle()
        
    def get_input(self):
        return self.__stdscr.getch()
    
    def sleep(self, n):
        curses.napms(n)
        
    def __addch(self, y, x, ch):
        return self.__stdscr.addch(y+1, x+1, ch)
    
    
    def draw_field(self, field: list[list]):
        for i in range(BOARD_Y):
            for j in range(BOARD_X):
                if field[i][j] == 1:
                    self.__addch(i, j, '.')
        

    def refresh(self):
        self.__stdscr.refresh()
    
    def clear(self):
        self.__stdscr.clear()
            
        