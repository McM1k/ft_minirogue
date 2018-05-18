# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generate_mob.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bcozic <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/07 14:45:58 by bcozic            #+#    #+#              #
#    Updated: 2018/01/07 20:52:31 by bcozic           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def ran_mob(lvl, mode):
    nb_mob = 0
    mob = init_list_mob()
    for i in range(0, 26):
        if mob[i].lvl_min <= lvl and mob[i].lvl_max >= lvl and mode >= mob[i].mod:
            nb_mob = nb_mob + 1
    if nb_mob > 1:
        nb_mob = random.randint(1, nb_mob)
    for i in range(0, 26):
        if mob[i].lvl_min <= lvl and mob[i].lvl_max >= lvl and mode >= mob[i].mod:
            nb_mob = nb_mob - 1
            if nb_mob == 0:
                return (mob, i)

    return -1

class Mob:
    def __init__(self, index):
        self.index = index
        self.name = ""
        self.hd = 0
        self.hp = 0
        self.ac = 0
        self.lvl_min = 0
        self.lvl_max = 0
        nb_turn = 0
        self.damage = [Dice(0)] * 8
        self.mod = 0
        self.xp = 0
        self.x = 0
        self.y = 0

class Dice:
    def __init__(self, index):
        self.index = index
        self.nb_dice = 0
        self.value = 0

def init_list_mob():
    mob = [Mob(0)] * 26
    for i in range(0, 26):
        mob[i] = Mob(i)
        if (i == 0):
            mob[i].name = "the giant ant"
            mob[i].hd = 2
            mob[i].ac = 3
            mob[i].lvl_min = 3
            mob[i].lvl_max = 12
            mob[i].nb_turn = 1
            mob[i].damage[0] = Dice(0)
            mob[i].damage[0].nb_dice = 1
            mob[i].damage[0].value = 6
            mob[i].mod = 0
            mob[i].xp = 9
        elif (i == 1):
            mob[i].name = "the bat"
            mob[i].hd = 1
            mob[i].ac = 3
            mob[i].lvl_min = 1
            mob[i].lvl_max = 8
            mob[i].nb_turn = 1
            mob[i].damage[0] = Dice(0)
            mob[i].damage[0].nb_dice = 1
            mob[i].damage[0].value = 2
            mob[i].mod = 0
            mob[i].xp = 1
        elif (i == 2):
            mob[i].name = "the centaur"
            mob[i].hd = 4
            mob[i].ac = 4
            mob[i].lvl_min = 8
            mob[i].lvl_max = 17
            mob[i].nb_turn = 2
            for j in range(2):
                mob[i].damage[j] = Dice(j)
                mob[i].damage[j].nb_dice = 1
                mob[i].damage[j].value = 6
            mob[i].mod = 0
            mob[i].xp = 15
        elif (i == 3):
            mob[i].name = "the dragon"
            mob[i].hd = 10
            mob[i].ac = -1
            mob[i].lvl_min = 22
            mob[i].lvl_max = 9999
            mob[i].nb_turn = 3
            mob[i].damage[0] = Dice(0)
            mob[i].damage[0].nb_dice = 1
            mob[i].damage[0].value = 8
            mob[i].damage[1] = Dice(1)
            mob[i].damage[1].nb_dice = 1
            mob[i].damage[1].value = 8
            mob[i].damage[2] = Dice(2)
            mob[i].damage[2].nb_dice = 3
            mob[i].damage[2].value = 10
            mob[i].mod = 1
            mob[i].xp = 6800
        elif (i == 4):
            mob[i].name = "the floating eye"
            mob[i].hd = 1
            mob[i].ac = 9
            mob[i].lvl_min = 2
            mob[i].lvl_max = 11
            mob[i].nb_turn = 0
            mob[i].mod = 1
            mob[i].xp = 5
        elif (i == 5):
            mob[i].name = "the violet fungi"
            mob[i].hd = 8
            mob[i].ac = 3
            mob[i].lvl_min = 15
            mob[i].lvl_max = 24
            mob[i].nb_turn = 0
            mob[i].mod = 1
            mob[i].xp = 80
        elif (i == 6):
            mob[i].name = "the gnome"
            mob[i].hd = 1
            mob[i].ac = 5
            mob[i].lvl_min = 6
            mob[i].lvl_max = 15
            mob[i].nb_turn = 1
            mob[i].damage[0] = Dice(0)
            mob[i].damage[0].nb_dice = 1
            mob[i].damage[0].value = 8
            mob[i].mod = 0
            mob[i].xp = 7
        elif (i == 7):
            mob[i].name = "the hobgoblin"
            mob[i].hd = 1
            mob[i].ac = 5
            mob[i].lvl_min = 1
            mob[i].lvl_max = 10
            mob[i].nb_turn = 1
            mob[i].damage[0] = Dice(0)
            mob[i].damage[0].nb_dice = 1
            mob[i].damage[0].value = 8
            mob[i].mod = 0
            mob[i].xp = 3
        elif (i == 8):
            mob[i].name = "the invisible stalker"
            mob[i].hd = 8
            mob[i].ac = 3
            mob[i].lvl_min = 16
            mob[i].lvl_max = 25
            mob[i].nb_turn = 1
            mob[i].damage[0] = Dice(0)
            mob[i].damage[0].nb_dice = 4
            mob[i].damage[0].value = 4
            mob[i].mod = 0
            mob[i].xp = 120
        elif (i == 9):
            mob[i].name = "the jackal"
            mob[i].hd = 1
            mob[i].ac = 7
            mob[i].lvl_min = 1
            mob[i].lvl_max = 7
            mob[i].nb_turn = 1
            mob[i].damage[0] = Dice(0)
            mob[i].damage[0].nb_dice = 1
            mob[i].damage[0].value = 2
            mob[i].mod = 0
            mob[i].xp = 2
        elif (i == 10):
            mob[i].name = "the kobold"
            mob[i].hd = 1
            mob[i].ac = 7
            mob[i].lvl_min = 1
            mob[i].lvl_max = 6
            mob[i].nb_turn = 1
            mob[i].damage[0] = Dice(0)
            mob[i].damage[0].nb_dice = 1
            mob[i].damage[0].value = 4
            mob[i].mod = 0
            mob[i].xp = 1
        elif (i == 11):
            mob[i].name = "the leprechaun"
            mob[i].hd = 3
            mob[i].ac = 8
            mob[i].lvl_min = 7
            mob[i].lvl_max = 16
            mob[i].nb_turn = 1
            mob[i].damage[0] = Dice(0)
            mob[i].damage[0].nb_dice = 1
            mob[i].damage[0].value = 1
            mob[i].mod = 1
            mob[i].xp = 10
        elif (i == 12):
            mob[i].name = "the mimic"
            mob[i].hd = 7
            mob[i].ac = 7
            mob[i].lvl_min = 19
            mob[i].lvl_max = 9999
            mob[i].nb_turn = 1
            mob[i].damage[0] = Dice(0)
            mob[i].damage[0].nb_dice = 3
            mob[i].damage[0].value = 4
            mob[i].mod = 1
            mob[i].xp = 100
        elif (i == 13):
            mob[i].name = "the nymph"
            mob[i].hd = 3
            mob[i].ac = 9
            mob[i].lvl_min = 11
            mob[i].lvl_max = 20
            mob[i].nb_turn = 0
            mob[i].mod = 1
            mob[i].xp = 37
        elif (i == 14):
            mob[i].name = "the orc"
            mob[i].hd = 1
            mob[i].ac = 6
            mob[i].lvl_min = 4
            mob[i].lvl_max = 13
            mob[i].nb_turn = 1
            mob[i].damage[0] = Dice(0)
            mob[i].damage[0].nb_dice = 1
            mob[i].damage[0].value = 8
            mob[i].mod = 0
            mob[i].xp = 5
        elif (i == 15):
            mob[i].name = "the purple worm"
            mob[i].hd = 15
            mob[i].ac = 6
            mob[i].lvl_min = 21
            mob[i].lvl_max = 9999
            mob[i].nb_turn = 2
            mob[i].damage[0] = Dice(0)
            mob[i].damage[0].nb_dice = 2
            mob[i].damage[0].value = 12
            mob[i].damage[1] = Dice(1)
            mob[i].damage[1].nb_dice = 2
            mob[i].damage[1].value = 4
            mob[i].mod = 0
            mob[i].xp = 4000
        elif (i == 16):
            mob[i].name = "the quasit"
            mob[i].hd = 3
            mob[i].ac = 2
            mob[i].lvl_min = 10
            mob[i].lvl_max = 19
            mob[i].nb_turn = 3
            mob[i].damage[0] = Dice(0)
            mob[i].damage[0].nb_dice = 1
            mob[i].damage[0].value = 2
            mob[i].damage[1] = Dice(1)
            mob[i].damage[1].nb_dice = 1
            mob[i].damage[1].value = 2
            mob[i].damage[2] = Dice(0)
            mob[i].damage[2].nb_dice = 1
            mob[i].damage[2].value = 4
            mob[i].mod = 0
            mob[i].xp = 32
        elif (i == 17):
            mob[i].name = "the rust monster"
            mob[i].hd = 5
            mob[i].ac = 2
            mob[i].lvl_min = 9
            mob[i].lvl_max = 18
            mob[i].nb_turn = 0
            mob[i].damage = "0d0"
            mob[i].mod = 0
            mob[i].xp = 20
        elif (i == 18):
            mob[i].name = "the snake"
            mob[i].hd = 1
            mob[i].ac = 5
            mob[i].lvl_min = 1
            mob[i].lvl_max = 9
            mob[i].nb_turn = 1
            mob[i].damage[0] = Dice(0)
            mob[i].damage[0].nb_dice = 1
            mob[i].damage[0].value = 3
            mob[i].mod = 0
            mob[i].xp = 2
        elif (i == 19):
            mob[i].name = "the troll"
            mob[i].hd = 6
            mob[i].ac = 4
            mob[i].lvl_min = 13
            mob[i].lvl_max = 22
            mob[i].nb_turn = 3
            mob[i].damage[0] = Dice(0)
            mob[i].damage[0].nb_dice = 1
            mob[i].damage[0].value = 8
            mob[i].damage[1] = Dice(1)
            mob[i].damage[1].nb_dice = 1
            mob[i].damage[1].value = 8
            mob[i].damage[2] = Dice(2)
            mob[i].damage[2].nb_dice = 2
            mob[i].damage[2].value = 6
            mob[i].mod = 0
            mob[i].xp = 120
        elif (i == 20):
            mob[i].name = "the umber hulk"
            mob[i].hd = 8
            mob[i].ac = 2
            mob[i].lvl_min = 18
            mob[i].lvl_max = -1
            mob[i].nb_turn = 3
            mob[i].damage[0] = Dice(0)
            mob[i].damage[0].nb_dice = 3
            mob[i].damage[0].value = 4
            mob[i].damage[1] = Dice(1)
            mob[i].damage[1].nb_dice = 3
            mob[i].damage[1].value = 4
            mob[i].damage[2] = Dice(2)
            mob[i].damage[2].nb_dice = 2
            mob[i].damage[2].value = 5
            mob[i].mod = 0
            mob[i].xp = 200
        elif (i == 21):
            mob[i].name = "the vampire"
            mob[i].hd = 8
            mob[i].ac = 1
            mob[i].lvl_min = 20
            mob[i].lvl_max = 9999
            mob[i].nb_turn = 1
            mob[i].damage[0] = Dice(0)
            mob[i].damage[0].nb_dice = 1
            mob[i].damage[0].value = 10
            mob[i].mod = 0
            mob[i].xp = 350
        elif (i == 22):
            mob[i].name = "the wraith"
            mob[i].hd = 5
            mob[i].ac = 4
            mob[i].lvl_min = 14
            mob[i].lvl_max = 23
            mob[i].nb_turn = 1
            mob[i].damage[0] = Dice(0)
            mob[i].damage[0].nb_dice = 1
            mob[i].damage[0].value = 6
            mob[i].mod = 0
            mob[i].xp = 55
        elif (i == 23):
            mob[i].name = "the xorn"
            mob[i].hd = 7
            mob[i].ac = -2
            mob[i].lvl_min = 17
            mob[i].lvl_max = 26
            mob[i].nb_turn = 4
            for j in range(3):
                mob[i].damage[j] = Dice(j)
                mob[i].damage[j].nb_dice = 1
                mob[i].damage[j].value = 3
            mob[i].damage[3] = Dice(3)
            mob[i].damage[j].nb_dice = 4
            mob[i].damage[j].value = 6
            mob[i].mod = 0
            mob[i].xp = 190
        elif (i == 24):
            mob[i].name = "the yeti"
            mob[i].hd = 4
            mob[i].ac = 6
            mob[i].lvl_min = 12
            mob[i].lvl_max = 21
            mob[i].nb_turn = 1
            mob[i].damage[0] = Dice(0)
            mob[i].damage[0].nb_dice = 2
            mob[i].damage[0].value = 6
            mob[i].mod = 0
            mob[i].xp = 50
        elif (i == 25):
            mob[i].name = "the zombie"
            mob[i].hd = 2
            mob[i].ac = 8
            mob[i].lvl_min = 5
            mob[i].lvl_max = 14
            mob[i].nb_turn = 1
            mob[i].damage[0] = Dice(0)
            mob[i].damage[0].nb_dice = 1
            mob[i].damage[0].value = 8
            mob[i].mod = 0
            mob[i].xp = 6
    return mob
