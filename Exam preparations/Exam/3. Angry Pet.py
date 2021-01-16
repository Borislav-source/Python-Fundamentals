def check(price_type, price):
    the_sum = 0
    if price_type == 'positive':
        if price > 0:
            the_sum += price
    elif price_type == 'negative':
        if price < 0:
            the_sum += price
    elif price_type == 'all':
        the_sum += price
    return the_sum


def calculations(new_list, entry_price, type_of_items, price_type):
    the_sum = 0
    for price in new_list:
        if type_of_items == 'cheap':
            if entry_price > price:
                the_sum = check(price_type, price)
        elif type_of_items == 'expensive':
            if entry_price <= price:
                the_sum = check(price_type, price)
    return the_sum


price_ratings = list(map(int, input().split()))
entry_point = int(input())
type_of_items = input()
price_type = input()
entry_price = price_ratings[entry_point]

left_side = price_ratings[:entry_point]
right_side = price_ratings[entry_point + 1:]

left = calculations(left_side, entry_price, type_of_items, price_type)
right = calculations(right_side, entry_price, type_of_items, price_type)

if left >= right:
    print(f"Left - {left}")
else:
    print(f"Right - {right}")
