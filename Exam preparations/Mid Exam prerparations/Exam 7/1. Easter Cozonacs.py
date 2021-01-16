budget = float(input())
price_for_kilogram = float(input())
count = 0
current_eggs = 0
pack_of_eggs = price_for_kilogram * 0.75
milk = price_for_kilogram * 0.3125
price = price_for_kilogram + pack_of_eggs + milk

while budget > price:
    budget -= price
    count += 1
    current_eggs += 3
    if count % 3 == 0:
        current_eggs -= count - 2
print(f"You made {count} cozonacs! Now you have {current_eggs} eggs and {budget:.2f}BGN left.")