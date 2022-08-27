class TrieNode:
    def __init__(self):
        self.letters = collections.defaultdict(TrieNode)
        self.word = ""
        self.letter = ""
        self.isword = False
        self.parent = None
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        cur = self.root
        for l in word:
            prev = cur
            cur = cur.letters[l]
            cur.parent = prev
            cur.letter = l
        cur.word = word
        cur.isword = True
        
    def clean(self, node):
        node.isword = False

        if len(node.letters) > 0:
            return

        while node.parent:
            parent = node.parent
            del parent.letters[node.letter]
            
            if len(parent.letters) == 0 and not parent.isword:
                node = parent
            else:
                break

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        res = []
        
        for word in words:
            trie.add_word(word)
            
        def find_word(i, j, node):
            if node.isword:
                res.append(node.word)
                trie.clean(node)
            
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in node.letters:
                return
            
            letter = board[i][j]
            next_node = node.letters[letter]
            board[i][j] = '#'

            for di, dj in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                find_word(di, dj, next_node)
                
            board[i][j] = letter

            
        for i in range(len(board)):
            for j in range(len(board[0])):
                find_word(i, j, trie.root)
        
        return res