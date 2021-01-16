rows_number = int(input())
condition = False
moves = 0
for rows in range(rows_number):
    row = input()
    if len(row) == row.count('#') and rows is not 0:
        print('Kate cannot get out')
        condition = True
        break
    else:
        for i in row:
            if i == ' ':
                moves += 1
if condition:
    pass
else:
    print(f'Kate got out in {moves + 1} moves')


