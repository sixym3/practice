#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 09:00:48 2022

@author: sixym3
"""

"""
Recursion - divde/decrease and conquer
reducing a problem to a simplier version of the same problem
A function calls it self again and again
A base case to prevent infinite recursions 

Iterative algorithems, Ex. for loops, while loops, and can be captured by 
state variables: values that tell us excatly which stage the algorithm is in

Disctionaries - also mutable

Mathmatical Induction
To prove a statement which is indexed on integer is true for all values of n:
    1) Prove that it is true when n is it's smallest value
    2) Prove that it is true for an arbitary value n, one can show it must be
    true for n+1
    
Induction example:
    0 + 1 + 2 + ... + n = ((n)(n+1))/2
    
1) Prove for smallest value of n = 0
    0 = ((0)(0+1))/2 = 0 True
2) Suppose some value of k is true for this statement, prove that k+1 also is
    true
    1 + 2 + ... + k = ((k)(k + 1))/2
    1 + 2 + ... + k + (k + 1) = ((k + 1)(k + 2))/2
    ((k)(k + 1))/2 + (k + 1) = ((k + 1)(k + 2))/2
    k^2 + 3k + 2 = k^2 + 3k + 2 True
    
Therefore, this expressions is true for all values of n > 0
"""

def multi_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

def multi(a, b):
    """
    Not solving for edge cases such as b = 0 or a negative value
    """
    if b == 1:
        return a
    else:
        return a + multi(a, b-1)
    
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def factorial_iter(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

def printmoves(n, fr, to):
    print("Move disc",n ,"from" , fr, "to", to)

def towers(n, fr, to, sp):
    if n == 1:
        printmoves(n, fr, to)
    else:
        towers(n - 1, fr, sp, to)
        printmoves(n, fr, to)
        towers(n - 1, sp, to, fr)
        
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fib_dic(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_dic(n - 1, d) + fib_dic(n - 2, d)
        d[n] = ans
        return ans
    
d = {1: 1, 2: 1}
    
def pali(inputstr):
    n = len(inputstr)
    if n <= 1:
        return True
    else:
        return pali(inputstr[1:-1]) and inputstr[0] == inputstr[-1]
    
def isPalidrome(s):
    
    def toChars(s):
        s = s.lower()   
        ans = ""
        for char in s:
            if char in "abcdefghijklmnopqrstuvwxyz":
                ans += char
        return ans
    
    def ispali(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and ispali(s[1:-1])
    
    return ispali(toChars(s))

def lyrics_to_dict(lyrics):
    result = {}
    for word in lyrics:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

def get_most_used_word(lyric_dict):
    values = lyric_dict.values()
    most_used = max(values)
    result = []
    for word in lyric_dict:
        if lyric_dict[word] == most_used:
            result.append(word)
    return result

song = """You're here where you should be
Snow is falling as the carolers sing
It just wasn't the same
Alone on Christmas day
Presents, what a beautiful sight
Don't mean a thing if you ain't holding me tight
You're all that I need
Underneath the tree
Tonight

I'm gonna hold you close
Make sure that you know
I was lost before you
Christmas was cold and grey
Another holiday alone to celebrate
But then, one day, everything changed
You're all I need
Underneath the tree
""".split(" ")

# print(get_most_used_word(lyrics_to_dict(song)))
    
    
#towers(4, "A", "B", "C")
"""
print(fib(6))
for i in range(10):
    print(fib(i))
"""
# print(isPalidrome("Are	we	not	drawn	onward,	we	few,	drawn	onward	to	new	era?"))
for i in range(1, 11):
    print(d)
    
    print(fib_dic(i, d))

#print(factorial_iter(3))