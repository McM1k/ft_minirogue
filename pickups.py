import random
import level

treasure_symbol = u'\u2671'.encode('utf-8')
food_symbol = u'\u262c'.encode('utf-8')
armor_symbol = u'\u16e5'.encode('utf-8')
weapon_symbol = u'\u16cf'.encode('utf-8')
scroll_symbol = u'\u1599'.encode('utf-8')
potion_symbol = u'\u00a1'.encode('utf-8')

class treasure:

    def __init__(s, map, number):
        count = 0
        for j in range (25):
            for i in range (80):
                if map[j][i] == level.grass_symbol:
                    count = count + 1
        count = random.randint(1, count - 2)
        j = i = 0
        while j < 25:
            i = 0
            while i < 80:
                if map[j][i] == level.grass_symbol:
                    count = count - 1
                    if count == -1:
                        map[j][i] = treasure_symbol
                i = i + 1
            j = j + 1

        s.number = number
        s.pos_x = i
        s.pos_y = j
        s.value = random.randint(50, 100)

    def __del__(s):
        s.pos_x = 0
        s.pos_y = 0

    def collect(s, user):
        user.gold = user.gold + s.value
        del(s)
        return user

class food:

    def __init__(s, map, number):
        count = 0
        for j in range (25):
            for i in range (80):
                if map[j][i] == level.grass_symbol:
                    count = count + 1
        count = random.randint(1, count - 2)
        j = i = 0
        while j < 25:
            i = 0
            while i < 80:

                if map[j][i] == level.grass_symbol:
                    count = count - 1
                    if count == -1:
                        map[j][i] = food_symbol
                i = i + 1
            j = j + 1

        s.number = number
        s.pos_x = i
        s.pos_y = j
        s.rations = random.randint(1, 3)

    def __del__(s):
        s.pos_x = 0
        s.pos_y = 0

    def collect(s, user):
        user.ration = user.ration + s.rations
        del(s)
        return user

def placefoods(map):
    foods = [food(map, 0)] * 1
    for i in range(1):
        foods[i] = food(map, i)
    return foods

def placetreasures(map):
    treasures = [treasure(map, 0)] * 3
    for i in range(3):
        treasures[i] = treasure(map, i)
    return treasures

def drawpickups(map, treasures, foods):
    for i in range(3):
        map[treasures[i].pos_y][treasures[i].pos_x] = treasure_symbol
    for i in range(1):
        map[foods[i].pos_y][foods[i].pos_x] = food_symbol
    return map