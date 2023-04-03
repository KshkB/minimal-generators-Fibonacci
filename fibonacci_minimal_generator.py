"""
Given a number N, N > 0, what is the minimal pair of non-negative integers 
generating a Fibonacci sequence containing N?
"""

class Fibonaci:

    def __init__(self, initial, next):
        self.initial = initial
        self.next = next
    
    def generate_until(self, tgt):
        """
        Generate Fibonacci sequence until tgt is saturated
        """
        curr_stack = [self.initial, self.next]
        curr_val = sum(curr_stack)
        while(curr_val < tgt):
            curr_stack.pop(0)
            curr_stack += [curr_val]
            curr_val = sum(curr_stack)
        
        if curr_val == tgt:
            return True 
        return False
        
def minimal_generators(tgt):
    generators = []
    for j in range(1, tgt+1):
        for i in range(j+1):
            fib = Fibonaci(i, j)
            if fib.generate_until(tgt) == True:
                generators += [(i, j)]
    return generators

def order_by(arr):
    """
    Order tuples by Euclidean distance
    """
    Euclidean_distances = []
    for tple in arr:
        dist = (tple[0]**2 + tple[-1]**2)**(1/2)
        Euclidean_distances += [dist]
    tuple_dist_dict = dict(zip(arr, Euclidean_distances))
    return min(tuple_dist_dict, key=tuple_dist_dict.get)
