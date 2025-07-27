class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ', '')  # remove spaces
        stack = []
        num = 0
        op = '+'  # Start with '+' to push the first number

        for i in range(len(s)):
            char = s[i]

            if char.isdigit():
                num = num * 10 + int(char)

            # If char is an operator or last character
            if not char.isdigit() or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    prev = stack.pop()
                    # Truncate toward zero
                    stack.append(int(prev / float(num)))

                op = char
                num = 0

        return sum(stack)
        