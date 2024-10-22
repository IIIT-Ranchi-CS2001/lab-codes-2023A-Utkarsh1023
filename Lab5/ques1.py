import math

def euclidean_distance(point1, point2):
    distance = math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)
    return distance

point1 = (1.0, 2.0, 3.0)
point2 = (4.0, 5.0, 6.0)

distance = euclidean_distance(point1, point2)

print("Euclidean Distance is: ", distance)
