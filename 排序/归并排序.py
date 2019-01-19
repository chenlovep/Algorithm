def break_sort(L):
    L_len = len(L)
    A = []
    #序列长度为1时，将其返回
    if len(L) == 1:
        return L   
    L_1 = L[:len(L)//2]
    L_2 = L[len(L)//2:]
    L_left = break_sort(L_1)
    L_right = break_sort(L_2)
    #将分开的两个序列进行合并
    while True:
        if L_left[0] < L_right[0]:
            A.append(L_left[0])
            del L_left[0]
        else:
            A.append(L_right[0])
            del L_right[0]
        if len(L_left) == 0:
            A += L_right
            break
        if len(L_right) == 0:
            A += L_left
            break
    return A
#归并排序
def merge_sort(L):
    #新序列
    #将序列拆分成两部分
    A = [];L_left = [];L_right = []
    L_ = break_sort(L)
    return L_
    
    
L = [9,8,7,532,3,2,3423]
#L_插入排序后的序列
L_ = merge_sort(L)
print(L_)
