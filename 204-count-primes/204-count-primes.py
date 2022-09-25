class Solution(object):
    
    def divisions(self,num):
        count=0
        for i in range(1,num+1):
            if num%i==0:
                count+=1
        return False if count>2 else True
        
        
    
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        counter = 0
        numbers = [False, False] + [True] * (n - 2)
        if n <= 2:
            return 0
        
        # Initialize numbers[0] and numbers[1] as False because 0 and 1 are not prime.
        # Initialze numbers[2] through numbers[n-1] as True because we assume each number
        # is prime until we find a prime number (p) that is a divisor of the number
        for e in range(2,  int(sqrt(n)) + 1):
            if numbers[e]==True:
            #Set all multiples of p to false false because they are not prime
                for multiple in range(e*e,n,e):
                    numbers[multiple] = False
        return sum(numbers)
                
            
            
        
        
        