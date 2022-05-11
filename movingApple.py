from unittest import result


class UserMainCode(object):
    def moveApple(cls,input1,input2):

        avg = sum(input2)//input1
        result = 0
        for i in range(input1):
            result+=abs(avg - input[i])
        return result//2    
    input1=input()
    input2=input()
    moveApple(input1,input2)