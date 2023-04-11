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


# 如果i客户节点连接的边缘节点无法满足其需求
# 先找出当前与客户节点i联通的 有最大连通数的边缘节点xMax
def maxEdgeNode(i):
    xm = 0  # 当前与客户节点i连通的 有最大连通数的边缘节点xMax
    xcm = 0  # 当前与客户节点i连通的 有最大连通数的边缘节点xMax的连通数x_countMax
    for x in range(1, N + 1):  # 在边缘节点中寻找
        count = [0] * (N + 1)  # Array count 记录这个边缘节点的连通数
        if Y[i][x] == 1:  # 找到一个与客户i相连通的边缘节点x
            for k in range(1, M + 1):  # 在客户节点中遍历，统计该边缘节点的连通数
                if Y[k][x] == 1:  # 如果客户k与边缘节点x连通
                    count[x] = count[x] + 1
                    if count[x] > xcm:
                        xcm = count[x]
                        xm = x
    ans = [0] * 2
    ans[0] = xm
    ans[1] = xcm
    return ans


# 再对所有与xMax相连的客户节点计算其冗余带宽（连接的边缘节点上限带宽和-该客户节点需求）
def redundancyOfClients(x, t0):
    total = [0] * (M + 1)
    for i in range(1, M + 1):  # 遍历客户节点
        if Y[i][x] == 1:  # 如果客户i与x连通
            for j in range(1, N + 1):  # 计算其连接的边缘节点带宽上限和
                total[i] = total[i] + C[j]
        total[i] = total[i] - D[t0][i]
    return total


# 选取冗余最大的客户节点进行排水
def find_max_index(arr):
    max_index = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index


def drainage(t0, fr, ov, x, to):  # 排水：t0时刻，从客户fr，溢出ov，通过边缘节点x，排到客户to

    if ov < X[t0][to][x]:
        x1 = ov
        X[t0][to][x] -= ov
        x[t0][fr][x] += ov
        for j in range(N + 1):  # 遍历边缘节点
            if j != x:
                if (Cc[j] - X[t0][to][j]) >= x1:  # 如果与to相连的边缘节点的剩余≥x1
                    X[t0][to][j] += x1
                else:
                    x[t0][to][j] = Cc[j]  # x[t0][to][j] += Cc[j]-x[t0][to][j]
                    x1 = x1 - (Cc[j] - x[t0][to][j])
        return True
    else:
        return False


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
                X[t][i][j] = Cc[j]
                dc = dc - Cc[j]
                Cc[j] = 0
        if dc != 0:  # 如果i客户节点连接的边缘节点无法满足其需求
            over = dc  # def over为溢出值
            xMax = maxEdgeNode(i)[0]  # 当前与客户节点i连通的 有最大连通数的边缘节点xMax
            x_countMax = maxEdgeNode(i)[1]  # 当前与客户节点i连通的 有最大连通数的边缘节点xMax的连通数x_countMax
            redundancy = redundancyOfClients(xMax, t)  # 求出客户冗余数组
            maxRedundantClient = find_max_index(redundancy)  # maxRedundantClient冗余最大的客户节点
            # if not drainage(i, over, xMax, maxRedundantClient):  # 如果drainage返回True，则排水完成;反之这个xMax不足以完成排水
            drainage(t, i, over, xMax, maxRedundantClient)
