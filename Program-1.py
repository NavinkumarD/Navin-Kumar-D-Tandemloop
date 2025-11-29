# Problem-1: Calculator using class

class Calculator:
    def add(self, a, b): return a + b
    def sub(self, a, b): return a - b
    def mul(self, a, b): return a * b
    def div(self, a, b):
        if b == 0:
            return "Division by zero not allowed"
        return a / b

a = float(input())
b = float(input())
op = input()

c = Calculator()

if op == "add":
    print(c.add(a, b))
elif op == "sub":
    print(c.sub(a, b))
elif op == "mul":
    print(c.mul(a, b))
elif op == "div":
    print(c.div(a, b))
else:
    print("Invalid operation")
