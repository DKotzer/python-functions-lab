##Python Function Lab

### Challenge 1

def sum_to(i):
    holder = 0
    for num in range(1,i+1):
        holder += int(num)
    print("sum to ",holder)
    return holder

sum_to(6)  # returns 21
sum_to(10) # returns 55



### Challenge 2

def largest(nums):
    biggest = 0;
    for num in nums:
        if num > biggest:
            biggest = num
    print("largest ",biggest)
    return biggest
    
largest([1, 2, 3, 4, 0])  # returns 4
largest([10, 4, 2, 231, 91, 54])  # returns 231



### Challenge 3


def occurances(one, two):
    print('occurances:',one.count(two))

occurances('fleep floop', 'e')   # returns 2
occurances('fleep floop', 'p')   # returns 2
occurances('fleep floop', 'ee')  # returns 1
occurances('fleep floop', 'fe')  # returns 0



### Challenge 4

def product(*args):
    sum = 1;
    for arg in args:
        sum = sum * arg
    print(f"sum: {sum}")
    return sum
    

product(-1, 4) # returns -4
product(2, 5, 5) # returns 50
product(4, 0.5, 5) # returns 10.0

