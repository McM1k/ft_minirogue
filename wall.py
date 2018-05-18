# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    wall.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bcozic <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/06 18:04:04 by bcozic            #+#    #+#              #
#    Updated: 2018/01/07 23:11:21 by bcozic           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import level
import pickups

def wall(map, y, x, mob, nb_mob, user, treasures, foods):
    for i in range(nb_mob):
        if mob[i].x == x and mob[i].y == y:
            return (2, mob[i])
    if map[y - 1][x] == pickups.treasure_symbol:
        for i in range(len(treasures)):
            if y == treasures[i].pos_y and x == treasures[i].pos_x:
                user = treasures[i].collect(user)
                del(treasures[i])
        return (1, mob[0])

    if map[y - 1][x] == pickups.food_symbol:
        for i in range(len(foods)):
            if y == foods[i].pos_y and x == foods[i].pos_x:
                user = foods[i].collect(user)
                del(foods[i])
        return (1, mob[0])

    if map[y - 1][x] == level.grass_symbol\
            or map[y - 1][x] == level.door_symbol\
            or map[y - 1][x] == level.tunnel_symbol\
            or map[y - 1][x] == level.door_lvl_symbol:
        return (1, mob[0])
    return (0, mob[0])
