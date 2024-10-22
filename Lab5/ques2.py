points = [tuple(map(float, input(f"Enter the coordinates of point {i+1} (x, y): ").split())) for i in range(2)]

(x1, y1), (x2, y2) = points

if y1 != y2:  
    slope = (x1 - x2) / (y1 - y2)
    print(f"The equation of the line is: (x - {x1}) = {slope} * (y - {y1})")
else:
    print(f"The line is vertical, with the equation: x = {x1}")
