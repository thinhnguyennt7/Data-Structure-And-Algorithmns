# Hey, I Already Did That!
# ========================

# Commander Lambda uses an automated algorithm to assign minions randomly to tasks, in order to keep her minions on their toes. But you've noticed a flaw in the algorithm - it eventually loops back on itself, so that instead of assigning new minions as it iterates, it gets stuck in a cycle of values so that the same minions end up doing the same tasks over and over again. You think proving this to Commander Lambda will help you make a case for your next promotion. 

# You have worked out that the algorithm has the following process: 

# 1) Start with a random minion ID n, which is a nonnegative integer of length k in base b
# 2) Define x and y as integers of length k.  x has the digits of n in descending order, and y has the digits of n in ascending order
# 3) Define z = x - y.  Add leading zeros to z to maintain length k if necessary
# 4) Assign n = z to get the next minion ID, and go back to step 2

# For example, given minion ID n = 1211, k = 4, b = 10, then x = 2111, y = 1112 and z = 2111 - 1112 = 0999. Then the next minion ID will be n = 0999 and the algorithm iterates again: x = 9990, y = 0999 and z = 9990 - 0999 = 8991, and so on.

# Depending on the values of n, k (derived from n), and b, at some point the algorithm reaches a cycle, such as by reaching a constant value. For example, starting with n = 210022, k = 6, b = 3, the algorithm will reach the cycle of values [210111, 122221, 102212] and it will stay in this cycle no matter how many times it continues iterating. Starting with n = 1211, the routine will reach the integer 6174, and since 7641 - 1467 is 6174, it will stay as that value no matter how many times it iterates.

# Given a minion ID as a string n representing a nonnegative integer of length k in base b, where 2 <= k <= 9 and 2 <= b <= 10, write a function answer(n, b) which returns the length of the ending cycle of the algorithm above starting with n. For instance, in the example above, answer(210022, 3) would return 3, since iterating on 102212 would return to 210111 when done in base 3. If the algorithm reaches a constant, such as 0, then the length is 1.

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java

# Test cases
# ==========

# Inputs:
#     (string) n = "1211"
#     (int) b = 10
# Output:
#     (int) 1

# Inputs:
#     (string) n = "210022"
#     (int) b = 3
# Output:
#     (int) 3

def answer(n, b):
    ourArr = []
    flag = True
    count = 0
    k = len(str(n))
    counter = 100
    checked = []
    
    while counter > 0:
        arr = []
        if k == 0:
            return 0
        if int(n) == 0:
            return 1
        for i in range(k):
            arr.append(n[i])
        xArr = sorted(arr, reverse=True)
        yArr = sorted(arr)
        x = int(''.join(map(str, xArr)))
        y = int(''.join(map(str, yArr)))
        
        if b!= 10:
            z = decToB(bToDec(x, b) - bToDec(y, b), b)
        else:
            z = x - y

        array = []
        for j in range(len(str(z))):
            array.append(str(z)[j])
        if len(array) < (k):
            array.insert(0, '0')

        n = (''.join(map(str,array)))
        if n in ourArr and n not in checked:
            count += 1
            checked.append(n)

        ourArr.append(n)
        counter -= 1

    return(count)

def bToDec(n, b):
    n = str(n)
    getLen = len(n)
    newVal = 0
    for i in range(getLen):
        newVal = newVal + (int(n[i])*(b**(getLen-1)))
        getLen -= 1
    return newVal

def decToB(n, b):
    if n == 0:
        return 0
    d = []
    while n > 0:
        number = int(n % b)
        d.append(number)
        n = int(n / b)
    d = [str(i) for i in d]
    return "".join(d[::-1])

