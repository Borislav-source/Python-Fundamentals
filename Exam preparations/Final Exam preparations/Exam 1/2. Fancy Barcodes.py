import re


def hasNumbers(inputString):
     return bool(re.search(r'\d', inputString))


n = int(input())


for _ in range(n):
    data = input()
    pattern = r"^@#+([A-Z][a-zA-Z0-9]{3}[a-zA-Z0-9]+[A-Z])@#+"
    word = re.findall(pattern, data)
    if any(word):
        if hasNumbers(*word):
            patt = r"\d"
            number = re.findall(patt, *word)
            print(f"Product group: {''.join(number)}")
        else:
            print('Product group: 00')
    else:
        print('Invalid barcode')
