# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    user_action.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bcozic <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/07 16:39:36 by bcozic            #+#    #+#              #
#    Updated: 2018/01/07 23:17:15 by bcozic           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import wall
import fight
import level
import pickups

def user_act(map, treasures, foods, user, mob, nb_mob, stdscr, win):
    c = stdscr.getch()
    end = 0
    if c == ord('s') and user.y < 24:
        mod,mob = wall.wall(map, user.y + 1, user.x, mob, nb_mob, user, treasures, foods)
        if mod == 1:
            user.y = user.y + 1
        elif mod == 2:
            fight.fight_user(mob, user, win, stdscr)
    if c == ord('w') and user.y > 0:
        mod,mob = wall.wall(map, user.y - 1, user.x, mob, nb_mob, user, treasures, foods)
        if mod == 1:
            user.y = user.y - 1
        elif mod == 2:
            fight.fight_user(mob, user, win, stdscr)
    if c == ord('d') and user.x < 79:
        mod,mob = wall.wall(map, user.y, user.x + 1, mob, nb_mob, user, treasures, foods)
        if mod == 1:
            user.x = user.x + 1
        elif mod == 2:
            fight.fight_user(mob, user, win, stdscr)
    if c == ord('a') and user.x > 0:
        mod,mob = wall.wall(map, user.y, user.x - 1, mob, nb_mob, user, treasures, foods)
        if mod == 1:
            user.x = user.x - 1
        elif mod == 2:
            fight.fight_user(mob, user, win, stdscr)
    if c == ord('e'):
        user.hp = user.hp_max
        user.ration = user.ration - 1
    if c == ord('z'):
        if (map[user.y - 1][user.x] == level.door_lvl_symbol):
            end = 1
        if (map[user.y - 1][user.x] == pickups.treasure_symbol):
            user.gold = user.gold+10
        if (map[user.y - 1][user.x] == pickups.food_symbol):
            user.hp = user.hp_max
    if c == ord('q'):
        end = 2
    if c == ord('p'):
        end = 1
    return (end)

class User:
    name = "you"
    hp = 12
    hp_max = 12
    xp = 0
    ac = 5
    gold = 0
    ration = 0
    ph_strgt = 16
    strgt = 16
    strgt_max = 16
    damage = 3
    lvl = 1
    x = 0
    y = 0
