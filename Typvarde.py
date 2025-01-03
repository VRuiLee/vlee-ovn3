
def mode(vector):
    """Return the mode from a vector with whole numbers.
    If multiple values are equally common it will return the smallest of them."""

    # Time complexity O(n) since there is only constant functions within the for loops      

    vector_dict = {} # https://docs.python.org/3/library/stdtypes.html#dict
    mode_value = []

    if vector == [] or not isinstance(vector, list) or not all(isinstance(x, int) for x in vector): # Chatgpt for all()
        return None

    for i in range(len(vector)):
        if vector[i] in vector_dict:
            vector_dict[vector[i]] += 1
        else:
            vector_dict[vector[i]] = 1
    
    highest = max(vector_dict.values())

    for key, value in vector_dict.items():
        if value == highest:
            mode_value.append(key)

    return min(mode_value)


# Unit test
assert mode([1, 2, 3, 3, 2, 1]) == 1
assert mode([4, -5, 3]) == -5
assert mode([3]) == 3

# Test empty list
assert mode([]) == None

# Test with other datatypes
assert mode([1.5, 2, 3]) == None
assert mode(['a', 'b']) == None
assert mode(1) == None

print ("The test is done")
