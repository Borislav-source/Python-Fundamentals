n = int(input())
final_text = ''
condition = False
condition_2 = False
balance = False
t = 1
for i in range(0, n):
    text = input()
    final_text += text
for k in range(0, len(final_text)):
    if condition == True and final_text[k] == '(':
        print('UNBALANCED')
        break
    if condition == True and final_text[k] == ')':
        condition_2 = True
        condition = False
        t += 1
    else:
        if condition == True:
            condition_2 = False
    if final_text[k] == '(':
        condition = True
    if  final_text[k] == ')' and t == 1:
        print('UNBALANCED')
        break
if k + 1 == len(final_text):
    if condition_2 == True and condition == False:
        balance = True
        print('BALANCED')
    else:
        print('UNBALANCED')

