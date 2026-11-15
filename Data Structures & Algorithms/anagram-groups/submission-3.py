class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for anagram in strs:
            check_anagram = {"a": 0, "b": 0, "c": 0, "d": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h":0, "i":0, "j":0, "k":0, "l":0,
        "o":0, "m":0, "p":0, "n":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}
            order = 0
            for char in anagram:
                check_anagram[char] +=1
            
            ana = ""
            for key, value in check_anagram.items():
                for i in range(value):
                    ana += key

            print(ana)
            if ana not in hashmap:
                    hashmap[ana] = []
            hashmap[ana].append(anagram)
        
        return list(hashmap.values())