class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        mapping = defaultdict(list)
        for word in strs:
            frequency = [0]*26
            for char in word:
                frequency[ord(char) - ord('a')] += 1
            mapping[tuple(frequency)].append(word)
        
        answer = []
        for lists in mapping.values():
            answer.append(lists)
        return answer



        