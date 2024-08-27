#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        el=0
        i=1
        count=1
        for i in range(N):
            if(A[el]==A[i]):
                count=count+1
            else:
                count=count-1
            if count==0:
                el=i
                count=1
        count=0
        for i in A:
            if(A[el]==i): count=count+1
        if(count>N//2): return A[el]
        return -1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
