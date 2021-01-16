orders_count = int(input())
order_price = 0
for order in range(orders_count):
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())
    price_for_coffee = (days * capsules) * price_per_capsule
    order_price += price_for_coffee
    print(f'The price for the coffee is: ${price_for_coffee:.2f}')

print(f"Total: ${order_price:.2f}")
