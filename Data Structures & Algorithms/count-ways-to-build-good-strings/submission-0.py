class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        

        # s[i] = the number of valid strings of length i

        # s[i] = (s[i - zero]) + (s[i - one])

        # s[0] = 1

        # answer: sum(s[low:high+1])

        s = [1] # s[0] = 1

        for i in range(1, high+1):

            good_strings = 0

            if i - zero >= 0:
                good_strings += s[i - zero]

            if i - one >= 0:
                good_strings += s[i - one]

            s.append(good_strings)

        count = sum(s[low:high+1])
        return count % 1000000007