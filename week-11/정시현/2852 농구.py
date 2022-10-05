#백준 2852 NBA 농구

import re

n = int(input())

goal = []
for i in range(n):
    goal.append(re.split(' |:',input()))

print(goal)
count1 = 0
count2 = 0
time = (goal[0][1]*60)+goal[0][2]
time1 = 0
time2 = 0
for i in range(n):
    if(goal[i][0] == 1):
        count1 +=1
    else :
        count2 +=1

    if(count1 >count2):
        if(count1 - count2 ==1):
            time = int((goal[i][1]*60)+goal[i][2])
        if(i==(n-1)):
            time1 += 48*60 - time

    elif(count2 > count1):
        if(count2-count1 ==1):
            time= int((goal[i][1]*60)+goal[i][2])
        if(i==(n-1)):
            time2 += 48*60 - time
    if(count1 == count2):
        if(i !=0):
            
            if(goal[i][0]==1):
                time2 += int((goal[i][1]*60)+goal[i][2])-time
            else:
                time1 += int((goal[i][1]*60)+goal[i][2])-time

print(time1)
print(time2)
