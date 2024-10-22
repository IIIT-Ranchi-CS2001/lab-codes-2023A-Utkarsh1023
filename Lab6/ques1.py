def my_zip(customer_names, customer_ids, shopping_points, strct=True):
    if strct:
        if len(customer_names) == len(customer_ids) == len(shopping_points):
            return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]
        else:
            raise ValueError("All lists must be of equal length for strict zipping.")
    
    else:
        min_len = min(len(customer_names), len(customer_ids), len(shopping_points))
        return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(min_len)]


customer_names = ['Utkarsh', 'Nikki', 'Prachi']
customer_ids = ['ID001', 'ID002', 'ID003']
shopping_points = [150, 200, 250]

try:
    result_strict = my_zip(customer_names, customer_ids, shopping_points, strct=True)
    print("Strict zipping:", result_strict)
except ValueError as e:
    print(e)

result_non_strict = my_zip(customer_names, customer_ids, shopping_points[:3], strct=False)  
print("Non-strict zipping:", result_non_strict)
