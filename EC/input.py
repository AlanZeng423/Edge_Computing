import csv

# 处理demand.csv文件
'''
demand.csv 
time,CB,CA,CE,CX...
- 第 1 列：即 time 列，表示不同时刻。
- 第 2 列 ~ 第 M+1 列：
    - 第 1 行：表示客户节点ID，唯一标识一个客户节点。长度不超过 10 的字符串，由大小写字母或数字组成。
    - 第 2 行 ~ 最后1行：表示客户节点在该时刻的带宽需求。非负整数，单位是 MB。
- 客户节点数： M ≤ 50 。
- 带宽值：不超过 2^63 ~ 1MB 。
'''

with open("./data/demand.csv", mode="r", encoding="utf-8", newline="") as demand_csv:
    demand_reader = csv.reader(demand_csv)
    demand_csv = list(demand_reader)

# T:时刻数
T = len(demand_csv) - 1
# M:客户节点数
M = len(demand_csv[0]) - 1
# 客户节点ID
client_ID = [0] * (M + 1)
for i in range(1, len(demand_csv[0])):
    client_ID[i] = str(demand_csv[0][i])
# 表示客户节点 i 在该时刻 t 的带宽需求Dit
D = [[0] * (M + 1) for i in range(T + 1)]
for t in range(1, T + 1):
    for i in range(1, M + 1):
        D[t][i] = int(demand_csv[t][i])

'''
device.csv
device_name,bandwith
- 第 1 列：即 device_name 列，表示边缘节点 ID，唯一标识一个边缘节点。长度不超过 32 的字符串。
- 第 2 列：即 bandwidth 列，表示对应边缘节点的带宽上限。非负整数，单位为 MB。
- 边缘节点数： N ≤ 300 。
- 带宽值：不超过 263 − 1MB 。
'''
with open("./data/device.csv", mode="r", encoding="utf-8", newline="") as device_csv:
    device_reader = csv.reader(device_csv)
    device_csv = list(device_reader)

# N:边缘节点数
N = len(device_csv) - 1
# edge节点ID
edge_ID = [0]*(N+1)
# 对应边缘节点j的带宽上限Cj
C = [0]*(N+1)
for i in range(1,len(device_csv)):
    edge_ID[i] = str(device_csv[i][0])
    C[i] = int(device_csv[i][1])

'''
connect.csv
device_name,CB,CA,CE,CX...
- 第 1 列：即 device_name 列，表示边缘节点 ID，唯一标识一个边缘节点。
- 第 2 列 ~ 第 M+1 列：
    – 第 1 行：表示客户节点 ID，唯一标识一个客户节点。
    – 第 2 行 最后一行：表示客户节点与该边缘节点的连通性情况，0 代表不连通，1 代表连通。
'''
with open("./data/connect.csv", mode="r", encoding="utf-8", newline="") as connect_csv:
    connect_reader = csv.reader(connect_csv)
    connect_csv = list(connect_reader)

# 客户节点i与该边缘节点j的连通性情况Yij
Y = [[0] * (N + 1) for i in range(M + 1)] # (N+1)行*(M+1)列
for i in range(1, len(connect_csv)):
    for j in range(1, len(connect_csv[0])):
        Y[j][i] = int(connect_csv[i][j])


# test
print(T)
print(M,N)
print(len(client_ID),len(edge_ID))
print(len(D),len(D[0]))
print(len(C))
print(len(Y),len(Y[0]))