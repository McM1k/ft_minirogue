# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    fight.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bcozic <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/07 17:32:07 by bcozic            #+#    #+#              #
#    Updated: 2018/01/07 22:51:43 by bcozic           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
import message
import wall

def fight_user(mob, user, win, stdscr):
    hit_chance = 5 + (user.lvl * 5) + (mob.ac * 5)
    if hit_chance < random.randint(1, 100):
        message.message(win, user.name, " miss ", mob.name, 1, stdscr)
    else:
        mob.hp = mob.hp - user.damage
        if mob.hp <= 0:
            message.message(win, user.name, " have defeted ", mob.name, 0, stdscr)
            user.xp = user.xp + mob.xp

        else:
            message.message(win, user.name, " have injured ", mob.name, 1, stdscr)
def fight_mob(mob, user, win, stdscr):
    damage = 0
    for i in range(mob.nb_turn):
        hit_chance = 20 + (mob.hd * 5) + (user.ac * 5)
        if hit_chance < random.randint(1, 100):
            for j in range(mob.damage[i].nb_dice):
                if mob.damage[i].value:
                    damage = damage + 1
                else:
                    damage = damage + random.randint(1, mob.damage[i].value)
    if damage == 0:
        message.message(win, mob.name, " miss ", user.name, 0, stdscr)
    else:
        user.hp = user.hp - damage
        if user.hp <= 0:
            message.message(win, mob.name, " have defeted ", user.name, 0, stdscr)
        else:
            message.message(win, mob.name, " have injured ", user.name, 0, stdscr)

def mob_mov(map, user_y, user_x, mob, list_mob, nb_mob, user, treasures, foods):
    if abs(mob.y - user_y) > abs(mob.x - user_x):
        if y_move(map, user_y, user_x, mob, list_mob, nb_mob, user, treasures, foods) == 1:
            return
        if x_move(map, user_x, user_y, mob, list_mob, nb_mob, user, treasures, foods) == 1:
            return
    else:
        if x_move(map, user_x, user_y, mob, list_mob, nb_mob, user, treasures, foods) == 1:
            return
        if y_move(map, user_y, user_x, mob, list_mob, nb_mob, user, treasures, foods) == 1:
            return

def x_move(map, user_x, user_y, mob, list_mob, nb_mob, user, treasures, foods):

    if mob.x < user_x:
        if mob.x + 1 == user_x and mob.y - user_y == 0:
            return 0
        valid,s = wall.wall(map, mob.y, mob.x + 1, list_mob, nb_mob, user, treasures, foods)
        if valid == 1:
            mob.x = mob.x + 1
        return valid
    else:
        if mob.x == user_x:
            return 0
        if mob.x - 1 == user_x and mob.y - user_y == 0:
            return 0
        valid,s = wall.wall(map, mob.y, mob.x - 1, list_mob, nb_mob, user, treasures, foods)
        if valid == 1:
            mob.x = mob.x - 1
        return valid

def y_move(map, user_y, user_x, mob, list_mob, nb_mob, user, treasures, foods):
    if mob.y < user_y:
        if mob.y + 1 == user_y and mob.x - user_x == 0:
            return 0
        valid,s = wall.wall(map, mob.y + 1 , mob.x, list_mob, nb_mob, user, treasures, foods)
        if valid == 1:
            mob.y = mob.y + 1
        return valid
    else:
        if mob.y == user_y:
            return 0
        if mob.y - 1 == user_y and mob.x - user_x == 0:
            return 0
        valid,s = wall.wall(map, mob.y - 1 , mob.x, list_mob, nb_mob, user, treasures, foods)
        if valid == 1:
            mob.y = mob.y - 1
        return valid
