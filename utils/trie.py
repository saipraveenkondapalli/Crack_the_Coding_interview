class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.end_of_word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def _get_node(self):
        return TrieNode()

    def _char_to_index(self, char):
        return ord(char) - ord('a')

    def insert(self, key):
        cur = self.root
        length = len(key)
        for x in range(length):
            index = self._char_to_index(key[x])
            if not cur.children[index]:
                cur.children[index] = self._get_node()
            cur = cur.children[index]
        cur.end_of_word = True

    def search(self, key):
        cur = self.root
        length = len(key)
        for x in range(length):
            index = self._char_to_index(key[x])
            if not cur.children[index]:
                return False
            cur = cur.children[index]

        return cur and cur.end_of_word


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
