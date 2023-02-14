import array as arr
import numpy as np
lst = []
for i in range(0,10):
    ele = int(input())
    lst.append(ele)
arr1 = np.array(lst)
arr2 = np.where(arr1<=0,1,arr1)
for i in range(0,10):
    print('X[{}] = {}'.format(i,arr2[i]))