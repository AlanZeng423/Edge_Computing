from input import M, N, C, T, Y, D

'''
X_ij^t
'''

# x[t][i][j]  t时刻第i(1≤i≤M)个客户节点向第j(1≤j≤N)个边缘节点分配的带宽
X = [[[0] * (N + 1) for i in range(M + 1)] for j in range(T + 1)]
# 第 j 个边缘节点在 t 时刻的总带宽需求为 w[j][t]
W = [[0] * (T + 1) for i in range(N + 1)]
# 第 j 个边缘节点的成本 Sj
S = [0] * (N + 1)

# 思路1：先提供一个可以存储，在任意时刻，某一edge带宽使用总额的二维数组 alledge[time][j]（对X中的时间和edge进行循环遍历，可以得到），
# 对alledge[][]排序？（新数组一维即可，因为每次都要使用；冒泡排序吧 ，里面存edge的序列，edge从小到大进行排列）对edge进行从小到大的使用，同时更新X，判断X的空位

alledge = [[0] * (N + 1) for i in range(T + 1)]  # 某一时间，edge使用带宽的总额
sortedge = [0] * (N + 1)  # 用于给alledge进行排序，相当于所以，避免破坏alledge的顺序


def put(t, alledge, sortedge, X, C, D, Y):
    for i in range(1, M + 1):  # 对客户进行遍历
        count = D[t][i]
        for j in range(1, N + 1):  # 对edge进行遍历
            list = sortedge[j]  # 使用edge的大小排序来遍历，也可以保证不重不漏
            if Y[i][list] == 1 & X[t][i][list] != C[j]:
                if C[list] - alledge[t][list] >= count:  # 可以放进去
                    alledge[t][list] += count  # 可能之前用过，所以
                    X[t][i][list] = count
                    count = 0
                else:  # 当前的不够放
                    alledge[t][list] = C[list]  # 直接装满了
                    X[t][i][list] = C[list] - alledge[t][list]
                    count -= C[list] - alledge[t][list]
            # 由于在递归的过程中，alledge的已经被维护了，所以不用再多谢一个函数进行维护了
    # 函数到现在，t次的分配已经完成了，需要对alledge[][]进行排序，保证每次挑到的都是上次使用最少的edge节点，减小成本
    alledge1 = [[0] * (N + 1) for i in range(T + 1)]
    alledge1 = alledge
    for i in range(1, N + 1):
        count = 1
        for j in range(2, N + 1):
            if alledge1[t][count] > alledge1[t][j] & alledge1[t][j] != -1:
                #谁小要谁，
                count = j
        alledge1[t][count] = -1
        #得到就令其为-1就行
        sortedge[i] = count


for i in range(1, T + 1):
    put(i, alledge, sortedge, X, C, D, Y)
