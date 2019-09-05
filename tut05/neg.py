def remove_negs(num_list):
    """Remove negative numbers from the list num_list."""
    b = []
    for item in num_list:
        if item < 0:
            b.append(item)

    for item in num_list:
        for c in b:
            if item == c:
                num_list.remove(item)


