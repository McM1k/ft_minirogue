import main
import random
nw_corner_symbol = u'\u2554'.encode('utf-8')
ne_corner_symbol = u'\u2557'.encode('utf-8')
sw_corner_symbol = u'\u255a'.encode('utf-8')
se_corner_symbol = u'\u255d'.encode('utf-8')
horizontal_symbol = u'\u2550'.encode('utf-8')
vertical_symbol = u'\u2551'.encode('utf-8')
grass_symbol = '.'
door_symbol = u'\u256c'.encode('utf-8')
tunnel_symbol = u'\u2591'.encode('utf-8')
door_lvl_symbol = u'\u22a0'.encode('utf-8')

class room:
    def __init__(s, i):
        s.number = i + 1
        s.pos_x = 0
        s.pos_y = 0
        s.size_x = 0
        s.size_y = 0
        s.door_n = False
        s.door_e = False
        s.door_s = False
        s.door_w = False

def checkPaths(roomsConnected, paths, tried, currentRoom):
    if (tried > 9):
        return roomsConnected

    if (currentRoom == 4):
        if (paths[6] == True and roomsConnected[5] == False):
            roomsConnected[5] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 5)
        if (paths[3] == True and roomsConnected[1] == False):
            roomsConnected[1] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 1)
        if (paths[5] == True and roomsConnected[3] == False):
            roomsConnected[3] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 3)
        if (paths[8] == True and roomsConnected[7] == False):
            roomsConnected[7] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 7)
    if (currentRoom == 1):
        if (paths[0] == True and roomsConnected[0] == False):
            roomsConnected[0] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 0)
        if (paths[1] == True and roomsConnected[2] == False):
            roomsConnected[2] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 2)
    if (currentRoom == 3):
        if (paths[2] == True and roomsConnected[0] == False):
            roomsConnected[0] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 0)
        if (paths[7] == True and roomsConnected[6] == False):
            roomsConnected[6] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 6)
    if (currentRoom == 7):
        if (paths[10] == True and roomsConnected[6] == False):
            roomsConnected[6] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 6)
        if (paths[11] == True and roomsConnected[8] == False):
            roomsConnected[8] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 8)
    if (currentRoom == 5):
        if (paths[4] == True and roomsConnected[2] == False):
            roomsConnected[2] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 2)
        if (paths[9] == True and roomsConnected[8] == False):
            roomsConnected[8] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 8)
    if (currentRoom == 0):
        if (paths[0] == True and roomsConnected[1] == False):
            roomsConnected[1] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 1)
        if (paths[2] == True and roomsConnected[3] == False):
            roomsConnected[3] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 3)
    if (currentRoom == 2):
        if (paths[1] == True and roomsConnected[1] == False):
            roomsConnected[1] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 1)
        if (paths[4] == True and roomsConnected[5] == False):
            roomsConnected[5] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 5)
    if (currentRoom == 8):
        if (paths[9] == True and roomsConnected[5] == False):
            roomsConnected[5] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 5)
        if (paths[11] == True and roomsConnected[7] == False):
            roomsConnected[7] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 7)
    if (currentRoom == 6):
        if (paths[7] == True and roomsConnected[3] == False):
            roomsConnected[3] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 3)
        if (paths[10] == True and roomsConnected[7] == False):
            roomsConnected[7] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 7)

    return roomsConnected

def placedoors(rooms):
    tunnel_nb = random.randrange(8, 11)
    tunnels = [False] * 12
    check = 0
    while check != 9:
        for i in range(tunnel_nb):
            tunnels[random.randrange(12)] = True
        roomsConnected = [False] * 9
        roomsConnected[4] = True
        roomsConnected = checkPaths(roomsConnected, tunnels, 0, 4)
        check = 0
        for i in range(9):
            if roomsConnected[i] == True:
                check = check + 1
    if tunnels[0]:
        rooms[0].door_e = rooms[1].door_w = True
    if tunnels[1]:
        rooms[1].door_e = rooms[2].door_w = True
    if tunnels[2]:
        rooms[0].door_s = rooms[3].door_n = True
    if tunnels[3]:
        rooms[1].door_s = rooms[4].door_n = True
    if tunnels[4]:
        rooms[2].door_s = rooms[5].door_n = True
    if tunnels[5]:
        rooms[3].door_e = rooms[4].door_w = True
    if tunnels[6]:
        rooms[4].door_e = rooms[5].door_w = True
    if tunnels[7]:
        rooms[3].door_s = rooms[6].door_n = True
    if tunnels[8]:
        rooms[4].door_s = rooms[7].door_n = True
    if tunnels[9]:
        rooms[5].door_s = rooms[8].door_n = True
    if tunnels[10]:
        rooms[6].door_e = rooms[7].door_w = True
    if tunnels[11]:
        rooms[7].door_e = rooms[8].door_w = True
    return rooms

def drawroom(size_y, size_x, pos_y, pos_x, map):
    if size_x == 1 and size_y == 1:
        map[pos_y][pos_x] = tunnel_symbol
    else:
        map[pos_y - 1][pos_x - 1] = nw_corner_symbol
        map[pos_y - 1][pos_x + size_x] = ne_corner_symbol
        map[pos_y + size_y][pos_x - 1] = sw_corner_symbol
        map[pos_y + size_y][pos_x + size_x] = se_corner_symbol
        for i in range(pos_x, pos_x + size_x):
            map[pos_y - 1][i] = horizontal_symbol
            map[pos_y + size_y][i] = horizontal_symbol
        for i in range(pos_y, pos_y + size_y):
            map[i][pos_x - 1] = vertical_symbol
            map[i][pos_x + size_x] = vertical_symbol
        for i in range(pos_y, pos_y + size_y):
            for j in range(pos_x, pos_x + size_x):
                map[i][j] = grass_symbol
    return map

def linkroomsx(d1y, d1x, d2y, d2x, map):
    i = d1x + 1
    j = d1y
    turn = random.randint(d1x + 1, d2x - 1)
    while i < turn:
        map[j][i] = tunnel_symbol
        i = i + 1

    if d2y > d1y:
        while j < d2y:
            map[j][i] = tunnel_symbol
            j = j + 1
    else:
        while j > d2y:
           map[j][i] = tunnel_symbol
           j = j - 1

    while i < d2x:
        map[j][i] = tunnel_symbol
        i = i + 1
    return map

def linkroomsy(d1y, d1x, d2y, d2x, map):
    j = d1y + 1
    i = d1x
    turn = random.randint(d1y + 1, d2y - 1)
    while j < turn:
        map[j][i] = tunnel_symbol
        j = j + 1

    if d2x > d1x:
        while i < d2x:
            map[j][i] = tunnel_symbol
            i = i + 1
    else:
        while i > d2x:
            map[j][i] = tunnel_symbol
            i = i - 1

    while j < d2y:
        map[j][i] = tunnel_symbol
        j = j + 1
    return map

def drawtunnels(rooms, map):
    for i in range(9):
        if rooms[i].door_e:
            if rooms[i].size_y == 1:
                door1_y = rooms[i].pos_y
                door1_x = rooms[i].pos_x
            else:
                door1_y = rooms[i].pos_y + random.randrange(0, rooms[i].size_y)
                door1_x = rooms[i].pos_x + rooms[i].size_x
                map[door1_y][door1_x] = door_symbol
            if rooms[i + 1].size_y == 1:
                door2_y = rooms[i + 1].pos_y
                door2_x = rooms[i + 1].pos_x
            else:
                door2_y = rooms[i + 1].pos_y + random.randrange(0, rooms[i + 1].size_y)
                door2_x = rooms[i + 1].pos_x - 1
                map[door2_y][door2_x] = door_symbol
            map = linkroomsx(door1_y, door1_x, door2_y, door2_x, map)

        if rooms[i].door_s:
            if rooms[i].size_y == 1:
                door1_y = rooms[i].pos_y
                door1_x = rooms[i].pos_x
            else:
                door1_x = rooms[i].pos_x + random.randrange(0, rooms[i].size_x)
                door1_y = rooms[i].pos_y + rooms[i].size_y
                map[door1_y][door1_x] = door_symbol
            if rooms[i + 3].size_y == 1:
                door2_y = rooms[i + 3].pos_y
                door2_x = rooms[i + 3].pos_x
            else:
                door2_x = rooms[i + 3].pos_x + random.randrange(0, rooms[i + 3].size_x)
                door2_y = rooms[i + 3].pos_y - 1
                map[door2_y][door2_x] = door_symbol
            map = linkroomsy(door1_y, door1_x, door2_y, door2_x, map)

    return map

def placerooms(rooms):
    small_rooms = 3
    i = 0
    while i < 9:
        rooms[i].size_x = random.randrange(1, 24)
        rooms[i].size_y = random.randrange(1, 5)
        if rooms[i].size_x == 1 or rooms[i].size_y == 1:
            if small_rooms:
                small_rooms = small_rooms - 1
                rooms[i].size_x = rooms[i].size_y = 1
            else:
                i = i - 1
        i = i + 1

    for i in range(9):
        x_min = (i % 3) * 27 + 1
        x_max = x_min + 23 - rooms[i].size_x
        if rooms[i].size_x == 24 or x_min == x_max:
            rooms[i].pos_x = x_min
        else:
            rooms[i].pos_x = random.randrange(x_min, x_max)

        y_min = (i / 3) * 8 + 1
        y_max = y_min + 4 - rooms[i].size_y
        if rooms[i].size_y == 24 or y_min == y_max:
            rooms[i].pos_y = y_min
        else:
            rooms[i].pos_y = random.randrange(y_min, y_max)
    return rooms

def newlevel(level):
    rooms = [room(0)] * 9
    for i in range(9):
        rooms[i] = room(i)
    rooms = placerooms(rooms)
    rooms = placedoors(rooms)
    map = [[' ' for y in range(81)] for x in range(81)]

    for i in range(9):
        map = drawroom(rooms[i].size_y, rooms[i].size_x, rooms[i].pos_y, rooms[i].pos_x, map)
    map = drawtunnels(rooms, map)
    return map
