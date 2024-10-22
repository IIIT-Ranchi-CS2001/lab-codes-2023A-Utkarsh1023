customer_names = [input(f"Enter name of customer {i+1}: ") for i in range(3)]
customer_ids = [input(f"Enter ID of customer {i+1}: ") for i in range(3)]
shopping_points = [int(input(f"Enter shopping points of customer {i+1}: ")) for i in range(3)]

customers = list(zip(customer_names, customer_ids, shopping_points))

sorted_customers_with_sorted = sorted(customers, key=lambda x: x[2])

customers_without_sorted = customers[:]  
for i in range(len(customers_without_sorted)):
    for j in range(0, len(customers_without_sorted) - i - 1):
        if customers_without_sorted[j][2] > customers_without_sorted[j + 1][2]:
            customers_without_sorted[j], customers_without_sorted[j + 1] = customers_without_sorted[j + 1], customers_without_sorted[j]

print("Customers sorted using sorted():", sorted_customers_with_sorted)
print("Customers sorted without using sorted():", customers_without_sorted)
