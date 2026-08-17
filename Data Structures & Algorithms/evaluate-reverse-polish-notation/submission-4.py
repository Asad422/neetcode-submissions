class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # ["2","1","1","+","3","*"]
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }
        for i in range(len(tokens)):
            if tokens[i] not in operations:
                stack.append(int(tokens[i]))
            else:
                secondNumber = stack.pop()
                firstNumber = stack.pop()
                result = operations[tokens[i]](firstNumber, secondNumber)
                stack.append(result)
        return stack.pop()    




                

                


        