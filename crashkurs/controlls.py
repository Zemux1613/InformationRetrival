def sort(a, b, c):
    max = 0
    if a > b and a > c:
        max = a
    elif b > a and b > c:
        max = b
    elif c > a and c > b:
        max = c

    low = 0
    if a < b and a < c:
        low = a
    elif b < a and b < c:
        low = b
    elif c < a and c < b:
        low = c

    other = 0
    if max == a and low == b or max == b and low == b:
        other = c
    elif max == c and low == a or max == a and low == c:
        other = b
    elif max == b and low == c or max == c and low == b:
        other = a

    return low, other, max

def price(station1, station2):
    price = 2

    road_map = {
        11: [12, 21, 31],
        12: [13, 11],
        13: [12],
        21: [11, 22],
        22: [21, 23],
        23: [22],
        31: [11, 32],
        32: [31, 33],
        33: [32]
    }

    if station1 in road_map:
        if station2 in road_map[station1]:
            price -= 1

    inner_cycle = [11, 21, 31]
    last_stations = [13, 23, 33]

    if station1 in inner_cycle and station2 not in inner_cycle:
        price += 1

    if station2 in last_stations or station1 in last_stations:
        price += 1

    if station1 == station2:
        return 0

    return price