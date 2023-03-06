class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr_char_positions = {}
        cur_len, res = 0, 0

        for i, char in enumerate(s):
            past_i = substr_char_positions.get(char)
            if past_i is not None and past_i in range(i - cur_len, i): 
                cur_len = i - past_i
            else: cur_len += 1

            substr_char_positions[char] = i
            res = max(res, cur_len)


        return res