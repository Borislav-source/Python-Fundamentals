todo_notes = input()
list_todo = [0 for _ in range(10)]
while not todo_notes == 'End':
    todo_notes = todo_notes.split('-')
    list_todo.insert(int(todo_notes[0]), todo_notes[1])
    todo_notes = input()
list_todo = [el for el in list_todo if not el == 0]
print(list_todo)