# You are given an array of integers a, where each element a[i] represents the length of a ribbon.
# Your goal is to obtain k ribbons of the same length, by cutting the ribbons into as many pieces as you want.
# Your task is to calculate the maximum integer length L for which it is possible to obtain at least k ribbons of length L by cutting the given ones.

def solution(a, k):
    """
    a: list of ribbons
    k: min number of ribbons
    return L: max ribbon length
    
    note: if j <= k: solution(a, j) >= solution(a, k)
    general procedure: Each L maps to number of available split ribbons, r.
    Try L=1,2,3,4,...max(a) until r < k, then return L - 1. How do we optimize this?
    This L iteration is basically looking for the breaking point. Try using a binary-search 
    for this point
    """
    left, right = 1, max(a)
    while left < right - 1:
        L = (left + right)//2
        if ribbon_num(a, L) >= k: left = L
        else: right = L
    return left
        
        
def ribbon_num(a, L):
    return sum(map(lambda r_len: r_len // L, a))
    