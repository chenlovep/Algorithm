def new_insert_sort(A,a):
    #A已排序序列
    #a待插入数据

    #已排序序列为空，则添加第一个数据
    if len(A) == 0:
        A.append(a)
        return A
    for i in range(len(A)):
        #带插入数据为最小
        if A[i]>= a:
            A.insert(i,a)
            return A
    #待插入数据为最大
    A.append(a)
    return A
def insert_sort(L):
    #新序列
    A = []
    for i in range(len(L)):
        A = new_insert_sort(A, L[i])
    return A
L = [1,1,1,1,1,1]
#L_插入排序后的序列
L_ = insert_sort(L)
print(L_)
