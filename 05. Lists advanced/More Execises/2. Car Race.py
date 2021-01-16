def time_count(car):
    summ = 0
    if car == 1:
        for time in range(finish):
            if times[time] == 0:
                summ *= 0.8
            else:
                summ += times[time]
    elif car == 2:
        for time in range(1, finish + 1):
            if times[-time] == 0:
                summ *= 0.8
            else:
                summ += times[-time]
    return round(summ, 2)


times = list(map(int, input().split()))
finish = len(times) // 2
car1 = time_count(car=1)
car2 = time_count(car=2)

if car1 < car2:
    print(f'The winner is left with total time: {car1:,g}')
else:
    print(f'The winner is right with total time: {car2:,g}')

