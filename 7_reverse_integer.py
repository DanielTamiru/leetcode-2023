class Solution:
    def reverse(self, x: int) -> int:
        """
        This problem is considerably harder in strongly typed languages with size caps on integers.
        Let's assume this isn't the case
        """
        if x == 0: return 0
        sign = -1 if x < 0 else 1
        lower_bound, upper_bound = - (2**31), (2**31) - 1
      
        res = sign * int(str(abs(x))[::-1])
        return res if lower_bound <= res and res <= upper_bound else 0