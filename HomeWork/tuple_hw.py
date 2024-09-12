students = ("Utkarsh", "Dinshu", "Nikki", "Mayank", "Anand")
marks = (67, 82, 91, 55, 78)

combined = tuple(zip(students, marks))
print(f"Combined Tuples are : {combined}")

sorted_combined = sorted(combined, key=lambda x: x[1])
print(f"Sorted Tuples are : {sorted_combined}")
highest = sorted_combined[-1] 
lowest = sorted_combined[0]    

print(f"Student with Highest mark: [{highest[0]}, Marks: {highest[1]}]")
print(f"Student with Lowest mark: [{lowest[0]}, Marks: {lowest[1]}]")

second_highest = sorted_combined[-2]
print(f"Student with Second-highest mark: [{second_highest[0]}, Marks: {second_highest[1]}]")

above_75 = [student for student, mark in combined if mark > 75]
count_above_75 = len(above_75)
print(f"Number of students who scored above 75 marks: {count_above_75} Student.")
