class Tri:
    def __init__(self):
        self.children={}
        self.end=False
class WordInsertSearch:
    def __init__(self):
        self.root= Tri()

    def insert(self, word):
        current=self.root
        for c in word:
            if c not in current.children:
                current.children[c]=Tri()
            current=current.children[c]
        current.end=True

    def dfs(self, node, index, word):
        if index==len(word):
            return node.end
        char =word[index]
        if char=='.':
            for child in node.children.values():
                if self.dfs(child,index+1, word):
                    return True
            return False
        if char in node.children:
            return self.dfs(node.children[char],index+1, word)
        return False

    def search(self, word):
            current=self.root
            return self.dfs(current,0,word)
    def simpelsearch(self,word):
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            current=current.children[c]
        return current.end

trie = WordInsertSearch()
trie.insert("apple")
trie.insert("app")
trie.insert("bat")

print(trie.search("app"))   # True
print(trie.search("appl."))  # True
print(trie.search("bat"))    # True
print(trie.search_wild_card("b.."))    # True
print(trie.search("applz"))  # False
print(trie.search("apple"))  # False
