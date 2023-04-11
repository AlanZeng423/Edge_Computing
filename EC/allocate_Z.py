from input import M, N, C, T, Y, D

# x[t][i][j]   t时刻第i(1≤i≤M)个客户节点向第j(1≤j≤N)个边缘节点分配的带宽
X = [[[0] * (N + 1) for i in range(M + 1)] for j in range(T + 1)]

# Array usage[t][j]  在t时刻j边缘节点的使用量
usage = [[0] * (N + 1) for i in range(T + 1)]


# usage[t][j] = for i in range(M+1) : u+=x[t][i][j]

# 定义函数sort_by_usage
def sort_by_usage(usage, t):
    # 构建一个字典，用于存储每个节点在t时刻的使用量
    usage_dict = {}
    for j in range(len(usage[t])):
        usage_dict[j] = usage[t][j]

    # 对字典按照使用量升序排序
    sorted_dict = sorted(usage_dict.items(), key=lambda x: x[1])

    # 构建结果数组
    result = [x[0] for x in sorted_dict]

    return result


# Array Cc:currentC[j]
Cc = [0] * (N + 1)
Cc = C  # 对应边缘节点j的带宽上限C[j]

for t in range(T + 1):
    for i in range(M + 1):
        dc = D[t][i]  # dc:currentD 当前t时刻，客户i需要的带宽
        for j in sort_by_usage(usage, t):
            if Y[i][j] == 0:  # 如果不连通，跳过
                continue
            # if dc == 0:  # 如果当前客户节点带宽需求=0
            # X[t][i][j] = 0
            if Cc[j] >= dc:  # 如果t时刻当前边缘节点j的剩余带宽≥dc
                X[t][i][j] = dc
                Cc[j] -= dc
                dc = 0
            else:  # C[j] < dc
                X[i][j][t] = Cc[j]
                dc = dc - Cc[j]
                Cc[j] = 0
        if dc != 0:  # 如果i客户节点连接的边缘节点无法满足其需求
            over = dc  # def over为溢出值
            x = 1
            xMax = 0
            x_countMax = 0
            for x in range(1, N + 1):  # 在边缘节点中寻找
                count = [] * N  # Array count 记录
                if Y[i][x] == 1:  # 找到一个与客户i相连通的边缘节点x
                    k = 1
                    for k in range(1, ):  # 统计该边缘节点的连通数
                        if Y[k][x] == 1:  # 如果客户k与边缘节点x连通
                            count[x] = count[x] + 1
                            if count[x] > x_countMax:
                                x_countMax = count[x]
                                xMax = x
                        k = k + 1
            # 先找出当前与客户节点i的有最大连通数的边缘节点xMax
            # 再对所有与xMax相连的客户节点计算其冗余带宽（连接的边缘节点上限带宽和-该客户节点需求）
            # 选取冗余最大的客户节点进行排水
