from aocd import submit, get_data


def main():
    day = 20
    year = 2020
    data = get_data(day=day, year=year)

    test_data_a = {
"""Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...""": 20899048083289,
    }
    test_data_b = {
"""Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...""": 273,
    }

    for i, (test, true) in enumerate(test_data_a.items()):
        result = solve_a(test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_a = solve_a(data)
    print(f"result a: {result_a}\n")
    submit(result_a, part="a", day=day, year=year)

    for i, (test, true) in enumerate(test_data_b.items()):
        result = solve_b(test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_b = solve_b(data)
    print(f"result b: {result_b}\n")
    submit(result_b, part="b", day=day, year=year)


def getBorders(tile, maxLen):
    borders = []

    # top
    borders.append([tile[(0, x)] for x in range(maxLen+1)])
    # bottom
    borders.append([tile[(maxLen, x)] for x in range(maxLen+1)])
    # left
    borders.append([tile[(y, 0)] for y in range(maxLen+1)])
    # right
    borders.append([tile[(y, maxLen)] for y in range(maxLen+1)])

    return borders


def flip(tiles, _id, maxLen, horizontal=True):
    newTile = {}
    if horizontal:
        for y in range(maxLen+1):
            for x in range(maxLen, -1, -1):
                newTile[(y, maxLen-x)] = tiles[_id][(y, x)]
    else:
        for y in range(maxLen, -1, -1):
            for x in range(maxLen+1):
                newTile[(maxLen-y, x)] = tiles[_id][(y, x)]
    tiles[_id] = newTile


def rotate(tiles, _id, maxLen, times):
    for r in range(times):
        newTile = {}
        for y in range(maxLen+1):
            for x in range(maxLen+1):
                newTile[(y, x)] = tiles[_id][(maxLen-x, y)]
        tiles[_id] = newTile


def rotatedBorders(borders):
    newBorders = []
    # top
    newBorders.append(list(reversed(borders[2])))
    # bottom
    newBorders.append(list(reversed(borders[3])))
    # left
    newBorders.append(borders[1])
    # right
    newBorders.append(borders[0])
    return newBorders


def solve_a(data):
    tiles = {}
    for block in data.split("\n\n"):
        sblock = block.splitlines()
        _id = sblock[0].split()[1][:-1]
        tile = {}
        for y, line in enumerate(sblock[1:]):
            for x, c in enumerate(line):
                tile[(y, x)] = c
        tiles[_id] = tile
    maxLen = max(y for y, x in next(iter(tiles.values())).keys())
    matches = {}
    for _id, tile in tiles.items():
        borders = getBorders(tile, maxLen)
        for other, otile in tiles.items():
            if _id == other:
                continue
            oborders = getBorders(otile, maxLen)
            for border in borders:
                if border in oborders or list(reversed(border)) in oborders:
                    if _id in matches:
                        matches[_id].add(other)
                    else:
                        matches[_id] = {other}
                    if other in matches:
                        matches[other].add(_id)
                    else:
                        matches[other] = {_id}
                    break
    res = 1
    for k, v in matches.items():
        if len(v) == 2:
            res *= int(k)
    return res


def solve_b(data):
    tiles = {}
    for block in data.split("\n\n"):
        sblock = block.splitlines()
        _id = sblock[0].split()[1][:-1]
        tile = {}
        for y, line in enumerate(sblock[1:]):
            for x, c in enumerate(line):
                tile[(y, x)] = c
        # tile, rotation, flip vertical, flip horizontal
        tiles[_id] = tile

    maxLen = max(y for y, x in next(iter(tiles.values())).keys())

    # neighbours = {_id: {} for _id in tiles}
    neighbours = {list(tiles)[0]: {}}
    # get neighbours with rotation
    done = set()
    while len(done) < len(tiles):
        for _id in tiles:
            if _id not in neighbours:
                continue
            done.add(_id)
            # top, bottom, left, right
            borders = getBorders(tiles[_id], maxLen)
            # for i in range(list(tiles).index(_id) + 1, len(tiles)):
            for oid in tiles:
                # oid = list(tiles)[i]
                if _id == oid:
                    continue
                connected = False
                oborders = getBorders(tiles[oid], maxLen)
                for j, oborder in enumerate(oborders):
                    if oborder in borders or list(reversed(oborder)) in borders:
                        connected = True
                        if oid not in neighbours:
                            neighbours[oid] = {}
                if connected:
                    stop = True
                    if oborders[1] == borders[0]:
                        neighbours[_id]["up"] = oid
                        neighbours[oid]["down"] = _id
                    elif oborders[0] == borders[1]:
                        neighbours[_id]["down"] = oid
                        neighbours[oid]["up"] = _id
                    elif oborders[3] == borders[2]:
                        neighbours[_id]["left"] = oid
                        neighbours[oid]["right"] = _id
                    elif oborders[2] == borders[3]:
                        neighbours[_id]["right"] = oid
                        neighbours[oid]["left"] = _id

                    # try flipped
                    elif list(reversed(oborders[1])) == borders[0]:
                        neighbours[_id]["up"] = oid
                        neighbours[oid]["down"] = _id
                        flip(tiles, oid, maxLen)
                    elif list(reversed(oborders[0])) == borders[1]:
                        neighbours[_id]["down"] = oid
                        neighbours[oid]["up"] = _id
                        flip(tiles, oid, maxLen)
                    elif list(reversed(oborders[3])) == borders[2]:
                        neighbours[_id]["left"] = oid
                        neighbours[oid]["right"] = _id
                        flip(tiles, oid, maxLen, False)
                    elif list(reversed(oborders[2])) == borders[3]:
                        neighbours[_id]["right"] = oid
                        neighbours[oid]["left"] = _id
                        flip(tiles, oid, maxLen, False)
                    else:
                        stop = False

                    # try rotated rotate
                    for r in range(1, 4):
                        if stop:
                            break
                        oborders = rotatedBorders(oborders)
                        if oborders[1] == borders[0]:
                            neighbours[_id]["down"] = oid
                            neighbours[oid]["up"] = _id
                            rotate(tiles, oid, maxLen, r)
                            stop = True
                        elif oborders[0] == borders[1]:
                            neighbours[_id]["up"] = oid
                            neighbours[oid]["down"] = _id
                            rotate(tiles, oid, maxLen, r)
                            stop = True
                        elif oborders[3] == borders[2]:
                            neighbours[_id]["left"] = oid
                            neighbours[oid]["right"] = _id
                            rotate(tiles, oid, maxLen, r)
                            stop = True
                        elif oborders[2] == borders[3]:
                            neighbours[_id]["right"] = oid
                            neighbours[oid]["left"] = _id
                            rotate(tiles, oid, maxLen, r)
                            stop = True

                        # try flipped
                        elif list(reversed(oborders[1])) == borders[0]:
                            neighbours[_id]["down"] = oid
                            neighbours[oid]["up"] = _id
                            rotate(tiles, oid, maxLen, r)
                            flip(tiles, oid, maxLen)
                            stop = True
                        elif list(reversed(oborders[0])) == borders[1]:
                            neighbours[_id]["up"] = oid
                            neighbours[oid]["down"] = _id
                            rotate(tiles, oid, maxLen, r)
                            flip(tiles, oid, maxLen)
                            stop = True
                        elif list(reversed(oborders[3])) == borders[2]:
                            neighbours[_id]["left"] = oid
                            neighbours[oid]["right"] = _id
                            rotate(tiles, oid, maxLen, r)
                            flip(tiles, oid, maxLen, False)
                            stop = True
                        elif list(reversed(oborders[2])) == borders[3]:
                            neighbours[_id]["right"] = oid
                            neighbours[oid]["left"] = _id
                            rotate(tiles, oid, maxLen, r)
                            flip(tiles, oid, maxLen, False)
                            stop = True

    right = next(_id for _id, neighs in neighbours.items()
                 if "right" not in neighs and "up" not in neighs)
    ids = []
    while True:
        cur = right
        line = []
        while True:
            line.append(cur)
            if "left" not in neighbours[cur]:
                break
            cur = neighbours[cur]["left"]
        ids.append(line)
        if "down" not in neighbours[right]:
            break
        right = neighbours[right]["down"]

    pic = {}
    # build big image
    left = next(_id for _id, neighs in neighbours.items()
                if "left" not in neighs and "up" not in neighs)
    y = 0
    while True:
        x = 0
        cur = left
        while True:
            tile = tiles[cur]
            # for ty in range(0, maxLen+1):
                # for tx in range(0, maxLen+1):
            for ty in range(1, maxLen):
                for tx in range(1, maxLen):
                    if tile[(ty, tx)] == "#":
                        # pic[(ty-1+(maxLen-1)*y, tx-1+(maxLen-1)*x)] = "#"
                        # pic[(ty+(maxLen*y), tx+maxLen*x)] = "#"
                        pic[(ty+(maxLen-1)*y, tx+(maxLen-1)*x)] = "#"
                    # else:
                        # # pic[(ty+(maxLen*y), tx+maxLen*x)] = "."
                        # pic[(ty+(maxLen-1)*y, tx+(maxLen-1)*x)] = "."
            if "right" not in neighbours[cur]:
                break
            x += 1
            cur = neighbours[cur]["right"]
        y += 1
        if "down" not in neighbours[left]:
            break
        left = neighbours[left]["down"]

    maxLen = max(y for y, x in pic)

    # find monsters
    smonster = (
        "                  # \n"
        "#    ##    ##    ###\n"
        " #  #  #  #  #  #   \n"
    )
    monster = set()
    for my, line in enumerate(smonster.splitlines()):
        for mx, c in enumerate(line):
            if c == "#":
                monster.add((my, mx))
    found = 0
    for r in range(4):
        maxx = max(x for y, x in monster) + 1
        newMonster = set()
        for my, mx in monster:
            newMonster.add((maxx-mx, my))
        monster = newMonster
        for y in range(maxLen):
            for x in range(maxLen):
                if all((my+y, mx+x) in pic for my, mx in monster):
                    found += 1
        if found:
            break
    return len(pic) - found*15


if __name__ == "__main__":
    main()
