from front import View
from defines import *

def main():
    
    view = View()
    field = [[1] * BOARD_X] * BOARD_Y
    while view.game_on:
        view.clear()
        view.game_update()
        view.draw_field(field)
        view.refresh()
        ch = view.get_input()
        if ch == 10:
            view.game_on = False
        view.sleep(100)
        
    
    
if __name__ == "__main__":
    main()
