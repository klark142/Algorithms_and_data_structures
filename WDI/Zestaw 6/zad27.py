def not_cross(x, x1, y, y1, squares):
    if not squares:
        return True
    for square in squares:
        #todo
        return False

def area(x1, x2, y1, y2):
    return (x2 - x1) * (y2 - y1)


def solve(t, index, area, to_find, already_chosen):
    if area == 2012 and not to_find:
        return True
    x1, x2, y1, y2 = T[index]
    if not_cross((x1, x2, y1, y2), already_chosen):
        square_area = area(x1, x2, y1, y2)
        # nie bierzemy
        if solve(t, index + 1, area, to_find - 1, already_chosen):
            return True
        else: 
            already_chosen[13 - to_find - 1] = (x1, x2, y1, y2)
            if solve(t, index + 1, area - square_area, to_find - 1, already_chosen):
                return True
    return False
