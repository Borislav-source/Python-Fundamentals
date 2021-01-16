def coordinate_system(coordinate_system_1, coordinate_system_2):
    if sum(coordinate_system_1) < sum(coordinate_system_2):
        print((int(coordinate_x), int(coordinate_y)))
    elif sum(coordinate_system_1) > sum(coordinate_system_2):
        print((int(coordinate_x1), int(coordinate_y1)))
    else:
        print((int(coordinate_x), int(coordinate_y)))


coordinate_x = float(input())
coordinate_y = float(input())
coordinate_x1 = float(input())
coordinate_y1 = float(input())

coordinate_system_1 = [abs(coordinate_x), abs(coordinate_y)]
coordinate_system_2 = [abs(coordinate_x1), abs(coordinate_y1)]
coordinate_system(coordinate_system_1, coordinate_system_2)

