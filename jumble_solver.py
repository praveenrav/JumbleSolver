# Name: Praveen Ravishankar
# Jumble Solver

### Creating Trie Data Structure:
class TrieNode:

    def __init__(self, ch): # O(1)
        self.children = [None] * 26  # Creating an empty placeholder list for every letter in the alphabet
        self.char = ch  # Character stored in the Trie Node
        self.isWord = False  # Boolean to determine if the current node represents the end of a valid English word (in accordance with the given list)

class Trie:

    def __init__(self): # (Time AND Space: O(1))
        self.root = TrieNode("")  # Initializing Trie Node with an empty character
        self.wordsList = [] # Empty list to eventually store all English words that can be composed from the given input string

    def getCharIndex(self, ch_in): # (Time AND Space: O(1)) ; (Space: O(1))
        index = ord(ch_in) - ord('a')  # Assigning each lowercase letter an index between 0 and 25
        return index

    def insertWord(self, word_in): # (Time AND Space: O(len(word_in)) --> O(30) in worst-case scenario)
        node_cur = self.root
        word_in = word_in[:-1] # Removing the newline character at the end of each word

        for ch in word_in:
            ch_ind = self.getCharIndex(ch)

            if (node_cur.children[ch_ind] != None):
                node_cur = node_cur.children[ch_ind]
            else:
                node_newChild = TrieNode(ch)

                node_cur.children[ch_ind] = node_newChild
                node_cur = node_newChild

        node_cur.isWord = True  # Signifying that the last node represents the last character of the given word

    # Recursive Depth First Search (DFS) algorithm to print all word entries in the tree (was mainly used for debugging purposes):
    def printTrieWords(self, node, pref):

        # Determines if the function has been run for the first time (if yes, then select node to equal "1"):
        if(node == 1):
            node = self.root

        # If statement to determine if the current child is occupied by an actual node:
        if(node != None):
            pref_ch_next = pref + node.char # Updating the prefix with the character of the current node

            if(node.isWord):
                print(pref_ch_next)

            for child in node.children:
                self.printTrieWords(child, pref_ch_next) # Recursively calling the DFS method to find all words with the current prefix

    # Recursive Depth First Search (DFS) algorithm to search for valid word entries in the Trie
    # Time Complexity: O(x)
    # Space Complexity: O(n + p)
    def dfsWordSearch(self, node, pref, letters):

        pref = pref + node.char # Updating the prefix with the character of the current node

        # If statement to see if the current prefix is a valid word:
        if(node.isWord):
            # If statement to ensure that no duplicates are added to the words list:
            if(pref not in self.wordsList):
                self.wordsList.append(pref)

        # Looping through each of the characters in the remaining letters and performing the depth first search algorithm for each letter with the corresponding prefix
        for i in range(len(letters)):
            ch_cur = letters[i] # Retrieving each letter
            ch_cur_ind = self.getCharIndex(ch_cur) # Converting each letter to its corresponding index in the English alphabet (from 0 to 25)
            node_new = node.children[ch_cur_ind]

            # Removing the current character from the string for the next call of the DFS method:
            if(i == 0):
                let_rem = letters[1:]
            elif(i == (len(letters) - 1)):
                let_rem = letters[0:-1]
            else:
                let_rem = letters[0:i] + letters[(i+1):]

            # If statement to determine if the current child is occupied by an actual node:
            if(node_new is not None):
                self.dfsWordSearch(node_new, pref, let_rem) # Recursively calling the DFS method for the remaining string

    # Function to search for all valid English words using the characters in the given string and all its substrings
    def jumbleSolver(self, string):

        self.wordsList = []
        self.dfsWordSearch(self.root, "", string)

        return self.wordsList


### Main method:
str_in = input("Please type in a word: ") # Requesting user input for the given string on which to perform the jumble solver (Time AND Space: O(1))
print("Solving...")

## Creating Trie data structure:
wordTrie = Trie() # Creating a trie data structure that will eventually store all valid English words from the given text (Time AND Space: O(1))

# Loading list of valid words (Time: O(m); Space: O(m)):
with open('words_alpha.txt') as word_file:
    eng_words = word_file.readlines()

# Inserting each valid English word into the trie (Time: O(m); Space: O(m)):
for word in eng_words:
    wordTrie.insertWord(word)

# Performing the jumble solver on the given string (Time AND Space: Same as the dfsWordSearch() method):
words_list = wordTrie.jumbleSolver(str_in)

# Printing all valid words (Time Complexity: O(p); Space Complexity: O(1) assuming that the print function requires no memory):
for word in words_list:
    print(word)
