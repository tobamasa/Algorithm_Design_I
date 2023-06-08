"""
DPのO(nW)を確認するためのプログラムコード
"""
import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd
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
               [i+1 for i in range(2)],
               [i+1 for i in range(3)],
               [i+1 for i in range(4)],
               [i+1 for i in range(5)],
               [i+1 for i in range(6)],
               [i+1 for i in range(7)],
               [i+1 for i in range(8)],
               [i+1 for i in range(9)],
               [i+1 for i in range(10)],
               [i+1 for i in range(11)],
               [i+1 for i in range(12)],
               [i+1 for i in range(13)],
               [i+1 for i in range(14)],
               [i+1 for i in range(15)],
               [i+1 for i in range(16)],
               [i+1 for i in range(17)],
               [i+1 for i in range(18)],
               [i+1 for i in range(19)],
               [i+1 for i in range(20)]]
max_w_list = [i+1 for i in range(20)]

# 表を作成
dp_fig = pd.DataFrame(columns=[i+1 for i in range(20)])

# 実験部分
for weight_serect in weight_list:
    print(f"weight len : {len(weight_serect)}")
    fix_dp_esb = [] # それぞれの重みで実験を行った時の平均実行時間を保持
    for max_w_serect in max_w_list:
        dp_time= [] # ある重みWの時の平均実行時間を取得するためリスト化
        for num in range(epoch): # DPの実行時間計測
            time_start = time.perf_counter()
            subset_sum(weight_serect, max_w_serect)
            time_end = time.perf_counter()
            dp_time.append(time_end-time_start)
        print(f"\tmax_w : {max_w_serect}")
        print("\t\tDP  :{}".format(np.array(dp_time).mean()))
        fix_dp_esb.append(np.array(dp_time).mean())
    dp_fig.loc[f'{len(weight_serect)}'] = fix_dp_esb
dp_fig.to_csv('./DP_FIG_20to20.csv')

# データの作成
x = np.array([i+1 for i in range(20)])  # x軸の範囲を指定
df_dp = pd.read_csv('DP_FIG_20to20.csv', index_col=0, skiprows=0)

# 散布図のプロット
for p in range (20):
    y = np.array([p+1 for i in range(20)])  # y軸の範囲を指定
    plt.scatter(x, y, c=df_dp[f'{p+1}'],s=160,marker='s')

plt.colorbar(label='z')  # カラーバーを表示
plt.savefig('./DP_Order.png')
