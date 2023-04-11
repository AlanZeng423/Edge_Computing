from input import T, M, D, N, client_ID, edge_ID
from allocate_Z import X

'''

• customer_ID1：表示客户节点 ID。
• <site_id_1,bandwidth_1>：表示把该客户节点的大小为 bandwidth_1 的带宽需求分配给ID 为 site_id_1 的边缘节点。
'''

solution = open("solution.txt", "wt")

# 输出分配方案
for t in range(1, T + 1):
    for i in range(1, M + 1):
        client_node = client_ID[i]
        if D[t][i] == 0:
            print(client_node + ":", file=solution)
            continue
        temp = []
        for j in range(1, N + 1):
            if X[t][i][j] != 0:
                edge_node = edge_ID[j]
                temp_s = f"<{edge_node},{X[t][i][j]}>"
                temp.append(temp_s)
        if len(temp) != 0:
            print(client_node + ":", end="", file=solution)
        for k in range(len(temp)):
            if k == len(temp) - 1:
                print(temp[k], file=solution)
            else:
                print(temp[k], end=",", file=solution)

solution.close()
