# =====================================================================
#                     TRIE (PREFIX TREE) - REVISION NOTES
# =====================================================================
#
# WHAT IS A TRIE?
#   - A tree for storing STRINGS, where each edge is one character.
#   - The path from the root to a node spells a PREFIX.
#   - Each node has:
#       children     : map of char -> child node (or an array of 26)
#       is_end_of_word: True if a complete word ends at this node
#   - The root is empty (represents "").
#
#   Words: "car", "cat", "cart", "dog"
#
#               (root)
#              /      \
#             c        d
#             |        |
#             a        o
#            / \       |
#           r*  t*     g*
#           |
#           t*                 (* = end of a word)
#
# TIME COMPLEXITY (L = length of the word / prefix)
#   +--------------------------+--------+
#   | Operation                | Time   |
#   +--------------------------+--------+
#   | Insert                   | O(L)   |
#   | Search whole word        | O(L)   |
#   | starts_with(prefix)      | O(L)   |
#   | Delete                   | O(L)   |
#   | All words with a prefix  | O(L + number of chars in results) |
#   +--------------------------+--------+
#   - Time does NOT depend on how many words are stored!
#   Space: O(total characters of all words * alphabet size) in the worst
#   case. Shared prefixes are stored only once, which saves space.
#
# CHILDREN STORAGE
#   - Array of size 26: fast, but wastes memory for sparse nodes.
#   - Dict / hash map : memory efficient, any character set (used below).
#
# TRIE vs HASH SET
#   - Hash set: O(L) lookups too, but cannot answer PREFIX queries
#     efficiently.
#   - Trie: prefix search, autocomplete, sorted (lexicographic) listing.
#
# APPLICATIONS
#   - Autocomplete / search suggestions, spell checkers.
#   - IP routing (longest prefix match), T9 phone keyboards.
#   - Word games (Boggle, word search II).
#
# COMMON INTERVIEW PATTERNS
#   - Implement Trie (insert, search, startsWith).
#   - Word search II (trie + DFS on a grid).
#   - Longest common prefix of a list of words.
#   - Replace words with their shortest root, search suggestions system.
#   - Design add & search words with '.' wildcards.
#   - Maximum XOR of two numbers (binary trie of bits).
#   - Count distinct substrings (trie of all suffixes).
# =====================================================================


class TrieNode:
    def __init__(self):
        self.children = {}        # char -> TrieNode
        self.is_end = False
        self.prefix_count = 0     # how many words pass through this node


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.word_count = 0

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
            node.prefix_count += 1
        if not node.is_end:
            node.is_end = True
            self.word_count += 1
        else:
            # word already existed: undo the prefix counts we just added
            node = self.root
            for ch in word:
                node = node.children[ch]
                node.prefix_count -= 1

    def _find(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def search(self, word):
        node = self._find(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        return self._find(prefix) is not None

    def count_prefix(self, prefix):
        if prefix == "":
            return self.word_count
        node = self._find(prefix)
        return node.prefix_count if node else 0

    def words_with_prefix(self, prefix):
        """Autocomplete: all words starting with prefix, in sorted order."""
        node = self._find(prefix)
        result = []

        def _dfs(n, path):
            if n.is_end:
                result.append(path)
            for ch in sorted(n.children):
                _dfs(n.children[ch], path + ch)

        if node:
            _dfs(node, prefix)
        return result

    def delete(self, word):
        """Remove a word and prune nodes that are no longer needed."""
        if not self.search(word):
            return False

        def _delete(node, i):
            if i == len(word):
                node.is_end = False
                return not node.children  # prune if no children
            ch = word[i]
            child = node.children[ch]
            child.prefix_count -= 1
            if _delete(child, i + 1):
                del node.children[ch]
            return not node.is_end and not node.children

        _delete(self.root, 0)
        self.word_count -= 1
        return True

    def longest_common_prefix(self):
        node, prefix = self.root, ""
        while len(node.children) == 1 and not node.is_end:
            ch, node = next(iter(node.children.items()))
            prefix += ch
        return prefix

    def __len__(self):
        return self.word_count

    def __contains__(self, word):
        return self.search(word)


class WildcardTrie(Trie):
    """search() supports '.' which matches any single character."""

    def search(self, word):
        def _dfs(node, i):
            if i == len(word):
                return node.is_end
            ch = word[i]
            if ch == ".":
                return any(_dfs(child, i + 1) for child in node.children.values())
            return ch in node.children and _dfs(node.children[ch], i + 1)

        return _dfs(self.root, 0)


def replace_words(roots, sentence):
    """Replace each word with the shortest root that is its prefix."""
    trie = Trie()
    for r in roots:
        trie.insert(r)

    def shortest_root(word):
        node, prefix = trie.root, ""
        for ch in word:
            if ch not in node.children:
                return word
            node = node.children[ch]
            prefix += ch
            if node.is_end:
                return prefix
        return word

    return " ".join(shortest_root(w) for w in sentence.split())


if __name__ == "__main__":
    t = Trie()
    for w in ["car", "cat", "cart", "care", "dog", "dot", "do"]:
        t.insert(w)

    print("----- Trie -----")
    print("words:", len(t))
    print("search('car'):", t.search("car"), "| search('ca'):", t.search("ca"))
    print("starts_with('ca'):", t.starts_with("ca"), "| starts_with('z'):", t.starts_with("z"))
    print("count_prefix('car'):", t.count_prefix("car"), "| count_prefix('do'):", t.count_prefix("do"))
    print("autocomplete('ca'):", t.words_with_prefix("ca"))
    print("autocomplete('do'):", t.words_with_prefix("do"))

    print("\n----- Delete -----")
    t.delete("car")
    print("after delete('car'): search('car') =", t.search("car"),
          "| search('cart') =", t.search("cart"), "| words:", len(t))

    print("\n----- Longest common prefix -----")
    lcp = Trie()
    for w in ["flower", "flow", "flight"]:
        lcp.insert(w)
    print("['flower','flow','flight'] ->", repr(lcp.longest_common_prefix()))

    print("\n----- Wildcard search -----")
    wt = WildcardTrie()
    for w in ["bad", "dad", "mad"]:
        wt.insert(w)
    print("search('.ad'):", wt.search(".ad"), "| search('b..'):", wt.search("b.."),
          "| search('pad'):", wt.search("pad"))

    print("\n----- Replace words -----")
    print(replace_words(["cat", "bat", "rat"], "the cattle was rattled by the battery"))
