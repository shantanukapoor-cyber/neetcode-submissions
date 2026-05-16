class TrieNode:

    def __init__(self):
        self.children = {}
        self.end_of_line = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.end_of_line = True
        

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.end_of_line
            letter = word[index]
            if letter == '.':
                for element in node.children.values():
                    if dfs(index + 1, element):
                        return True
                return False
            else:
                if letter not in node.children:
                    return False
                if dfs(index + 1, node.children[letter]):
                    return True
            return False
        return dfs(0, self.root)

        
