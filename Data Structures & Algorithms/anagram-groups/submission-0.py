class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #creates you a key with deafult list value if no same key present in the dictionary 
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')]+=1
            res[tuple(count)].append(s)
        return list(res.values())


        