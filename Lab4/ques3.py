course_codes = input("Enter course codes: ").split()

course_names = input("Enter course names: ").split()


courses = [f"{code.strip()}: {name.strip()}" for code, name in zip(course_codes, course_names)]
print(course_codes)
print(course_names)
print("Course List: ", courses)
