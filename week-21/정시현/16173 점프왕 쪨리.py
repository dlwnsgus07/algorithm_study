#열혈노가다 했지만 장렬하게 틀림 나름 66퍼까지는 갔다..ㅎ
n = int(input())
map = [list(map(int,input().split())) for i in range(n)]

if(n==2):
    if(map[0][0]==1):
        if(map[1][0]==1):
            print("HaruHaru")
        elif(map[0][1]==1):
            print("HaruHaru")
        else:
            print("Hing")
    else:
        print("Hing")
else:
    if(map[0][0]==1):
        if(map[1][0]==1):
            if(map[2][0]==1):
                if(map[2][1]==1):
                    print("HaruHaru")
                else:
                    print("Hing")
            elif(map[2][0]==2):
                print("HaruHaru")

            elif(map[1][1]==1):
                if(map[1][2]==1 or map[2][1]==1):
                    print("HaruHaru")
                else:
                    print("Hing")
            else:
                print("Hing")
        elif(map[1][0]==2):
            if(map[1][2]==1):
                print("HaruHaru")
            else: print("Hing")
        
        elif(map[0][1]==1):
            if(map[0][2]==1):
                if(map[1][2]==1):
                    print("HaruHaru")
                else:
                    print("Hing")
            elif(map[0][2]==2):
                print("HaruHaru")
            elif(map[1][1]==1):
                if(map[1][2]==1 or map[2][1]==1):
                    print("HaruHaru")
                else:
                    print("Hing")
            else:
                print("Hing")
        elif(map[0][1]==2):
            if(map[2][1]==1):
                print("HaruHaru")
            else: print("Hing")    
        else:
            print("Hing")
    elif(map[0][0]==2):
        if(map[2][0]==1):
            if(map[2][1]==1):
                print("HaruHaru")
            else:
                print("Hing")
        elif(map[2][0]==2):
            print("HaruHaru")
        elif(map[0][2]==1):
            if(map[1][2]==1):
                print("HaruHaru")
            else:
                print("Hing")
        elif(map[0][2]==2):
            print("HaruHaru")
        else:
            print("Hing")
    else:
        print("Hing")