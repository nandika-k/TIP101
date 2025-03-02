def swap_ends(my_str):
    start = my_str[0]
    end = my_str[-1]

    my_str = end + my_str[1:-1] + start
    return my_str

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)