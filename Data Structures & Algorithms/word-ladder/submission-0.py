class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordBook = set(wordList)
        if endWord not in wordBook:
            return 0
        queue = deque()
        queue.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)
        while queue:
            z = len(queue)
            for _ in range(z):
                word, dist = queue.popleft()
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word == endWord:
                            return dist + 1
                        if new_word in wordBook and new_word not in visited:
                            visited.add(new_word)
                            queue.append((new_word, dist + 1))
        return 0