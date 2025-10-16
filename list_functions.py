#len
nums = [1, 8, 2, 3, 8, 3, 4, 5]
n = len(nums)
print(len(nums))

#count function
print(nums.count(4))

#
numbers = list(range(11))
T = (1, 2, 3, 4, 5, 6)
L = list(T)
print(L)
print(T)
for n in numbers:
    print(n,end=" ")

for t in T:
    print(t,end=" ")

for l in L:
    print(l,end=" ")

#pop, remove and del
#remove removes with value
print()
print(nums)
nums.remove(4)
print(nums)
del nums[4]
print(nums)

nums.pop(0) # pop usually means remove the last element.
# pop is equivalent to del
print(nums)