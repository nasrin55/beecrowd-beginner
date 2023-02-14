import numpy as np
for i in np.arange(0, 3.0, 0.2):
    for j in np.arange(i+1, i+4, 1):
        print('I=%.1lf J=%.1lf' %(i, j))