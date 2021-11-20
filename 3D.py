import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib

# 支持中文显示
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义坐标轴
fig = plt.figure()
ax1 = plt.axes(projection='3d')
# ax = fig.add_subplot(111,projection='3d')  #这种方法也可以画多个子图

# 定义三维数据
xx = np.arange(0.1, 0.8, 0.01)
yy = np.arange(0.1, 0.8, 0.01)
X, Y = np.meshgrid(xx, yy)
# Z = np.sin(X) + np.cos(Y)
Z = (12500*X**2 - 12500*X + 37044*Y + 40169)/(5*(Y + 1))
# Z = (18*B*d**2 + 26520*B*d + 5000*B + 9*d**3 + 13260*d**2 - 5000*d)/(2*d*(2*B + d))

# 作图
# ax1.plot_surface(X,Y,Z,cmap='rainbow')
# ax1.contour(X,Y,Z, zdim='z',offset=-2，cmap='rainbow)   #等高线图，要设置offset，为Z的最小值
# ax1.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
# ax1.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm)
ax1.plot_surface(X, Y, Z, rstride=1, cstride=1, color='gray')
ax1.set_xlabel(r'$\lambda$')
ax1.set_ylabel(r'$\beta$')
# ax1.set_zlabel('利润差', rotation=270)
# plt.title("制造商", Y=-0.1)
ax1.set_zlabel('Total profit', rotation=270)
# plt.title("集中决策", Y=-0.1)
plt.show()
