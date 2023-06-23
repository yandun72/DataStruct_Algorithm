import numpy as np
class EditDistance:
    def __init__(self):
        self.dp = None
    def minDistance(self, word1: str, word2: str) -> int:
        length1,length2 = len(word1),len(word2)
        first_line = ['None']*2 + list(word2)
        first_col = ['None']*2 + list(word1)
        tmp = np.tile(first_line, length1 + 2).reshape(length1 + 2, length2 + 2)
        tmp[:,0] = first_col
        tmp[1:,1:] = 0
        dp = tmp
        
        for i in range(2,length2 + 2):
            dp[1][i] = str(i-1)
        for j in range(2,length1 + 2):
            dp[j][1] = str(j-1)

        for i in range(2,length1 + 2):
            for j in range(2,length2 + 2):
                if word1[i-2] == word2[j-2]:
                    dp[i][j] = str(dp[i-1][j-1])
                else:
                    dp[i][j] = str(min(int(dp[i-1][j-1]),int(dp[i-1][j]),int(dp[i][j-1])) + 1)
        
        self.dp = dp
        return int(dp[-1][-1])
    
    def similarity(self,word1,word2):
        distance = self.minDistance(word1,word2)
        length = max(len(word2),len(word1))
        return (length- distance) / float(length)

    def print_dptable(self):
        for row in self.dp:
            for item in row:
                print(f'{item}\t', end='')
            print()

if __name__ == "__main__":
    solution = EditDistance()
    word1,word2 = '重庆邮电大学','重庆大学'
    print(f'{word1}和{word2}的编辑距离',solution.minDistance(word1,word2))
    print(f'{word1}和{word2}的相似度',  solution.similarity(word1,word2))
    solution.print_dptable()