import math as m
# Question 5
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

d = b*2 - 4*a*c
if(d == 0):
    print('Both roots are real and same.')
    R1 = R2 = -b/(2*a)
elif(d > 0):
    print('Two distinct real roots.')
    R1 = (-b + m.sqrt(d))/(2*a)
    R2 = (-b - m.sqrt(d))/(2*a)
elif(d < 0):
    print('Two complex roots.')
    R1 = -b/(2*a)
    R2 = m.sqrt(-d)/(2*a)

print(R1)
print(R2)