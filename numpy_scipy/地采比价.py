import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from IPython.display import display

#  设置matplotlib inline
plt.style.use("fivethirtyeight")
sns.set_style({'font.sans-serif':['simhei','Arial']})
purchasePrice = pd.read_excel('/Users/luxixi/Downloads/pur.xlsx')
# display(purchasePrice.head())

# 查看了解数据表头，默认前十行
# purchasePrice.info()
# purchasePrice.describe()




