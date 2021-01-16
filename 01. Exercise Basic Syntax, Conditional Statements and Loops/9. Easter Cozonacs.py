budget = float(input())
flour_price = float(input())

current_cozonacs_count = 0
collored_eggs = 0
one_pack_eggs = flour_price * 0.75
milk_per_cozonac = ((flour_price * 0.25) + flour_price) / 4

price_per_cozunak = one_pack_eggs + milk_per_cozonac + flour_price

while budget > price_per_cozunak:
    budget -= price_per_cozunak
    current_cozonacs_count += 1
    collored_eggs += 3
    if current_cozonacs_count % 3 == 0:
        collored_eggs = collored_eggs - (current_cozonacs_count - 2)

print(f'You made {current_cozonacs_count} cozonacs! Now you have {collored_eggs} eggs and {budget:.2f}BGN left.')

