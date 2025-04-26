class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        '''
        Understand:
        We're gonna be incrementing the value by 1 in total
        if the digit is 9 then we'll need to change it to 0 and look for the next non 9 digit
        return a list of the array of digits
        edge case:
        all digits are 9
        '''
        #create a new list
        outputs = [1]
        #if the last digit is 9:
        if digits[len(digits)-1] == 9:
            #iterate from the end of the list to the next non 9 digit
            for index in range(len(digits)-1,-2, -1):
                print(index)
                #if index = -1:
                if index == -1:
                    #list concatenate
                    outputs += digits
                #change the digits to 0
                elif digits[index] == 9:
                    digits[index] = 0
                #else:
                else:
                    digits[index] +=1
                    return digits
                    #incremement
                    #return old list
            #return new list
            return outputs
        #else:
        else:
            digits[len(digits)-1] +=1
            #increment by 1
        #return old list
        return digits
dsigits = [1, 2, 3, 4]
fix = [9, 9, 9]
solution = Solution()
problem1 = solution.plusOne(dsigits)
problem2 = solution.plusOne(fix)
print(problem1)
print(problem2)