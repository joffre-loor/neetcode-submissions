class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x","y","z"]

        words=set()
        for w in wordList:
            words.add(w)
        
        visited = set()
        q = deque()
        q.append(beginWord)

        res = 0
        while q:
            res+=1
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return res
                for i in range(len(curr)):
                    for c in chars:
                        check = curr[:i] + c + curr[i+1:]
                        if check not in words:
                            continue
                        q.append(check)  
                        words.remove(check)

        return 0