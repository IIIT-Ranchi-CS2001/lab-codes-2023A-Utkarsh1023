# Question 4
name = input('Name: ')
roll = int(input('Roll Number: '))
marks = int(input('Marks: '))

if(marks >= 90):
    print('Grade Point: 10')
    print('Remarks: OUTSTANDING')
elif(90 > marks >= 80):
    print('Grade Point: 9')
    print('Remarks: VERY GOOD')
elif(80 > marks >= 70):
    print('Grade Point: 8')
    print('Remarks: GOOD')
elif(70 > marks >= 60):
    print('Grade Point: 7')
    print('Remarks: AVERAGE')
elif(60 > marks >= 50):
    print('Grade Point: 6')
    print('Remarks: PASS')
elif(marks < 50):
    print('Grade Point: 0')
    print('Remarks: FAIL')
