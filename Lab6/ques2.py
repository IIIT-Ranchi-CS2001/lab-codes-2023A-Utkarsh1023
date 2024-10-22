def my_sort(data_list, key=0):
    n = len(data_list)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if data_list[j][key] > data_list[j + 1][key]:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
    
    return data_list

def my_zip(customer_names, customer_ids, shopping_points, strct=True):
    if strct:
        if len(customer_names) == len(customer_ids) == len(shopping_points):
            return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]
        else:
            raise ValueError("All lists must be of equal length for strict zipping.")
    else:
        min_len = min(len(customer_names), len(customer_ids), len(shopping_points))
        return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(min_len)]

customer_names = ['Alice', 'Bob', 'Charlie']
customer_ids = ['ID001', 'ID003', 'ID002']
shopping_points = [150, 250, 200]

customers = my_zip(customer_names, customer_ids, shopping_points, strct=True)

sorted_by_name = my_sort(customers, key=0)
print("Sorted by Customer Name:", sorted_by_name)

sorted_by_id = my_sort(customers, key=1)
print("Sorted by Customer ID:", sorted_by_id)

sorted_by_points = my_sort(customers, key=2)
print("Sorted by Shopping Points:", sorted_by_points)
