class Solution:
    def subArraySum(self,arr, n, s):
       
        end=0
        temp=0
        i=0
        sum=0
        while(i<n):
            sum=sum+arr[i]
            end=i
            while(sum>s and temp<end):
                sum=sum-arr[temp]
                temp=temp+1
            if(sum==s):
                return [temp+1,end+1]
            i=i+1
        return [-1]
            
        
