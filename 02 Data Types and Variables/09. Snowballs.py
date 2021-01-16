number_of_snowballs = int(input())
max_size = 0
for i in range(1, number_of_snowballs + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow // snowball_time) ** snowball_quality
    if snowball_value > max_size:
        max_size = snowball_value
        a = snowball_snow
        b = snowball_time
        c = snowball_quality
print(f'{a} : {b} = {max_size} ({c})')