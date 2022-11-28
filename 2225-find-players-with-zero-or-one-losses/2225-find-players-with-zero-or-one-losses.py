class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d={}
        for i in matches:
            if i[1] in d:
                d[i[1]]+=1
            else:
                d[i[1]]=1
        a,b=set(),[]
        for i in matches:
            if i[0] not in d:
                a.add(i[0])
        for k,v in d.items():
            if v==1:
                b.append(k)
        a=list(a)
        a.sort()
        b.sort()
        answer=[a,b]
        return answer
        