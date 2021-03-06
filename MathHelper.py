import math
def min2(a, b):
    if a < b:
        return a
    else:
        return b


def max2(a, b):
    if a > b:
        return a
    else:
        return b


def determinant(p1, p2, p):
    assert len(p1) == 2
    assert len(p2) == 2
    assert len(p) == 2
    return (p2[0] - p1[0])*(p[1] - p1[1]) - (p2[1] - p1[1])*(p[0] - p1[0])


def length(p1, p2 = [0, 0]):
    assert len(p1) == 2
    assert len(p2) == 2
    return math.sqrt((p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1]))


def angle(p1, p0, p2):
    """
    returns angle p1p0p2 
    """
    assert len(p1) == 2
    assert len(p0) == 2
    assert len(p2) == 2
    ca = (p1[0] - p0[0])*(p2[0] - p0[0]) + (p1[1] - p0[1])*(p2[1] - p0[1])
    ca = ca / (length(p1, p0) * length(p2, p0))
    ca = math.acos(ca)
    return ca


def min_and_max(p):
    minimum = p[0]
    maximum = p[0]
    for i in range(len(p)):
        if minimum > p[i]:
            minimum = p[i]
        if maximum < p[i]:
            maximum = p[i]
    return minimum, maximum


def vector1(p1, p2):
    assert len(p1) == 2
    assert len(p2) == 2
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]

    return [x2 - x1, y2 - y1]


def point_min(p):
    """
    :param p: points
    :return: max by x and if needed min by y
    """
    minimum = p[0]
    for i in range(len(p)):
        if minimum[1] == p[i][1] and minimum[0] > p[i][0]:
            minimum = p[i]
        if minimum[1] <= p[i][1]:
            minimum = p[i]
    return minimum

def point_min1(p):
    """
    :param p: points
    :return: min by x and if needed min by y
    """
    minimum = p[0]
    for i in range(len(p)):
        if minimum[1] == p[i][1] and minimum[0] < p[i][0]:
            minimum = p[i]
        if minimum[1] <= p[i][1]:
            minimum = p[i]
    return minimum


def point_min_by_x(p):
    """
    p - points
    return - min by x and if needed min by y
    """
    minimum = p[0]
    for i in p:
        if minimum[0] == i[0] and minimum[1] > i[0]:
            minimum = i
        if minimum[0] >= i[0]:
            minimum = i
    return minimum


def point_max_by_x(p):
    """
    p - points
    return - max by x and if needed min by y
    """
    maximum = p[0]
    for i in p:
        if maximum[0] == i[0] and maximum[1] > i[0]:
            maximum = i
        if maximum[0] <= i[0]:
            maximum = i
    return maximum


def oct(v):
    assert len(v) == 2
    x = v[0]
    y = v[1]
    if 0 <= y < x:
        return 1
    if 0 < x <= y:
        return 2
    if 0 <= -x < y:
        return 3
    if 0 < y <= -x:
        return 4
    if 0 <= -y < -x:
        return 5
    if 0 < -x <= -y:
        return 6
    if 0 <= x < -y:
        return 7
    if 0 < -y <= x:
        return 8
    return 0


def cos_num(p1, p2):
    assert len(p1) == 2
    assert len(p2) == 2
    return (p2[0] - p1[0]) / length(p1, p2)


def cos_num_abs(p1, p2):
    assert len(p1) == 2
    assert len(p2) == 2

    return math.fabs(p2[0] - p1[0]) / length(p1, p2)

def cos_3points(p1, p0, p2):
    v1 = vector1(p0, p1)
    v2 = vector1(p0, p2)

    return scalar(v1, v2) / (length(p1, p0) * length(p2, p0))


def scalar(p1, p2):
    assert len(p1) == 2
    assert len(p2) == 2
    return p1[0] * p2[0] + p1[1] * p2[1]


def triangle_square(p1, p2, p3):
    assert len(p1) == 2
    assert len(p2) == 2
    assert len(p3) == 2
    return abs(determinant(p1, p2, p3)) / 2


def perimeter(p):
    sum = 0
    for i in range(len(p)):
        sum = sum + length(p[i - 1], p[i])
    return sum


def distance(p1, p2, p):
    assert len(p1) == 2
    assert len(p2) == 2
    assert len(p) == 2
    A = p1[1] - p2[1]
    B = p2[0] - p1[0]
    C = p1[0] * p2[1] - p2[0] * p1[1]
    return abs(A * p[0] + B * p[1] + C) / math.sqrt(A ** 2 + B ** 2)


def gcd(a, b):
    assert a > 0
    assert b > 0
    while b:
        a, b = b, a % b
    return a


def mcd(a, b):
    assert a > 0
    assert b > 0
    return (a / gcd(a, b)) * b


def get_intersection_point(line1, line2):
    assert len(line1) == 2
    assert len(line2) == 2
    assert len(line1[0]) == 2
    assert len(line1[1]) == 2
    assert len(line2[0]) == 2
    assert len(line2[1]) == 2

    x = []
    y = []

    A1 = line1[1][1] - line1[0][1]
    B1 = line1[0][0] - line1[1][0]
    C1 = -line1[0][0] * line1[1][1] + line1[0][1] * line1[1][0]
    A2 = line2[1][1] - line2[0][1]
    B2 = line2[0][0] - line2[1][0]
    C2 = -line2[0][0] * line2[1][1] + line2[0][1] * line2[1][0]
    if A1 == 0:
        y = line1[0][1]
    if A2 == 0:
        y = line2[0][1]
    if B1 == 0:
        x = line1[0][0]
    if B2 == 0:
        x = line2[0][0]
    if x != [] and y != []: # lines - (horizontal and vertical)
        return [x, y]
    else:
        if x != []: # one line horizontal
            if B1 == 0:
                return [x, -(C2 + A2 * x) / B2]
            else:
                return [x, -(C1 + A1 * x) / B1]
        elif y != []: # one line vertical
            if A1 == 0:
                return [-(B2 * y + C2) / A2, y]
            else:
                return [-(B1 * y + C1) / A1, y]
        else: # 2 lines neither vertical not horizontal
            if A1 < 0:
                A1 = -A1
                B1 = -B1
                C1 = -C1
            if A2 < 0:
                A2 = -A2
                B2 = -B2
                C2 = -C2
            A = mcd(A1, A2)
            B1 = B1 * A / A1
            C1 = C1 * A / A1
            A1 = A
            B2 = B2 * A / A2
            C2 = C2 * A / A2
            A2 = A

            y = -(C1 - C2) / (B1 - B2)
            x = -(B1 * y + C1) / A1
            return [x, y]


def param_t_for_line(start, point, end):
    assert len(start) == 2
    assert len(point) == 2
    assert len(end) == 2
    assert not start == end
    return length(start, point) / length(start, end)

def point_from_param_t(a, b, t):
    assert len(a) == 2
    assert len(b) == 2
    return [int(a[0] * (1 - t) + b[0] * t), int(a[1] * (1 - t) + b[1] * t)]

def sorted_by_x(points):
    """
    get points
    return:
        sorted points by x
    """
    points = points.copy()
    #assert points[0] == 2
    for i in range(len(points)):
        for j in range(len(points)):
            if points[i][0] < points[j][0]:
                points[i], points[j] = points[j], points[i]

    return points


def sorted_by_y(points):
    """
    get points
    return:
        sorted points by y
    """
    points = points.copy()
    #assert points[0] == 2
    for i in range(len(points)):
        for j in range(len(points)):
            if points[i][1] > points[j][1]:
                points[i], points[j] = points[j], points[i]

    return points


def is_delonay_condition(p1, p2, p3, p4):
    """
    p1, p2, p3 - triangle
    p2, p3, p4 - triangle
    p2, p3 - same side of the triangles
    """
    cA = ((p2[0] - p1[0]) * (p3[0] - p1[0]) +
                 (p2[1] - p1[1]) * (p3[1] - p1[1])) 
    cB = ((p2[0] - p4[0]) * (p3[0] - p4[0]) +
                 (p2[1] - p4[1]) * (p3[1] - p4[1])) 
    if cA >= 0 and cB >= 0:
        return True
    elif cA < 0 and cB < 0:
        return False
    else:
        return (
                abs((p2[0] - p1[0]) * (p3[1] - p1[1]) - 
                    (p3[0] - p1[0]) * (p2[1] - p1[1])) * cB 
                    +
                abs((p2[0] - p4[0]) * (p3[1] - p4[1]) - 
                    (p3[0] - p4[0]) * (p2[1] - p4[1])) * cA            
                ) >= 0

def is_distinct_points(points, point_q):
    assert len(point_q) == 2
    assert len(points) > 0
    result = True
    for point in points:
        if point == point_q:
            result = False
            break
    return result

def start_line(points):
    first = point_min(points)
    max_cos = -1
    for point in points:
        if first != point: 
            cos_tmp = cos_num(first, point) 
            if cos_tmp > max_cos and point != first: 
                max_cos = cos_tmp
                second = point
    return [first, second]


def angle_between_vectors(v1, v2):
    return math.acos(scalar(v1, v2) / (length(v1) * length(v2)) )


def biggest_angle(points, q1, q2):
    angle = 0
    result = []
    for point in points:
        if point != q1 and point != q2:
            angle_tmp = angle_between_vectors(vector1(point, q1), vector1(point, q2))
            if angle_tmp > angle and determinant(q1, q2, point) < 0:
                angle = angle_tmp
                result = point
    return result

def exists(a, b, c, arr):
    """
    a, b, c - points
    arr - array of sides
    """
    for i in range(len(arr) - 3):
        tmp_sides = arr[i:i + 3]
        if a in tmp_sides and b in tmp_sides and c in tmp_sides:
            return True
    return False





