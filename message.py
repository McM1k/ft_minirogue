# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    message.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bcozic <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/07 18:21:25 by bcozic            #+#    #+#              #
#    Updated: 2018/01/07 22:44:41 by bcozic           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import curses

def message(win, act, mess, pas, wait, stdscr):
    c = 0
    for i in range(80):
        win.addch(0, i, ' ')
    curses.init_pair(10, curses.COLOR_BLACK, curses.COLOR_WHITE)
    win.addstr(0, 0, act)
    win.addstr(0, len(act), mess)
    win.addstr(0, len(act) + len(mess), pas)
    if wait == 1:
        win.addstr(0, len(act) + len(mess) + len(pas), " MORE ", curses.color_pair(10))
        win.refresh()
        while c != ord(' '):
            c = stdscr.getch()

def infos(user, time, lvl, win):
    win.addstr(25, 0, "Level:", curses.color_pair(1))
    nb = str(lvl)
    win.addstr(25, 6, nb, curses.color_pair(1))

    win.addstr(25, 13, "Hits:", curses.color_pair(1))
    nb = str(user.hp)
    win.addstr(25, 17, nb, curses.color_pair(1))
    slen = 17 + len(nb)
    win.addch(25, slen, '(', curses.color_pair(1))
    nb = str(user.hp_max)
    win.addstr(25, slen + 1, nb, curses.color_pair(1))
    slen = slen + 1 + len(nb)
    win.addch(25, slen, ')', curses.color_pair(1))

    win.addstr(25, 26, "Str:", curses.color_pair(1))
    nb = str(user.strgt)
    win.addstr(25, 30, nb, curses.color_pair(1))
    slen = 30 + len(nb)
    win.addch(25, slen, '(', curses.color_pair(1))
    nb = str(user.strgt_max)
    win.addstr(25, slen + 1, nb, curses.color_pair(1))
    slen = slen + 1 + len(nb)
    win.addch(25, slen, ')', curses.color_pair(1))

    win.addstr(25, 39, "Gold:", curses.color_pair(1))
    nb = str(user.gold)
    win.addstr(25, 44, nb, curses.color_pair(1))

    win.addstr(25, 52, "Armor:", curses.color_pair(1))
    nb = str(user.ac)
    win.addstr(25, 44, nb, curses.color_pair(1))
