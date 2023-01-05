class Trie:

    class TrieNode:

        def __init__(self):     #The __init__ method of this class creates an empty dictionary.
            self.children = {}  #self.children is an empty dictionary that will store all the nodes in the trie.
            self.endOfTheWord = False  #self.endOfTheWord is set to False so that there are no words at the end of a string when using this trie as a word list or dictionary lookup function.

    def __init__(self):         #It creates a TrieNode object and assigns it to the self.root variable.
        self.root = self.TrieNode()

    def insert(self, word):  #It inserts a word into the trie.
        cur = self.root      #variable for value of the root.
        for c in word:       #It creates a new node in the root of the tree and then iterating through all of the letters in that word.
            if c not in cur.children:
                cur.children[c] = self.TrieNode()
            cur = cur.children[c]
        cur.endOfTheWord = True    #If there is no letter already in this node, it will create one for it and set its endOfTheWord property to true.            

    def search(self, word):        #It returns True if word is in the Trie, False otherwise.
        cur = self.root
        for c in word:             #It iterates through all of the root node's children, starting at the root, and checks to see if any of them are included in the current node's list of children.
            if c not in cur.children:
                return False       #not found, it returns False
            cur = cur.children[c]
        return cur.endOfTheWord

    def list_words(self,trie,str):  #It acts as Helper Function for get_all.
        my_list = []
        if trie.endOfTheWord:
            my_list.append(str)
        for i in trie.children:     #It iterates through all of the children of this node and appends them to my_list if they are not empty.
            ls = self.list_words( trie.children[i] , str+i )
            if len(ls)!=0:
                my_list +=ls
        return my_list    #It returns the list containing all the words in child node.

    def get_all(self):    #It returns a list of all the words in a trie in alphabetical order.
        return sorted(self.list_words(self.root,""))

    def list_pre(self,trie,pre,str,p):     #The list_pre() function takes in the previous string, the current word to be processed, and then returns a list of strings that will be appended onto my_list. It acts as a Helper function for begin_with.
        my_list = []                       #It sets up an empty list.
        if trie.endOfTheWord and p >= len(pre):
            my_list.append(str)
        
        for i in trie.children:      #It iterates through each child node in the trie and checks whether they are at the end of a word or past len(pre) before checking for their siblings        
            if p >= len(pre) or i == pre[p]:
                ls = self.list_pre( trie.children[i] , pre , str+i , p+1 )
                if len(ls)!=0:
                    my_list +=ls
        return my_list

    def begins_with(self, prefix):   #It returns a list of words that begin with prefix in alphabetical order
        return sorted(self.list_pre(self.root,prefix,"",0))   
