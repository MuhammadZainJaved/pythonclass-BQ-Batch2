no_of_students = int(input("How many students in your class ? "))
'''
while condition:
    do something
    update condition - monitor - change
'''
sample_lst = [[
    'Zain', 'Ahmed', [60, 70, 61] , 300
],
[
    'Amjad', 'Asfar', [60, 70, 61] , 300
]
]
n = 0
lst_of_students_data = []
while n < no_of_students:
    name = input(f"What is your {n+1}th student name ??")
    fname = input(f"What is your {n+1}th student's father name ??")
    number_of_subjects = int(input("How many subjects attempted ??"))
    total_marks = int(input("what are the total marks ??"))
    subject_marks = []
    # subject_marks.append(arguments)
    if number_of_subjects > 0:
        print("Please insert your marks subject wise..! ")
        for i in range(number_of_subjects):
            temp = int(input("State your marks here .. "))
            subject_marks.append(temp)
    temp_lst = [name, fname, subject_marks, total_marks]
    lst_of_students_data.append(temp_lst)     
    n = n + 1

print(lst_of_students_data)


[
    ['Ali', 'Iqbal', [58, 80, 70], 300],
    ['Shahzeb', 'Khan', [100, 80, 60], 300],
    ['Sudais', 'Imran', [100, 30], 200]
]