n = int(input())

array = []
for _ in range(n):
	array.append(input().split())

array.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in array:
	print(student[0])
