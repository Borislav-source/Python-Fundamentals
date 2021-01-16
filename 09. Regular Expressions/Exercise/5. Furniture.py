import re
data = input()
end_price = 0
products = []
while not data == 'Purchase':
    pattern = r">>[a-zA-Z]+<<\d+[0-9.]+!\d+"
    valid = re.findall(pattern, data)
    if data in valid:
        price_pattern = r"(\d+[.0-9]+)!"
        price = re.findall(price_pattern, data)
        amount_pattern = r"!(\d+)"
        amount = re.findall(amount_pattern, data)
        product_pattern = r">([a-zA-Z]+)<"
        product = re.findall(product_pattern, data)
        products.append(*product)
        price = float(*price)
        amount = int(*amount)
        end_price += price * amount
    data = input()
print('Bought furniture:')
for p in products:
    print(p)
print(f"Total money spend: {end_price:.2f}")
