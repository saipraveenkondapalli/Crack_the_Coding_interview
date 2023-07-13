class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.endOfWord = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def _getNode(self):
        return TrieNode()

    def _charToindex(self, char):
        return ord(char) - ord('a')

    def insert(self, key):
        cur = self.root
        length = len(key)
        for x in range(length):
            index = self._charToindex(key[x])
            if not cur.children[index]:
                cur.children[index] = self._getNode()
            cur = cur.children[index]
        cur.endOfWord = True

    def search(self, key):
        cur = self.root
        length = len(key)
        for x in range(length):
            index = self._charToindex(key[x])
            if not cur.children[index]:
                return False
            cur = cur.children[index]

        return cur and cur.endOfWord



if __name__ == "__main__":
    keys = ["the", "a", "there", "answer", "any", "by", "bye", "their"]
    output = ["Not present in trie",
              "Present in trie"]

    # Trie object 
    t = Trie()

    # Construct trie 
    for key in keys:
        t.insert(key)
    print(t.root.children)
    # Search for different keys 
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))

    # Output:
    # the ---- Present in trie
    # these ---- Not present in trie
    # their ---- Present in trie
    # thaw ---- Not present in trie
