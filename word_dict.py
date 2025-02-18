class WordDictionary:

    def __init__(self):
        self.size = 3
        self.ptr = 0
        self.word_list = [None] * self.size

    def isFull(self):
        return self.ptr == self.size

    def resize(self):
        # Double the size of the stack and move all items
        new_size = self.size * 2
        new_list = [None] * new_size
        for i in range(self.ptr):
            new_list[i] = self.word_list[i]
        self.word_list = new_list
        self.size = new_size

    def addWord(self, word: str) -> None:
        if self.isFull():
            self.resize()
        self.word_list[self.ptr] = word
        self.ptr += 1
        self.words_by_length = defaultdict(list)

    def search(self, word: str) -> bool:
        for i in range(self.ptr):

            if len(word)!=len(self.word_list[i]):
                continue
            ser_word = ''
            ex_word = ''
            for j, s in enumerate(word):
                if s=='.':
                    continue
                ser_word=ser_word+s
                ex_word=ex_word+self.word_list[i][j]
            if ser_word==ex_word and len(ser_word>0):
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
wordDictionary =WordDictionary();
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
wordDictionary.addWord("dog")
print(wordDictionary.search("pad"))
print(wordDictionary.search("bad"))
print(wordDictionary.search(".ad"))
print(wordDictionary.search("b.."))