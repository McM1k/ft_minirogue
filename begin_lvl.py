# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    begin_lvl.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bcozic <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/07 14:39:39 by bcozic            #+#    #+#              #
#    Updated: 2018/01/07 23:21:20 by bcozic           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import generate_mob
import random
import level

def init_lvl(lvl, map):
    mob = [generate_mob.Mob(0)] * 4
    for i in range(0, 4):
        current_mob,index = generate_mob.ran_mob(lvl, 1)
        mob[i] = generate_mob.Mob(index)
        mob[i].name = current_mob[index].name
        mob[i].hd = current_mob[index].hd
        mob[i].hp = generate_hp(mob[i].hd)
        mob[i].ac = current_mob[index].ac
        mob[i].lvl_min = current_mob[index].lvl_min
        mob[i].lvl_max = current_mob[index].lvl_max
        mob[i].nb_turn = current_mob[index].nb_turn
        mob[i].damage = current_mob[index].damage
        mob[i].xp = current_mob[index].xp + (mob[i].hd / 10)
        mob[i].y,mob[i].x = choose_place(map)
    return mob

def generate_hp(nb_d):
    hp = 0
    for i in range(nb_d):
        hp = hp + random.randint(1, 8)
    return hp

def choose_place(map):
    nb_place = 0
    for y in range(1, 26):
        for x in range(80):
            if (map[y - 1][x] == '.'):
                nb_place = nb_place + 1
    if nb_place != 1:
        nb_place = random.randint(1, nb_place)
    for y in range(1, 26):
        for x in range(80):
            if (map[y - 1][x] == '.'):
                nb_place = nb_place - 1
                if nb_place == 0:
                    return (y, x)
    return (0, 0)

def init_door(map):
    y,x = choose_place(map)
    map[y - 1][x] = level.door_lvl_symbol
