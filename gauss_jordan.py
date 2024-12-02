import numpy as np

def gaussJordan(a, b):
    a = np.array(a, float)
    b = np.array(b, float)
    n = len(b)
    det = 1.0e0
    for k in range(n):
        if np.fabs(a[k,k]) < 1.0e-3:
            for i in range(k+1, n):
                if np.fabs(a[i,k]) > np.fabs(a[k,k]):
                    for j in range(k, n):
                        a[k,j], a[i,j] = a[i,j], a[k,j]
                    b[k], b[i] = b[i], b[k]
                    break
        pivot = a[k,k]
        for j in range(k, n):
            a[k,j] /= pivot
            a[k,j] = round(a[k,j], 2)
        b[k] /= pivot
        b[k] = round(b[k], 2)
        det *= pivot
        det = round(det, 2)
        for i in range(n):
            if i == k or a[i,k] == 0: continue
            factor = a[i, k]
            for j in range(k, n):
                a[i,j] -= factor * a[k,j]
            b[i] -= factor * b[k]

    return a, b, det


a = [[7, -5, -7], [-5, 9, 9], [4, -5, 3]]
b = [0, 0, 0]

A, X, Det = gaussJordan(a, b)
print(X)
print(A)
print(Det)