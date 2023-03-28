from input import T, M, N, edge_ID, client_ID

'''
X_ij^t
'''


# x[i][j][t]  t时刻第i(1≤i≤M)个客户节点向第j(1≤j≤N)个边缘节点分配的带宽
X = [[[0]*(T+1) for i in range(N+1)] for j in range(M+1)]
# 第 j 个边缘节点在 t 时刻的总带宽需求为 w[j][t]
W = [[0]*(T+1) for i in range(N+1)]
# 第 j 个边缘节点的成本 Sj
S = [0]*(N+1)





