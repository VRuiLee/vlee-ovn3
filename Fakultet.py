def factorial(n):
    """Calculate the factorial of n (factorial returns 1 * 2 * ... * n, where n >= 1. If n = 0 it returns 1) """

    if not isinstance(n,int) or isinstance(n, bool) or n < 0: 
        return False
    
    if n == 0 or n == 1:
        return 1
    
    return n*factorial(n-1)
    

# Unit test
assert factorial(2)==2
assert factorial(1)==1
assert factorial(0)==1
assert factorial(20)==2432902008176640000
assert factorial(-2)==False

assert factorial('a')==False
assert factorial(1.2)==False
assert factorial([1, 2])==False
assert factorial(None)==False
assert factorial(True)==False

print ("The test is done")


# Induction Proof
"""

The statement P(n) to prove can be stated: 
    The function call factorial(n) returns the value 1 * 2 * ... * n.

Base case:
    P(1) is true since the function returns 1 when n = 1

Induction step:
    We make the hypothesis “P(i) is true for all i < k”, i.e. the call factorial(i) returns 1 * 2 * … * i when i < k. 
    Using this hypothesis, we need to prove P(k).

    If k ≥ 2 the call factorial(k) returns k*factorial(k-1). But we know, according to the induction hypothesis, 
    that the call factorial(k-1) returns 1 * 2 * … * (k-1). Ergo, factorial(k) will return:
    k * (1 * 2 * ... * (k-1)) = 1 * 2 * ... * k.
    
    Using induction, we can conclude that the call factorial(n) returns the value 1 * 2 * … * n whenever n ≥ 1. Q.E.D.

https://yourbasic.org/algorithms/induction-recursive-functions/

"""