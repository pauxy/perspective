def gen2d(width,height):
    arr = []
    if width<0 or height<0:
        return arr
    for i in range(height):
        row = []
        for i in range(width):
            row.append(0)
        arr.append(row)
    return arr
