customer_names = [input(f"Enter name of customer {i+1}: ") for i in range(3)]
customer_ids = [input(f"Enter ID of customer {i+1}: ") for i in range(3)]
shopping_points = [int(input(f"Enter shopping points of customer {i+1}: ")) for i in range(3)]

customers_with_zip = list(zip(customer_names, customer_ids, shopping_points))

customers_without_zip = [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(3)]

print("List of customers using zip():", customers_with_zip)
print("List of customers without using zip():", customers_without_zip)
