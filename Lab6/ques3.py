def my_max(*args):
    if len(args) == 0:
        raise ValueError("No elements to compare.")

    max_value = args[0]
    
    for value in args[1:]:
        if value > max_value:
            max_value = value

    return max_value



list_input = [10, 20, 30, 40, 5]
max_in_list = my_max(*list_input)
print("Maximum value in list:", max_in_list)

set_input = {25, 50, 10, 5}
max_in_set = my_max(*set_input)
print("Maximum value in set:", max_in_set)

tuple_input = (1, 2, 3, 4, 5)
max_in_tuple = my_max(*tuple_input)
print("Maximum value in tuple:", max_in_tuple)
