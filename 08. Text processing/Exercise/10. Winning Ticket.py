tickets = input().split(',')
tickets = [t.strip() for t in tickets]
symbols = ['@', '#', '$', '^']
for ticket in tickets:
    left = False
    right = False
    jackpot = False
    le = 0
    rt = 0
    if len(ticket) == 20:
        left_ticket = ticket[:10]
        right_ticket = ticket[10:]
        for smbl in symbols:
            if ticket.count(smbl) == 20:
                print(f'ticket "{ticket}" - 10{smbl} Jackpot!')
                jackpot = True
                break
            elif left_ticket.count(smbl) >= 6 and right_ticket.count(smbl) >= 6:
                left = True
                right = True
                break
        if jackpot:
            continue
        if left is True and right is True:
            if smbl * 6 in left_ticket and smbl * 6 in right_ticket:
                left = True
                right = True
            else:
                left = False
                right = False
            if left is True and right is True:
                count_left = left_ticket.count(smbl)
                count_right = right_ticket.count(smbl)
                count = min(count_left, count_right)
                print(f'ticket "{ticket}" - {count}{smbl}')
            else:
                print(f'ticket "{ticket}" - no match')
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print(f"invalid ticket")
