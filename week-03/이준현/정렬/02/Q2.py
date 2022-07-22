test = int(input())
array = list()

for i in range(test):
    data = input().split()
    array.append((data[0], int(data[1])))
array.sort(key=lambda x: x[1])

for i in array:
    print(i[0], end=' ')
#sort로 리스트 자체를 정렬하는 것과 sorted로 새로운 리스트를 반환하는 것중 무엇이 더 빠른지 판단이 안섬
#sorted가 단순하게 기존의 리스트를 헤치지 않는 다는 장점 이외에 속도면에 더 의미가 있는 건지, 기존의 리스트를 재활용할 일이 없다면
#리스트 메소드 sort를 쓰는게 더 빠른건지 모르겠다.