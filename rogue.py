# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    rogue.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bcozic <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/06 10:53:53 by bcozic            #+#    #+#              #
#    Updated: 2018/01/07 23:35:13 by bcozic           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import curses
import locale
import level
import pickups
import wall
import begin_lvl
import user_action
import fight
import message

def colormap(char):
    if char == pickups.treasure_symbol:
        return 1
    if char == '.':
        return 2
    elif char == level.ne_corner_symbol or char == level.nw_corner_symbol\
            or char == level.se_corner_symbol or char == level.sw_corner_symbol\
            or char == level.horizontal_symbol or char == level.vertical_symbol\
            or char == level.door_symbol or char == pickups.food_symbol:
        return 3
    else:
        return 0

locale.setlocale(locale.LC_ALL,"")

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)
curses.curs_set(0)
win = curses.newwin(26, 81, 5, 10)
hero = u'\u263a'.encode('utf-8')
curses.start_color()
curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)

user = user_action.User

print(user.lvl)
end = 0
time = 0
lvl = 0
life = 1
while end != 2 and life == 1:
    lvl = lvl + 1
    end = 0
    map = level.newlevel(0)
    begin_lvl.init_door(map)
    user.y,user.x = begin_lvl.choose_place(map)

    foods = pickups.placefoods(map)
    treasures = pickups.placetreasures(map)
    map = pickups.drawpickups(map, treasures, foods)

    map[user.y - 1][user.x] = 'x'
    mob = begin_lvl.init_lvl(1, map)
    nb_mob = 4
    map[user.y - 1][user.x] = '.'
    while end == 0 and life == 1:
        dead = 1
        for y in range(0, 25):
            for x in range(0, 80):
                win.addstr(y + 1, x, map[y][x], curses.color_pair(colormap(map[y][x])))
        win.addstr(user.y, user.x, hero, curses.color_pair(1))
        message.infos(user, time, lvl, win)
        for i in range(nb_mob):
            win.addch(mob[i].y, mob[i].x, mob[i].index + ord('A'))
        win.refresh()
        end = user_action.user_act(map, treasures, foods, user, mob, nb_mob, stdscr, win)
        if user.hp <= 0:
            life = 0
            win.clear()
            win.addstr(10, 0, "You are dead !!")
            win.refresh()
            c = 0
            while c != ord(' '):
                c = stdscr.getch()

        i = 0
        while i < nb_mob:
            if mob[i].hp <= 0:
                del mob[i]
                dead = 1
                nb_mob = nb_mob - 1
                i = i - 1
            elif abs(mob[i].x - user.x == 1):
                if mob[i].y - user.y == 0:
                    fight.fight_mob(mob[i], user, win, stdscr)
            elif abs(mob[i].y - user.y == 1):
                if mob[i].x - user.x == 0:
                    fight.fight_mob(mob[i], user, win, stdscr)
            else:
                fight.mob_mov(map, user.y, user.x, mob[i], mob, nb_mob, user, treasures, foods)
            i = i + 1

curses.endwin()
curses.nocbreak(); stdscr.keypad(0); curses.echo()
