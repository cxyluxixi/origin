import pandas as pd 
# 缺失值处理：na_values=
# na_values= ["null"]，用null字符替换缺失值。
df1 = pd.read_csv("ML-housePrice/train.csv",  na_values= ["null"])
print(df1.index,df1.index.name,df1.columns)

# 尝试将数据解析为日期：
# parse_dates = True，尝试解析所有可能为日期类型的列。
df2 = pd.read_csv("ML-housePrice/train.csv",  parse_dates = True)
print(df2.columns)
# parse_dates = [1, 2]，尝试解析给定列为日期类型的列。
df3 = pd.read_csv("ML-housePrice/train.csv",  parse_dates = [1, 2])
print(df3.dtypes)


# df的方法:
'''
describe(),head(),
sort_value(),sort_index(),
value_counts(), unique(),mean(),plot()
'''


# df 列重命名：
df1.columns = df1.columns.str.replace('xx', 'xxx')
pd.read_csv('data', names = new_cols_names, header=0)
df1.rename(columns = {"old1": "new1", "old2":"new2"},  inplace=True) 
#inplace参数表示，是否替换原df，还是保存赋值给新变量



# df 删除
df1.drop('column_name',axis=1)
df1.drop('row_index')#axis默认为0


# df 排序
df1.sort_index(axis=0/1)#0水平方向（给列排左右），1垂直方向（给行排上下）
# 单独排一列（这一列作为series），返回series
df1.colname.sort_values()
df1.colname.sort_values(ascending = False)
df1["colname"].sort_values()
df1["colname"].sort_values(ascending = False)
# 根据某些列的值排序，并扩展到其他区域，一行为一个整体一起移动
df1.sort_values(['column1','column2',])



# 字符串操作
df1.column.str.upper/contains/replace/strip/rstrip/lstrip




# 变更数据类型
df1.column.astype('newtype')
pd.read_csv('data',dtype={'column_name':newtype})
