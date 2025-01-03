
def Partition(v):
    """Partition reorders the elements of vector called v so that:
    all elements in v[:low] are negative,
    all elements in v[low:mid] are non negative, including 0.
    Returns the reorded v"""

    # Time complexity O(n) because the while loop has to go through the whole list. All the others are constant
   
    if v == [] or not isinstance(v, list) or not all(isinstance(x, int) for x in v): 
        return None

    low = 0
    p = 0

    for mid in range(len(v)):
        """
        Invariant:
		- v[:low] < 0
		- v[low:mid] >= 0
		- v[mid:] are unknown
		
	
	            < p       >= p        unknown     
		    -----------------------------------
		v: |          |          |a            |           
		    -----------------------------------
		              ^          ^             
		             low        mid           

        """
        a = v[mid]

        if a < p:
            v[mid] = v[low]
            v[low] = a
            low += 1
        
        # Do nothing if the element is positive

    return v

# Unit test
assert Partition([2, -2]) == [-2, 2]
assert Partition([1, 2, -2, 3, -1, 0, 3, -3]) == [-2, -1, -3, 3, 2, 0, 3, 1]

# Test empty list
assert Partition([]) == None

# Test correct list
assert Partition([-2, -3, -1, 4, 0, 1, 3]) == [-2, -3, -1, 4, 0, 1, 3]

# Test with other datatypes
assert Partition([1.5, 2, 3]) == None
assert Partition(['a', 'b']) == None
assert Partition(1) == None

print ("The test is done")



# https://yourbasic.org/algorithms/loop-invariants-explained/