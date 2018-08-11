import numpy as np

from archmm.maxent import MEMM


if __name__ == '__main__':

    X1 = np.random.rand(150, 10)
    X1[:50, 2] += np.arange(0, 50) * 0.2 + 78
    X1[50:100, 7] -= np.arange(50, 0, -1) * 0.2 + 98
    X1[100:, 3] += np.arange(0, 50) * 0.2 + 2
    X_s = [X1]
    Y1 = np.zeros(150)
    Y1[:50] = 1
    Y1[50:100] = 2
    Y_s = [Y1]

    memm = MEMM(3)
    memm.fit(X_s, Y_s)

    X2 = np.random.rand(100, 10)
    X2[:50, 2] += np.arange(0, 50) * 0.2 + 78
    X2[50:, 3] += np.arange(0, 50) * 0.2 + 2
    
    print(memm.predict(X2))
