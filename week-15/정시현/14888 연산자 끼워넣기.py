# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:18:07 2022

@author: KITCOOP
"""

n = int(input())
data = list(map(int, input().split()))

plus, minus, mul, div = map(int, input().split())

max_val = -1e9
min_val = 1e9

def dfs(i, arr):
    global plus, minus, mul, div, min_val, max_val
    if i==n:
        max_val = max(max_val, arr)
        min_val = min(min_val, arr)
    else:
        if plus > 0:
            plus -= 1
            dfs(i+1, arr + data[i])
            plus += 1
        if minus >0 :
            minus -= 1
            dfs(i+1, arr - data[i])
            minus += 1
        if mul > 0 :
            mul -= 1
            dfs(i+1, arr * data[i])
            mul += 1
        if div > 0 :
            div -= 1
            dfs(i+1, int(arr / data[i]))
            div += 1

dfs(1, data[0])

print(max_val)            
print(min_val)            
