from typing import List
from EditDistance import EditDistance
m = EditDistance()

class Node:
    def __init__(self,word:str):
        self.word = word
        self.children = {}

class BKTree:
    def __init__(self,word_list:List):
        self.word_list = word_list
        self.root = None


    def build(self):
        if len(self.word_list) == 0:
            return
        self.root = Node(self.word_list[0]) #创建根节点
        for word in self.word_list[1:]:
            self.insert(self.root,word)

    def insert(self,root,word):
        if root == None:
            return Node(word) #递归的出口
        distance = m.minDistance(root.word,word)

        if distance == 0:
            return
        if distance in root.children.keys(): #这个距离已经在当前结点里面了，就递归下去
            root.children[distance] = self.insert(root.children[distance],word)
        else:
            root.children[distance] = Node(word)
        
        return root
    
    def search(self,word,threshold_distance=3,threshold_similartiy = 0.75,topn = 10):
        result = []
        self._search(self.root,word,result,threshold_distance,threshold_similartiy)
        result.sort()
        result.reverse()
        return result[0:topn]

    def _search(self,root,word,result,threshold_distance,threshold_similartiy):
        if root == None:#递归出口
            return 
        
        distance = m.minDistance(root.word,word)
        max_length = max(len(root.word),len(word))
        similarity = (max_length - distance) / float(max_length)

        if distance <= threshold_distance and similarity >= threshold_similartiy:
            result.append((similarity,root.word))
        
        start = max(distance - threshold_distance,0)
        end   = distance + threshold_distance
        for dis in range(start,end + 1):
            if dis in root.children:
                self._search(root.children[dis],word,result,threshold_distance,threshold_similartiy)


        
import random
import string



if __name__ == "__main__":
    

    random_strings = ["apple", "appla", "appl", "aple", "banana", "banan", "bananna", "cat", "caat", "cot", "dog", "dogg", "elephant", "elepant", "elephantt", "fish", "fsh", "grape", "grepe", "hat", "hhat", "icre cream", "ice creem", "ice creamm", "jelly", "jely", "jelyy", "kangaroo", "kanggaroo", "kangarooo", "lemon", "leemn", "mango", "manngo", "nut", "nutt", "orange", "orrange", "pineapple", "pineapplle", "quail", "quall", "rabbit", "rabbitt", "strawberry", "strawbery", "strawberryy", "tiger", "tigerr", "umbrella", "umbrela", "violet", "violett", "watermelon", "watermellon", "xylophone", "xylophne", "yak", "yaak", "zebra", "zebr", "ant", "atn", "bird", "birdd", "carrot", "carot", "duck", "duc", "egg", "frogs", "frgo", "giraffe", "girrafe", "horse", "horsee", "insect", "inset", "jacket", "jakcet", "koala", "koalla", "lion", "lino", "monkey", "monnkey", "nose", "nsoe", "octopus", "octopuss", "peach", "pech", "quack", "quak", "raccoon", "raco", "snake", "snak", "tulip", "tuliip", "unicorn", "unicorrn", "vase", "vasse", "whale", "whall", "xylophone", "xylophoone", "yoyo", "yeeyo", "zeppelin", "zeplein", "antelope", "anteloppe", "buffalo", "buffaloo", "camel", "caamel", "dolphin", "dolpfin", "elephant", "elepahnt", "flamingo", "flamingoo", "gazelle", "gazell", "hippopotamus", "hipopotamus", "iguana", "iguan", "jaguar", "jagur", "kangaroo", "kangaroooo", "lemur", "lemurr", "mongoose", "mongoos", "narwhal", "narwhall", "opossum", "opossom", "peacock", "pecock", "quokka", "qokka", "rhinoceros", "rhinoceross", "squirrel", "squirrrel", "tortoise", "tortose", "umbrella", "umbrela", "vulture", "vulure", "walrus", "walruss", "x-ray fish", "x-rayfish", "yak", "yaak", "zebra", "zbra"]
    tree = BKTree(random_strings)
    tree.build()
    query = 'apple'
    topn = 5
    threshold_distance=3
    threshold_similartiy = 0.75
    result = tree.search(query,threshold_distance,threshold_similartiy,topn)
    print(f'query:{query},threshold_distance:{threshold_distance},threshold_similartiy:{threshold_similartiy},topn:{topn},result:{result}')

'''
query:apple,threshold_distance:3,threshold_similartiy:0.75,topn:5,result:[(1.0, 'apple'), (0.8, 'appla'), (0.8, 'appl'), (0.8, 'aple')]
'''      
        