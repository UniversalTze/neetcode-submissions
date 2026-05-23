class PrefixTree:

    def __init__(self):
        # what does this need
        # needs nodes that can point to each other
        self.terminal = False # tells you end of the line or not
        self.arrNodes = {}

    def insert(self, word: str) -> None:
        node = self
        for i in range(len(word)):
            if word[i] not in node.arrNodes:
                # create a new prefix Tree
                create = PrefixTree()
                node.arrNodes[word[i]] = create
            node = node.arrNodes[word[i]]
                
            if i == len(word) - 1:
                node.terminal = True

    def search(self, word: str) -> bool:
        node = self
        for i in range(len(word)):
            if word[i] in node.arrNodes:
                node = node.arrNodes[word[i]]
                
                if i == len(word) - 1 and node.terminal == True:
                    return True
            else:
                break
        return False
        

    def startsWith(self, prefix: str) -> bool:
        node = self
        for i in range(len(prefix)):
            if prefix[i] in node.arrNodes:
                node = node.arrNodes[prefix[i]]
                
                if i == len(prefix) - 1:
                    return True
            else:
                break
        return False

        
        