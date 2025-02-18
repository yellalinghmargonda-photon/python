class TireNode:
    def __init__(self):
        self.children={}
        self.EOW=False

class Tire:
    def __init__(self):
        self.root=TireNode()

    def insert(self, word):
        current=self.root
        for char in word:
            if char not in current.children:
                current.children[char]=TireNode()
            current=current.children[char]
        current.EOW=True
    def search(self,word):
        current=self.root
        for char in word:
            if char not in current.children:
                return  False
            current=current.children[char]
        return current.EOW
    def startsWith(self,word):
        current=self.root
        for char in word:
            if char  not in current.children:
                return False
            current=current.children[char]
        return True
trie = Tire()
trie.insert("apple")
print(trie.search("apple"))    # ✅ True
print(trie.search("app"))      # ❌ False (not a full word)
print(trie.startsWith("app"))  # ✅ True
trie.insert("app")
print(trie.search("app"))      # ✅ True (after inserting "app")
