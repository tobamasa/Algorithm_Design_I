import numpy as np
import time
import pandas as pd

# しらみつぶし探索
def exhaustive_search_bit(weight_list, target_sum):
    n = len(weight_list)
    solution = [] # 候補解
    for i in range(2**n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(weight_list[j])
        if sum(subset) == target_sum:
            solution.append(subset)
    return solution

# 動的計画法を用いた部分和問題
def subset_sum(weight_list, w):
    n = len(weight_list)
    M = np.full((n+1,w+1), -1)
    for j in range (w+1):
        M[0, j] = 0
    for i in range (1,n+1):
        for j in range (w+1):
            if j < weight_list[i-1]:
                M[i,j] = M[i-1, j]
            else:
                M[i,j] = max(M[i-1,j], weight_list[i-1]+M[i-1, j-weight_list[i-1]])
    return M[n,w]

# 実験条件
epoch = 10
weight_list = [[i+1 for i in range(1)],
               [i+1 for i in range(5)],
               [i+1 for i in range(10)],
            #    [i+1 for i in range(11)],
            #    [i+1 for i in range(12)],
            #    [i+1 for i in range(13)],
            #    [i+1 for i in range(14)],
               [i+1 for i in range(15)],
            #    [i+1 for i in range(16)],
            #    [i+1 for i in range(17)],
            #    [i+1 for i in range(18)],
            #    [i+1 for i in range(19)],
               [i+1 for i in range(20)]]
max_w_list = [1, 5, 10, 15, 20]

# 表を作成
esb_fig = pd.DataFrame(columns=['w1','w5','w10','w15','w20'])
dp_fig = pd.DataFrame(columns=['w1','w5','w10','w15','w20'])

# 実験部分
for weight_serect in weight_list:
    print(f"weight len : {len(weight_serect)}")
    fix_w_esb, fix_dp_esb = [], [] # それぞれの重みで実験を行った時の平均実行時間を保持
    for max_w_serect in max_w_list:
        esb_time, dp_time = [], [] # ある重みWの時の平均実行時間を取得するためリスト化
        for num in range(epoch): # しらみつぶしの実行時間計測
            time_start = time.perf_counter()
            exhaustive_search_bit(weight_serect, max_w_serect)
            time_end = time.perf_counter()
            esb_time.append(time_end-time_start) 

        for num in range(epoch): # DPの実行時間計測
            time_start = time.perf_counter()
            subset_sum(weight_serect, max_w_serect)
            time_end = time.perf_counter()
            dp_time.append(time_end-time_start)
        print(f"\tmax_w : {max_w_serect}")
        print("\t\tESB :{}".format(np.array(esb_time).mean()))
        print("\t\tDP  :{}".format(np.array(dp_time).mean()))
        fix_w_esb.append(np.array(esb_time).mean())
        fix_dp_esb.append(np.array(dp_time).mean())
    esb_fig.loc[f'n{len(weight_serect)}']= fix_w_esb
    dp_fig.loc[f'n{len(weight_serect)}'] = fix_dp_esb

esb_fig.to_csv('./ESB_FIG2.csv')
dp_fig.to_csv('./DP_FIG2.csv')