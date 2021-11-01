import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('clean_output.csv')
# data.columns = ["seed", "m", "n", "n_estimate","n_sigma","n_2sigma","time"]
m_values = [64, 512, 1024, 2048]
n_values = [10 ** 3, 10 ** 6, 5 * 10 ** 6]
for n in n_values:
    for m in m_values:
        sub_data = data.loc[(data['m'] == m) & (data['n'] == n), 'time']
        number_of_tries = sub_data.shape[0]
        total_time = sub_data.sum(axis=0)
        avg_time = total_time/number_of_tries
        std = 0
        sub_values = sub_data.values
        for i in sub_values:
            std += (i-avg_time)**2
        std = (std/number_of_tries)**0.5
        # sub_data = data.loc[(data['m'] == m) & (data['n'] == n) & (data['sigma'] == True)]
        # sigma_positive = sub_data.shape[0]
        # sub_data = data.loc[(data['m'] == m) & (data['n'] == n) & (data['2sigma'] == True)]
        # sigma2_positive = sub_data.shape[0]
        print(f'n: {n}, m: {m}, mean: {avg_time}, std: {std}')


# for n in n_values:
#     for m in m_values:
#         sub_data = data.loc[(data['m'] == m) & (data['n'] == n)]
#         number_of_tries = sub_data.shape[0]
#         sub_data = data.loc[(data['m'] == m) & (data['n'] == n) & (data['sigma'] == True)]
#         sigma_positive = sub_data.shape[0]
#         sub_data = data.loc[(data['m'] == m) & (data['n'] == n) & (data['2sigma'] == True)]
#         sigma2_positive = sub_data.shape[0]
#         print(f'n: {n}, m: {m}, sigma: {sigma_positive}, sigma2: {sigma2_positive}')

# colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:purple']
# sub_data = data.loc[(data['n'] == 10 ** 6)]
# x_label = [i + 1 for i in range(sub_data.shape[0])]

# for idx, m in enumerate(m_values):
#     y_label = []
#     sub_data2 = data.loc[(data['m'] == m) & (data['n'] == 10 ** 6), 'n_estimate']
#     sub_values = sub_data2.values
#     for i in sub_values:
#         y_label.append((10 ** 6 - i) / 10 ** 6 * 100)
#     plt.bar(x_label[idx*sub_data2.shape[0]:(idx+1)*sub_data2.shape[0]], y_label, color=colors[idx], label=str(m))
#
# plt.axhline(y=0, color='r', linestyle='-')
# plt.legend()
# ax = plt.gca()
# ax.axes.xaxis.set_visible(False)
# plt.show()
