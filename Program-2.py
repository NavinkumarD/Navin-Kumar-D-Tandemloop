# Problem-2: Print first 'a' odd numbers

a = int(input())

for i in range(a):
    print(2*i + 1, end=" " if i < a-1 else "")
