from queue import Queue
class ACNode:
    def __init__(self,char=None,isEnd = False,word='',fail=None,prefix=''):
        """
        AC自动机节点类
        
        参数：
        - char: 当前节点表示的字符
        - isEnd: 标识当前节点是否为敏感词的结束节点
        - word: 敏感词
        - fail: 失败指针，指向当前节点的失败节点
        - prefix: 当前节点的前缀
        
        属性：
        - char: 当前节点表示的字符
        - isEnd: 标识当前节点是否为敏感词的结束节点
        - word: 敏感词
        - fail: 失败指针，指向当前节点的失败节点
        - post_prefix_word: 后缀前缀匹配的敏感词列表
        - prefix_count: 前缀计数，记录有多少个敏感词以当前节点为前缀
        - child: 子节点字典，存储当前节点的子节点
        - prefix: 当前节点的前缀
        """
        self.char  = char
        self.isEnd = isEnd
        self.word = word
        self.fail = fail
        self.fail_char = ''
        self.prefix_count = 0
        self.child = {}
        self.child_char = []
        self.prefix = prefix
        #self.postfix = []

class AhoCorasick:
    def __init__(self,word_list):
        self.word_list = word_list
        self.root = ACNode() 
        
    
    def _insert_Trie(self,word:str):
        
        cur = self.root
        for index,char in enumerate(word):
            #print(word,char)
            if char not in cur.child:
                node = ACNode(char = char,prefix=word[0:index])
                cur.child[char] = node
                cur.child_char.append(char)

            cur = cur.child[char]
            cur.prefix_count += 1
        cur.isEnd=True
        cur.word = word
        #cur.postfix = [word]

    def init_Trie(self):
        for word in self.word_list:
            
            self._insert_Trie(word)

    def build_fail(self):
        
        queue = Queue()
        queue.put(self.root)
        #BFS的方式去遍历
        while not queue.empty():
            cur = queue.get()
            parent = cur
            for child in cur.child.values():
                if child == None:
                    continue
                queue.put(child)
                char = child.char #取出子节点的字符
                print(cur.char,char)
                if parent == self.root: 
                    child.fail = self.root#root结点的子节点的fail都指向root
                    child.fail_char = 'root'
                else:
                    tmp = parent.fail
                    while tmp:
                        if char in tmp.child:#如果当前字符在父节点fail指针所指的结点的child里面
                            child.fail = tmp.child[char]
                            child.fail_char = tmp.child[char].char
                            # if tmp.child[char].isEnd and child.isEnd:
                            #     child.postfix.extend(tmp.child[char].postfix)
                            break#找到了fail所指，就要停止
                        else:
                            tmp = tmp.fail
                            if tmp == None:
                                child.fail = self.root
                                child.fail_char = 'root'
                                break



            
    def build(self):
        self.init_Trie() #先构建Trie树
        self.build_fail() #再构建fail指针
    
    def search(self, text:str):
        """
        在输入文本中搜索所有匹配的敏感词

        参数：
        - text: 输入文本

        返回：
        包含所有匹配结果的列表，每个结果是一个字典，包含敏感词和其在文本中的起始位置

        """
        results = []  # 存储匹配结果的列表
        cur_state = self.root  # 当前状态初始化为根节点

        # 遍历输入文本中的每个字符
        for i, char in enumerate(text):
            # 检查当前状态的子节点是否包含当前字符,直到退回到root结点
            while char not in cur_state.child and cur_state != self.root:
                # 若不包含，则沿着失败指针回溯
                cur_state = cur_state.fail

            print(char,cur_state.char,cur_state.isEnd,cur_state.word)
            
            if char in cur_state.child:
                # 若包含，更新当前状态为匹配子节点
                cur_state = cur_state.child[char]
            else:
                # 当前字符没有匹配的子节点，继续下一个字符的匹配
                continue
            
            #检查是否到达敏感词的结束节点
            if cur_state.isEnd:
                # 匹配到敏感词，记录匹配结果
                match_word = cur_state.word
                start_index = i - len(match_word) + 1
                result = {"word": match_word, "start_index": start_index}
                results.append(result)
                #再看一下它的fail指针的位置处是否也是单词的结束点
                if cur_state.fail.isEnd:
                    match_word = cur_state.fail.word
                    start_index = i - len(match_word) + 1
                    result = {"word": match_word, "start_index": start_index}
                    results.append(result)

        return results

    

data = ['she','shr','he','h','her','hers','his']
acTree = AhoCorasick(word_list=data)
acTree.build()
res = acTree.search('ahishersuhg')
print('该字符串中匹配到词库当中的词汇以及位置信息：')
for x in res:
    print(x)
'''
{'word': 'h', 'start_index': 1}
{'word': 'his', 'start_index': 1}
{'word': 'she', 'start_index': 3}
{'word': 'he', 'start_index': 4}
{'word': 'her', 'start_index': 4}
{'word': 'hers', 'start_index': 4}
{'word': 'h', 'start_index': 9}
'''


