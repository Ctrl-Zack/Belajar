import numpy as np

def gauss(a):
    n = a.shape[0]
    det = 1.0e0
    iterasi = 1
    for k in range(n):
        # tukar baris
        if np.fabs(a[k,k]) < 1.0e-3:
            for i in range(k+1, n):
                if np.fabs(a[i,k]) > np.fabs(a[k,k]):
                    for j in range(k, n):
                        a[k,j], a[i,j] = a[i,j], a[k,j]
                    print(f"iterasi : {iterasi}")
                    print(a)
                    iterasi += 1
                    break
        # 1 utama
        pivot = a[k,k]
        for j in range(k, n):
            a[k,j] /= pivot
            a[k,j] = round(a[k,j], 2)
        det *= pivot
        det = round(det, 2)
        print(f"iterasi : {iterasi}")
        print(a)
        iterasi += 1
        # meng-0-kan
        for i in range(k, n):
            if i == k or a[i,k] == 0: continue
            factor = a[i, k]
            for j in range(k, n):
                a[i,j] -= factor * a[k,j]
            print(f"iterasi : {iterasi}")
            print(a)
            iterasi += 1
    return a, det


a = [[7, -5, -7], [-5, 9, 9], [4, -5, 3]]
a = np.array(a, float)
print("matrix awal :")
print(a)
A, DET = gauss(a)
print("matrix akhir :")
print(A)
print("determinan :")
print(DET)