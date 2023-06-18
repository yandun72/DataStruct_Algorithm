from typing import *
class Node:
    def __init__(self,char = None):
        self.char = char
        self.child = {}
        self.isEnd = False
        self.string = ''
        self.prefix_count = 0

class Trie:

    def __init__(self):
        self.root = Node()


    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            node = Node(char = ch)
            if ch not in cur.child:
                cur.child[ch] = node
            cur = cur.child[ch]
            cur.prefix_count += 1
        cur.isEnd = True
        cur.string = word
        


    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch in cur.child:
                cur = cur.child[ch]
            else:
                return False
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch in cur.child:
                cur = cur.child[ch]
            else:
                return False
        return True
    
    def backTrack(self,root,res):
        if root.isEnd == True:
            res.append(root.string) 
        if len(root.child) == 0:
            return 
            
        for key in root.child.keys():
            self.backTrack(root.child[key],res)


    def getStartWith(self,prefix:str) -> List:
        cur = self.root
        for ch in prefix:
            if ch in cur.child:
                cur = cur.child[ch]
            else:
                return []
        #遍历该前缀结尾的word,要用回溯
        res = []
        tmp = cur
        self.backTrack(tmp,res)
        return res






if  __name__ == "__main__":
    tree = Trie()
    for string,f in zip([["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]],["insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"]):
        if f == "insert":
            tree.insert(string[0])
        elif f == "search":
            tree.search(string[0])
        elif f == "startsWith":
            tree.startsWith(string[0])
    #获得前缀开头的所有字符串
    res = tree.getStartWith("a")
    print(res)
    res = tree.getStartWith("ap")
    print(res)
    res = tree.getStartWith("b")
    print(res)
    '''
    ['app', 'apple', 'add']
    ['app', 'apple']
    ['beer']
    '''