# Problem-4: Count multiples from 1 to 9

nums = list(map(int, input().split(",")))

result = {}

for i in range(1, 10):
    count = 0
    for x in nums:
        if x % i == 0:
            count += 1
    result[i] = count

print(result)
