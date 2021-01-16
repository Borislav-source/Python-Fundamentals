neighborhood = list(map(int, input().split("@")))
landing = 0
while True:
    data = input()
    if data == "Love!":
        break
    data = data.split()
    jump = int(data[1])
    landing += jump
    if landing <= len(neighborhood) - 1:
        if neighborhood[landing] > 0:
            neighborhood[landing] -= 2
            if neighborhood[landing] == 0:
                print(f"Place {landing} has Valentine's day.")
        else:
            print(f"Place {landing} already had Valentine's day.")
    else:
        landing = 0
        if neighborhood[0] > 0:
            neighborhood[0] -= 2
            if neighborhood[0] == 0:
                print(f"Place {landing} has Valentine's day.")
        else:
            print(f"Place {landing} already had Valentine's day.")

failed_places = len([place for place in neighborhood if place > 0])
print(f"Cupid's last position was {landing}.")
if failed_places > 0:
    print(f"Cupid has failed {failed_places} places.")
else:
    print(f"Mission was successful.")
