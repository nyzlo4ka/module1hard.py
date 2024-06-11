grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades_final = []
for i in grades:
    grades_final.append(sum(i) / len(i))
students_sort = sorted(students)
final_list = {}
for i in range(len(grades_final)):
    final_list[students_sort[i]] = grades_final[i]
print(final_list)





