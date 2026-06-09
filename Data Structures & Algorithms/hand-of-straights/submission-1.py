class Solution:
    def isNStraightHand(self, hand, groupSize):
        n, k = len(hand), groupSize
        if n % k != 0:
            return False
        freq = {}
        for value in hand:
            freq[value] = freq.get(value, 0) + 1
        for start in sorted(freq):
            count = freq[start]
            if count == 0:
                continue
            for j in range(start, start + k):
                if freq.get(j, 0) < count:
                    return False
                freq[j] -= count
        return True