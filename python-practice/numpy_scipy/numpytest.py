import numpy as np 


# numpy基础知识
def learn():
    lst = [[1,3,4,6],[3,5,7,8]]
    print(lst)
    nplst = np.array(lst)
    # ndim 维度
    print(nplst.ndim)
    # 几行几列
    print(nplst.shape)
    # 总个数
    print(nplst.size)
    # 生成随机数，randn（正态分布），randint，rand（0～1）
    print(np.random.randn(2,4))
    # Choice随机选择一个数
    print(np.random.choice([2,5,63,87]))
    # random生成各种分布
    print(np.random.beta(1,20))


    # 如果数字个数能够平分，会自动那么可以用-1缺省，
    nlist=(np.arange(1,11).reshape([5,-1]))
    # exp-自然指数的几次方,exp2-平方，sqrt-开放，sin三角函数，log-自然对数
    print(np.exp(nlist))
    # sum,max,min,add,sub,mul,div,**,dot(点乘)
    # axis 表示计算的深度，为0表示最外层，1表示第二层进行计算
    print(nlist.sum(axis=1))

    # concatenate 或者 vstack(垂直方向)，hstack(水平方向),
    # 相当于list里面的append
    lst1=np.array([1,3,4])
    lst2=np.array([4,73,3])
    print(np.concatenate((lst1,lst2),axis=0))

    # split，copy
    print(np.split(lst1,3))
    print(np.copy(lst2))


    # 线性方程组
    # from numpy.linalg import * 

    # 单位矩阵
    print(np.eye(3))
    nn = np.array([[4,9],[2,5]])
    # 逆矩阵
    print(inv(nn))
    # 反向矩阵,transpose 是矩阵自带的方法，object.transpose
    print(nn.transpose())
    # 行列式
    print(det(nn))
    # 特征值和特征向量
    print(eig(nn))
    # 线性方程组
    y = np.array([[5,],[7,]])
    print(solve(nn,y))

    # fft，傅里叶变换，信号处理
    print(np.fft.fft(np.array([1,2,43,5,4,5,5,5,3,2,2,1,1])))
    # corf，皮尔逊相关系数
    print(np.corrcoef([1,20,1],[3,56,2]))
    # 生产一元多次函数
    # 两个参数，参数1一个数组，若没有参数2，则生成一个多项式，例如：
    #     p = np.poly1d([2,3,5,7])   
    #     print(p)    ==>>2x3 + 3x2 + 5x + 7  
    print(np.poly1d([2,4,6]))



# matplotlib基础绘图
import matplotlib.pyplot as plb

plb.plot([2,4,5,6],[3,3,4,6]) #两个列表，分别表示横坐标和纵坐标
plb.ylabel('text')
plb.axis([2,3,4,5])  # axis表示x轴起始区间【2，3】，y轴【4，5】
pib.savefig('filename',dpi=600) #dpi表示图片像素

plb.plot(x,y,format_string='颜色，线性，标记符号类型',)
plb.plot(x,y,fontproperties='SimHei',fontsize=20)  #另一种，matplotlib.rcParams['font.family/size/style']=''
plb.text(x,y,'text',fontsize=20,fontproperties='')
plb.annotate(x,y,'text',arrowoprops=dict(facecolor='black',shrink=0.1,width=2.0))  #shrink表示文字相对(x,y)偏移的距离，width表示宽度

#画子图
plb.subplot2grid((3,3),(1,0),colspan=2)
# 另一种方法
# import matplotlib.gridspec as gridspec
# gs = gridspec.GridSpec(3,3)
# plt.subplot(gs[2,:])


from matplotlib import figure

x = np.linspace(-np.pi,np.pi,256,endpoint=True)
c,s = np.cos(x),np.sin(x)
plb.figure(1)
plb.plot(x,c,color='green',label='cos',linewidth=2.0,linestyle='-.',alpha=0.5)
# ‘-‘                         实线  
# ‘:’                         虚线   
# ‘–’                         破折线 
# ‘None’,’ ‘,’’               什么都不画    
# ‘-.’                        点划线

plb.plot(x,s,'red*','',label='sin',linewidth=1.0,alpha=0.1)
ax = plb.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('data',0)
ax.spines['bottom'].set_postion('data',0)
plb.title('title-name')


# figure，画子图
fig = plb.figure()

# 直方图
np.random.seed(0)
mu,sigma = 100,20  #均值和标准差
a = np.random.normal(mu,sigma,size=100)  #生成正态分布数组100个
plb.hist(a,20,normed=1,histtype='stepfilled',facecolor='b',alpha=0.75)
plb.title('Histogram')


# 散点图
ax =fig.add_subplot(3,3,1) #把图画在画布分割成3行3列，图像画在从左到右从上到下的第1块
h = 128
x = np.random.normal(0,1,h)
y = np.random.normal(0,1,h)
t = np.arctan2(y,x) #上色
# plb.axes([0.025,0.025,0.95,0.95]) #画布四个边缘位置，一般用来表示显示范围
ax.scatter(x,y,s=75,c=t,alpha=.5) #画图，s=size,点的大小，c=color，点的颜色，alpha透明度
plb.xlim(-1.5,1.5),plb.xticks([]) #坐标轴取值范围
plb.ylim(-1.5,1.5),plb.yticks([])
plb.axis()
plb.title('aaaa')
plb.xlabel('x')
plb.ylabel('y')

# 柱状图
a1x=fig.add_subplot(3,3,2) 
n = 10
x = np.arange(n)
y1 = (1- x/float(n)) * np.random.uniform(0.5,1.0,n)
y2 = (1- x/float(n))* np.random.uniform(0.5,1.0,n)
#可以写a1x, 也可以直接用plb
plb.bar(x,+y1,facecolor='#9999ff',edgecolor='white') 
#可以写a1x, 也可以直接用plb
plb.bar(x,-y2,facecolor='#ff9999',edgecolor='white')#y1,y2前面的符号，表示y1的图朝上在上面半部分，y2朝下在下面半部分
for x,y in zip(x,y1):
    plb.text(x+0.4,y+0.5,'%.2f' % y, ha='center',va='bottom')
# for x,y in zip(x,y2): 
#     plb.text(x+0.4,-y-0.5,'%.2f' % y, ha='center',va='top')
#     这里x无法进行重新生成，报错“zip argument #1 must support iteration”


#饼图
fig.add_subplot(3,3,3)
n = 20
z = np.ones(n)
z[-1] *=2
plb.pie(z,explode=z*0.05,colors=['%.2f' % (i/float(n)) for i in range(n)],labels=['%.2f' % (i/float(n)) for i in range(n)])
plb.gca().set_aspect('equal')
plb.xticks([])
plb.yticks([])

# 折线图
fig.add_subplot(3,3,4)
n = 20
theta = np.arange(0.0,2*np.pi,2*np.pi/n)
radii = 10 * np.random.rand(n)
plb.plot(theta,radii)

# 极坐标图
N= 20
theta = np.linspace(0.0,2*np.pi,N,endpoint=False)
radii1 = 10*np.random.rand(N)
width1 = np.pi/4*np.random.rand(N)
bars = plb.bar(theta,radii1,width1,bottom=0.0)
for r ,bar in zip(radii1,bars):
    bar.set_facecolor(plb.cm.viridis(r/10.))
    bar.set_alpha(0.5)

# 区域图
fig.add_subplot(3,3,5)
from matplotlib import cm #cm用来上色
data = np.random.rand(2,3) #几行几列
cmap = cm.Blues # 色系
map = plb.imshow(data,interpolation='nearest',cmap=cmap,aspect='auto',vmax=1,vmin=0)

# 3D图
from mpl_toolkits.mplot3d import Axes3D
fig.add_subplot(3,3,6,projection='3d')
plb.scatter(1,2,s=100,c='red')

# 热力图
fig.add_subplot(3,1,3)
def f(x,y):
    return (1-x/2 + x ** 5 + y **3)* np.exp(-x**2-y**2)
n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)
plb.contourf(X,Y,f(X,Y),8,alpha = .75, cmap = plb.cm.hot)

# plb.savefig('name.png')   保存图
plb.show()

