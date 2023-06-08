import pandas as pd
import matplotlib.pyplot as plt

# CSVファイルの読み込み
df_esb = pd.read_csv('ESB_FIG2.csv', index_col=0, skiprows=0)
df_dp = pd.read_csv('DP_FIG2.csv', index_col=0, skiprows=0)

# グラフの作成
x = [1,5,10,15,20]
x2 = [1,5,10,11,12,13,14,15,16,17,18,19,20]
"""
for i in x:
    esb = plt.plot(x, df_esb.loc[f'n{i}'], marker="o")
    dp = plt.plot(x, df_dp.loc[f'n{i}'], marker="o")

    # グラフのタイトルと軸ラベルの設定
    plt.title(f'n = {i}')
    plt.xlabel('w')
    plt.ylabel('Time')
    plt.legend((esb[0], dp[0]), ("ESB", "DP"), loc=2)

    # グラフの表示
    plt.savefig(f'./n={i}.png')
    plt.close()
"""
for i in x:
    esb = plt.plot(x2, df_esb[f'w{i}'], marker="o")
    dp = plt.plot(x2, df_dp[f'w{i}'], marker="o")

    # グラフのタイトルと軸ラベルの設定
    plt.title(f'w = {i}')
    plt.xlabel('n')
    plt.ylabel('Time')
    plt.legend((esb[0], dp[0]), ("ESB", "DP"), loc=2)

    # グラフの表示
    plt.savefig(f'./w={i}.png')
    plt.close()