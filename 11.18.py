#Duy Le 1913048
my_list = []
my_list1 = input().split()
n = len(my_list1)
for i in range(0,n):
    i = int(my_list1[i])
    if i >= 0:
        my_list.append(i)
my_list.sort()
print(*my_list, sep = ' ')