# 导入包
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 支持中文显示
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建数据
x = np.arange(0.1, 1.76, 0.01)
# y1 = (7264 * x + 5389) / (x + 1)  # 集中决策
y1 = -470.5 + 16.0*(x - 50)**2/x
y2 = 12.0*x + 387.458333333333 + 30000.0/x  # 制造商主导
y3 = 12.0*x + 387.458333333333 + 30000.0/x  # 零售商主导
y4 = 14.2222222222222*x + 410.814814814815 + 35555.5555555556/x  # 势均力敌

# 画曲线
plt.plot(x, y1, label='集中决策', color='k', linewidth=1, linestyle="-")
plt.plot(x, y2, label='制造商主导', color='b', linewidth=1, linestyle="-")
plt.plot(x, y3, label='零售商主导', color='b', linewidth=1, linestyle="--")
plt.plot(x, y4, label='势均力敌', color='g', linewidth=1, linestyle="-")

# 设置坐标轴范围
# plt.xlim((0, 1))
# plt.ylim((5200, 7000))

# 设置坐标轴刻度
# my_x_ticks = np.arange(0, 1.1, 0.1)
# my_y_ticks = np.arange(200, 720, 50)
# plt.xticks(my_x_ticks)
# plt.yticks(my_y_ticks)

# 设置坐标轴名称
plt.xlabel('需求价格弹性')
plt.ylabel('供应链总利润')

# 显示出所有图标
plt.legend(loc='right')
# 显示出所有设置
plt.show()
