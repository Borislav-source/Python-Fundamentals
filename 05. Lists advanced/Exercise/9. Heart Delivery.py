neighborhood = list(map(int, input().split("@")))
command = input()
last_jump = 0
n = 0
while not command == 'Love!':
    n = 0
    command = command.split()
    length_jump = int(command[1])
    for house in range(last_jump, len(neighborhood)):
        if length_jump == n:
            if not neighborhood[house] == 0:
                neighborhood[house] -= 2
                last_jump = house
                if neighborhood[house] == 0:
                    print(f"Place {house} has Valentine's day.")
                    break
                else:
                    break
            else:
                last_jump = house
                print(f"Place {house} already had Valentine's day.")
                break
        elif length_jump > ((len(neighborhood) - 1) - last_jump):
            last_jump = 0
            if not neighborhood[0] == 0:
                neighborhood[0] -= 2
                if neighborhood[0] == 0:
                    print(f"Place 0 has Valentine's day.")
                break
            else:
                print(f"Place 0 already had Valentine's day.")
                break
        n += 1
    command = input()
failed = [el for el in neighborhood if el > 0]
print(f"Cupid's last position was {last_jump}. ")
if len(failed) > 0: print(f"Cupid has failed {len(failed)} places.")
else: print("Mission was successful.")
