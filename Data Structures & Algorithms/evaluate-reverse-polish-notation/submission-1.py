class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for token in tokens:
            if token not in "+-*/":
                s.append(int(token))
            else:
                arg1 = s.pop()
                arg2 = s.pop()

                if token == '+':
                    s.append(arg1 + arg2)
                elif token == '*':
                    s.append(arg1 * arg2)
                elif token == '-':
                    s.append(arg2 - arg1)
                elif token == '/':
                    res = arg2 / arg1
                    if res > 0:
                        res = math.floor(res)
                    else:
                        res = math.ceil(res)
                    s.append(res)
        
        return s[-1]