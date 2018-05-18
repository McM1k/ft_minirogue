import curses
import level
win_size_x = 80
win_size_y = 25
x_player = 0
y_player = 0

def main():
    stdscr = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK, curses.A_BOLD)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.keypad(1)
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    win = curses.newwin(win_size_y, win_size_x)

    while 1:
        key = stdscr.getch()
        win.clear()
        if key == curses.KEY_EXIT:
            break
        if key == curses.KEY_DOWN and y_player < win_size_y - 2:
            y_player = y_player + 1
        if key == curses.KEY_UP and y_player:
            y_player = y_player - 1
        if key == curses.KEY_RIGHT and x_player < win_size_x - 2:
            x_player = x_player + 1
        if key == curses.KEY_LEFT and x_player:
            x_player = x_player - 1

        win.move(y_player, x_player)
        win.addch(level.player_symbol)
        win.refresh()

    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()

if __name__ == "__main__":
    main()