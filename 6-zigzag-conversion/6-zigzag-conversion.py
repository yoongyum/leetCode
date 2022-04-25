class Solution:
    def convert(self, s: str, numRows: int) -> str:           
        if numRows == 1 or numRows >= len(s):
            return s
        check = True;
        x,y = 0,0
        for i in range(len(s)):
            if check :
                if y ==  numRows-1 :
                    x+=1
                    y-=1
                    check = False
                else : y+=1
            else:
                if y == 0 :
                    y += 1
                    check = True
                else : 
                    x += 1
                    y -= 1
        
            
        matrix = [[0]*(x+1) for _ in range(numRows)]
        print(matrix)
        check = True;
        x,y = 0,0
        for i in range(len(s)):
            matrix[y][x] = s[i]
            if check :
                if y == numRows-1 :
                    x += 1
                    y -= 1
                    check = False
                else : y += 1
            else :
                if y == 0 :
                    y += 1
                    check = True
                else : 
                    x += 1
                    y -= 1
                    
        ans = []
        for l in matrix:
            for c in l:
                if c != 0:
                    ans.append(c)    
                    
        return ''.join(ans)