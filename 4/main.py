import collections

# puzzle input =  178416-676461
# part 1
doubles = [str(x) * 2 for x in range(10)]
ans = 0
for i in range(178416, 676461+1):
    if str(i) == ''.join(sorted(str(i))) and any (x in str(i) for x in doubles):
            ans +=1
print(ans)

# part 2, let's try something different
ans = 0
for i in range(178416, 676461+1):
    if str(i) == ''.join(sorted(str(i))) and 2 in collections.Counter(str(i)).values():
        ans +=1
print(ans)