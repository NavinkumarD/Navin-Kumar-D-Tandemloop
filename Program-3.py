# Problem-3: Special odd number pattern

a = int(input())

n = a if a % 2 == 1 else a - 1

for i in range(n):
    print(2*i + 1, end=" " if i < n-1 else "")
