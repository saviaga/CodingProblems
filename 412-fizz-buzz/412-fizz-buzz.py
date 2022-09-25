class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
       
        for num in range(1,n+1):
            this_ans = ""
            
            if num%3==0:
                this_ans += "Fizz"
            if num%5==0:
                this_ans +="Buzz"
            if not this_ans:
                this_ans =str(num)
            answer.append(this_ans)
        return answer
                
        