text_input = input()
resource = text_input
iteration = 0
basket = {}

while not text_input == 'stop':
    iteration += 1
    if iteration % 2 is not 0:
        if text_input not in basket:
            basket[text_input] = 0
        resource = text_input
    else:
        basket[resource] += int(text_input)
    text_input = input()

for key, value in basket.items():
    print(f'{key} -> {value}')