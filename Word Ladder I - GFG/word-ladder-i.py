from collections import deque

class Solution:
    def wordLadderLength(self, startWord, targetWord, wordList):
        s = set(wordList)
        q = deque()
        q.append([startWord,1])
        if startWord in s:
            s.remove(startWord)
        while q:
            word, steps = q.pop()
            if word == targetWord:
                return steps
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in s:
                        s.remove(new_word)
                        q.appendleft([new_word, steps+1])
        return 0




#{ 
 # Driver Code Starts
# from collections import deque 
if __name__ == '__main__':
	T=int(input())
	for tt in range(T):
		n = int(input())
		wordList = []
		for i in range(n):
			wordList.append(input().strip())
		startWord = input().strip()
		targetWord = input().strip()
		obj = Solution()
		ans = obj.wordLadderLength(startWord, targetWord, wordList)
		print(ans)

# } Driver Code Ends