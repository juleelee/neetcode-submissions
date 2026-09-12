class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operation = {"+","-","*","/"}
        stack = []

        res = int(tokens[0])

        for token in tokens : 

            if token in operation : 
                right = stack.pop()
                left = stack.pop()

                if token == "+" : 
                    res = left + right

                elif token == "-" : 
                    res = left - right
                    
                elif token == "*" : 
                    res = left * right

                elif token == "/" : 
                    res = int(left / right)

                
                stack.append(res)
            

            else : 
                stack.append(int(token))

        return res






        
        