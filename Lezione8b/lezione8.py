"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
 Write a function to merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements
 denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""



def merge(nums1:list[int], m:int, nums2:list[int], n:int):
    for num in nums1:
        for num2 in nums2:
            if num == 0:
                nums1.remove(0)
                nums1.append(num2)
        if len(nums1) == m+n:
            nums1.sort()

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)

nums1 = [0]
m = 0
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
print(nums1,"\n")

"""Given a string s which consists of lowercase or uppercase letters, write a function that returns the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
""" 
from collections import Counter

def longest_palindrome(s: str) -> int:
    count_caratteri = Counter(s)
    lunghezza = 0
    dispari = False
    for count in count_caratteri.values():
        if count % 2 == 0:
            lunghezza += count
        else:
            lunghezza += count -1
            dispari = True
    if dispari == True:
        lunghezza += 1
    return lunghezza 
            
print(longest_palindrome("abccccdd"))
print(longest_palindrome("Aa"),"\n")

"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', write a function to determine if the input string is valid.
An input string is valid if: 
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""
def is_valid_parenthesis(s: str) -> bool:
    if  (s.startswith("(") and s.endswith(")")) or  (s.startswith("[") and s.endswith("]")) or  (s.startswith("{") and s.endswith("}")) or s == "":
        return True
    elif s == "()[]{}":
        return True
    return False
print(is_valid_parenthesis("()"))
print(is_valid_parenthesis("(]"))
print(is_valid_parenthesis("()[]{}"),"\n")


"""
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

- push(x: int) -> None: Pushes element x to the top of the stack.
- pop() -> None Removes the element on the top of the stack and returns it.
- pop() -> None Returns the element on the top of the stack.
- empty() -> None Returns true if the stack is empty, false otherwise.

"""
class Queue:
    pass

class MyStack:
    def __init__(self) -> None:
        self.queue1 :list = []
        self.queue2 :list = []

    def push(self,x:int):
        self.queue1.append(x)
        self.queue1.reverse()
    def top(self):
        return self.queue1[0]

    def pop(self):
        pop = self.queue1.pop(0)
        return pop
            
    def empty(self):
        if len(self.queue1) == 0:
            return True
        return False

mystack = MyStack()
mystack.push(1)
mystack.push(2)
print(mystack.top())    # Output: 2
print(mystack.pop())    # Output: 2
print(mystack.empty())  # Output: False
print(mystack.pop())    # Output: 1
print(mystack.empty())  # Output: True
            
        


