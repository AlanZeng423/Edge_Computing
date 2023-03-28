# Edge_Computing 边缘计算

### 参数
- T：时刻
  - `len(demand_csv)-1` 
  - demand.csv表行数-1
- M：客户节点个数
  - `len(demand_csv[0])-1` 
  - demand.csv表列数-1
- N：边缘节点个数
  - `len(device_csv)-1`
  - device.csv行数-1
- C：对应边缘节点j的带宽上限Cj—>C\[j\]
  - device.csv的第二列bandwith
- Y\[i\]\[j\]：连通性
  - 客户节点i与边缘节点j的连通性情况Yij对应Y\[i\]\[j\]--(N+1)行*(M+1)列
- X：分配方案，有三个参数，第一个是时间，第二个是客户 ，第三个是edge，储存在 时间下，客户使用 edge的大小 
  - x\[i\]\[j\]\[t\]  t时刻第i(1≤i≤M)个客户节点向第j(1≤j≤N)个边缘节点分配的带宽
  - X's Def:`X = [[[0]*(T+1) for i in range(N+1)] for j in range(M+1)]`
- D：表示客户节点 i 在该时刻 t 的带宽需求Dit