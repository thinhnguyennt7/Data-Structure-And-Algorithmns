'''
Problem: Suppose you are at a party with n people (labeled from 0 to n - 1) and among them,

there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her
but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed
to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find
out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int
findCelebrity(n), your function should minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is
a celebrity in the party.
'''

KNOWS = [
            [False, True, True , False],
            [True , False, True , False],
            [False, False, False, False],
            [False, False, True , True ],
        ]

def knows(a, b):
    return KNOWS[a][b]

def find_celeb(n):
    '''ACCEPTABLE- Stack solution (If an interviewee comes up with this solution, 
    let them code it up and push them to the most optimal solution, down below, if time permits!)
    In this solution, we initialize a stack
    with the people as entries.
    We then pop two people off the stack (left and right)
    and check whether left knows right. If left does know right,
    left is not a celebrity, so we pop a person off the stack
    and set them to right. If left does not know right, we know
    right is not a celebrity, so we set right to the next
    person on the stack. This continues until the stack is empty.
    The final person on the stack is a potential candidate, so
    we check that person. We then finally run the full comparison
    check for the final candidate.
    >>> find_celeb(4)
    2
    >>> find_celeb(3)
    2
    >>> find_celeb(2)
    '''
    stack = list(range(n))
    left, right = stack.pop(), stack.pop()
    candidate = right
    while len(stack) > 0:
        if knows(left, right):
            candidate = left = stack.pop()
        else:
            candidate = right = stack.pop()
    if candidate == right and knows(candidate, left):
        candidate = left
    if candidate == left and knows(candidate, right):
        candidate = right

    for idx in range(n):
        if idx == candidate:
            continue
        if knows(candidate, idx):
            return -1
        if not knows(idx, candidate):
            return -1
    return candidate

def find_celeb2(n):
    '''MOST OPTIMAL- Pointer solution
    In this solution, we compare pairs of people
    to see if one knows the other. We maintain two pointers (left and right) to people, initialized
    to the beginning and end of the list. We know if left knows right, then left cannot
    be the celebrity, so we increment left. We also know if left does not know right,
    then right cannot be the celebrity, so we decrement right. This continues
    until the pointers are the same. This is the only candidate
    celebrity, so we perform a final check to see if this candidate
    knows no one and everyone knows the candidate (since we don't do all
    checks while searching for the candidate).
    >>> find_celeb(4)
    2
    >>> find_celeb(3)
    2
    >>> find_celeb(2)
    '''
    left_idx, right_idx = 0, n - 1

    while left_idx < right_idx:
        if knows(left_idx, right_idx):
            left_idx += 1
        else:
            right_idx -= 1
    for idx in range(n):
        if idx == left_idx:
            continue
        if knows(left_idx, idx):
            return -1
        if not knows(idx, left_idx):
            return -1
    return left_idx