grade = float(input())

def grade_in_words(grade):
    if 2 <= grade <= 2.99:
        return 'Fail'
    elif 3 <= grade <= 3.99:
        return 'Poor'
    elif 4 <= grade <= 4.99:
        return 'Good'
    elif 5 <= grade <= 5.49:
        return 'Very Good'
    elif 5.50 <= grade <= 6:
        return 'Excellent'
print(grade_in_words(grade))