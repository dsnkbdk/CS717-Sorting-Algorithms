# Calculate the distance between two points
def calculate_dis(data):
    distance = math.sqrt((data[0][0] - data[1][0])**2 + (data[0][1] - data[1][1])**2)
    return distance

def select_point(u, r, distance, x_mid):
    for v in r:
        if v[0] < x_mid - distance:
            continue
        if v[0] > x_mid + distance:
            break
        if v[1] >= u[1] - distance and v[1] <= u[1] + distance:
            yield v

# The minimum distance between points spanning two parts
def combine(l, r, find_min, x_mid):

    distance = find_min[1]
    min_dis = find_min[1]
    pair = find_min[0]

    for u in l:
        if u[0] < x_mid - distance:
            continue
        for v in select_point(u, r, distance, x_mid):
            distance = calculate_dis([u, v])
            if distance < min_dis:
                min_dis = distance
                pair = [u,v]

    return [pair, min_dis]


def divide(data):

    n = len(data)
    data = sorted(data)

    if n <= 1:
        return None, float('inf')

    elif n == 2:
        return [data, calculate_dis(data)]
    
    else:
        half = n//2
        x_mid = (data[half-1][0] + data[half][0])/2
        
        l = data[:half]
        r = data[half:]
        
        rec_l = divide(l)
        rec_r = divide(r)

        if rec_l[1] < rec_r[1]:
            find_min = combine(l, r, rec_l, x_mid)
        else:
            find_min = combine(l, r, rec_r, x_mid)
        
        pair = find_min[0]
        min_dis = find_min[1]

    return [pair, min_dis]


if __name__ == "__main__":

    import sys
    import math

    data = []

    # for line in open(sys.argv[1], 'r'):
    for line in sys.stdin:

        line = line.strip().split(" ")
        newline = [int(x) for x in line]
        data.append(tuple(newline))

    print(int(divide(data)[1]**2))