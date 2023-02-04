class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Using only repeated subtraction is inefficient. Instead, use bitwise operators 
        Not and Shift left.

        Let x' denote the maximum x where the following inequality holds: divisor * 2^x < dividend
        2^x' is then a value close to and less than the quotient. So, we can subtract divisor * 2^x'
        from the dividend (dividend -= divisor * 2^x') and restart the process of finding a x'
        (over and over) until the dividend is no longer large enough to be divisble by the divisor.

        'exp' for exponent in the code below is the x described in the process above.
        """
        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        
        if dividend < divisor: return 0
        if dividend == divisor: return -1 if negative else 1

        abs_quotient = 0
        while dividend >= divisor: 
            exp = 0 
            while dividend >= divisor << exp: exp += 1
            
            dividend -= divisor << (exp - 1)
            abs_quotient += 1 << (exp - 1)
       
        quotient = ~abs_quotient + 1 if negative else abs_quotient
        
        return min(max(quotient, -2147483648), 2147483647)

        