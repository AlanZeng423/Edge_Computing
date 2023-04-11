# from input import M, N, C, T, Y, D
# import numpy as np
#
# '''
# X_ij^t
# '''
#
# # x[t][i][j]  t时刻第i(1≤i≤M)个客户节点向第j(1≤j≤N)个边缘节点分配的带宽
# # X = [[[0] * (N + 1) for i in range(M + 1)] for j in range(T + 1)]
# X = np.zeros(M + 1, N + 1, T + 1)
# # 第 j 个边缘节点在 t 时刻的总带宽需求为 w[j][t]
# W = [[0] * (T + 1) for i in range(N + 1)]
# # 第 j 个边缘节点的成本 Sj
# S = [0] * (N + 1)
#
# Cc = [0] * (N + 1)  # Cc:currentC[j]
# Cc = C
#
# for t in range(1, T + 1):
#     for i in range(1, M + 1):
#         dc = D[t][i]  # dc:currentD
#         for j in range(1, N + 1):
#             if Y[i][j] == 0:
#                 continue
#             # if dc == 0:  # 如果当前客户节点带宽需求=0
#             # X[i][j][t] = 0
#             if Cc[j] >= dc:
#                 X[i][j][t] = dc
#                 Cc[j] -= dc
#                 dc = 0
#             else:  # C[j] < dc
#                 X[i][j][t] = Cc[j]
#                 dc = dc - Cc[j]
#                 Cc[j] = 0
#         if dc != 0:  # 如果i客户节点连接的边缘节点无法满足其需求
#             over = dc
#             x = 1
#             xMax = 0
#             x_countMax = 0
#             for x in range(1, N+1):
#                 count = [] * N
#                 if Y[i][x] == 1 & x != j:  # 找到一个与客户i相连通的边缘节点x
#                     k = 1
#                     for k in range(1,):  # 统计该边缘节点的连通数
#                         if Y[k][x] == 1:  # 如果客户k与边缘节点x连通
#                             count[x] = count[x] + 1
#                             if count[x] > x_countMax:
#                                 x_countMax = count[x]
#                                 xMax = x
#                         k = k + 1
#             # 先找出当前与客户节点i的有最大连通数的边缘节点xMax
#             # 再对所有与xMax相连的客户节点计算其冗余带宽（连接的边缘节点上限带宽和-该客户节点需求）
#             # 选取冗余最大的客户节点进行排水
#
#
#
#
#
#
#
