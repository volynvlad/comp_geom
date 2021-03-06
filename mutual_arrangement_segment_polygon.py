from MathHelper import get_intersection_point as gtp
from MathHelper import param_t_for_line as par_t
from MathHelper import point_from_param_t
from MathHelper import vector1
from MathHelper import scalar
from MathHelper import max2
from MathHelper import min2
from LinesRelative import is_intersect
from IsInSimple import octano_test


def cyrus_beck(p, line):
    assert len(line) == 2
    assert len(line[0]) == 2
    assert len(line[1]) == 2
    a = line[0]
    b = line[1]
    p = p.copy()
    n = len(p)
    p.append(p[0])
    t0 = 0
    t1 = 1
    result = []
    for i in range(n):
        if is_intersect(a, b, p[i], p[i + 1]):
            point = gtp([p[i], p[i + 1]], line)
            temp_t = par_t(a, point, b)
            print("temp_t = ", temp_t)
            n = [p[i + 1][1] - p[i][1], p[i][0] - p[i + 1][0]]
            ab = [b[0] - a[0], b[1] - a[1]]
            c = scalar(n, ab)
            if c > 0:
                print("c > 0")
                t1 = min2(t1, temp_t)
            elif c < 0:
                print("c < 0")
                t0 = max2(t0, temp_t)
            else: #c == 0
                print("c == 0")
                parA = par_t(p[i], p[i + 1], a)
                parB = par_t(p[i], p[i + 1], b)
                if parA >= 0 and parA <= 1:
                    print("add a")
                    result.add(a)
                if parB >= 0 and parB <= 1:
                    print("add b")
                    result.add(b) 
                if len(result) == 2:
                    print("result" , result)
                    return result
                if len(result) == 0:
                    result.add(p[i])
                    result.add(p[i + 1])
                    print("result" , result)
                    return result
                if parA >= 0 and parA <= 1:
                    if parB > 1:
                        result.add(p[i + 1])
                    else:
                        result.add(p[i])
                    print("result" , result)
                    return result
                if parB >= 0 and parB <= 1:
                    if parA > 1:
                        result.add(p[i + 1])
                    else:
                        result.add(p[i])
                    print("result" , result)
                    return result

            print("t0 = %f, t1 = %f" % (t0, t1))
    if t0 == 0 and t1 == 1 and not octano_test(p, a):
        print("t0 == 0 and t1 == 1")
        return []
    if t0 > t1:
        print("t0 > t1")
        return []
    elif t0 == t1:
        print("t0 == t1")
        result.append(point_from_param_t(t0))
        return result
    else: #t0 < t1
        return [point_from_param_t(a, b, t0), point_from_param_t(a, b, t1)]

