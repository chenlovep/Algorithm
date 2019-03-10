#全排列递归
'''
a=[1,2,3]

all_ = []
def all_list(a,part_first,part_second):
    if part_first == part_second:
        print(a)
        all_.append(a[:])
    else:
        for i in range(part_first, part_second):
            a[i], a[part_first] = a[part_first], a[i]
            all_list(a, part_first+1, part_second)
            a[i], a[part_first] = a[part_first], a[i]
all_list(a,0,len(a))
print(all_)
'''

#全排列 深度优先
a=[1,2,3]
visit = ['True']*len(a)
temp = [""] *len(a)
all_ = []
def dfs(a,position):
    if position == len(a):
        all_.append(temp[:])
        return
    for index in range(0,len(a)):
        if visit[index] == 'True':
            temp[position] = a[index]
            visit[index] = 'False'
            dfs(a,position+1)
            visit[index] = 'True'
dfs(a,0)
print(all_)
