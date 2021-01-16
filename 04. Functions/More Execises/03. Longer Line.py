def longest_line(point_1, point_2, point_3, point_4):
    firs_line = abs(sum(point_1) - sum(point_2))
    second_line = abs(sum(point_3) - sum(point_4))
    if firs_line > second_line:
        if not abs(sum(point_1)) > abs(sum(point_2)):
            print(f'{(int(coordinate_x), int(coordinate_y))}{(int(coordinate_x1), int(coordinate_y1))}')
        else:
            print(f'{(int(coordinate_x1), int(coordinate_y1))}{(int(coordinate_x), int(coordinate_y))}')
    elif firs_line < second_line:
        if not abs(sum(point_3)) > abs(sum(point_4)):
            print(f'{(int(coordinate_z), int(coordinate_k))}{(int(coordinate_z1), int(coordinate_k1))}')
        else:
            print(f'{(int(coordinate_z1), int(coordinate_k1))}{(int(coordinate_z), int(coordinate_k))}')
    else:
        if not abs(sum(point_1)) > abs(sum(point_2)):
            print(f'{(int(coordinate_x), int(coordinate_y))}{(int(coordinate_x1), int(coordinate_y1))}')
        else:
            print(f'{(int(coordinate_x1), int(coordinate_y1))}{(int(coordinate_x), int(coordinate_y))}')


coordinate_x = float(input())
coordinate_y = float(input())
coordinate_x1 = float(input())
coordinate_y1 = float(input())

coordinate_z = float(input())
coordinate_k = float(input())
coordinate_z1 = float(input())
coordinate_k1 = float(input())

point_1 = [coordinate_x, coordinate_y]
point_2 = [coordinate_x1, coordinate_y1]
point_3 = [coordinate_z, coordinate_k]
point_4 = [coordinate_z1, coordinate_k1]

longest_line(point_1, point_2, point_3, point_4)
