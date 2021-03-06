# import pandas as pd
# import numpy as np
# import matplotlib as plt
# df = pd.DataFrame(np.random.randn(1000, 4), index=range(0,1000),columns=['A', 'B', 'C', 'D'])
# df = df.cumsum()
# df.plot()
# plt.figure()




import xlrd
import pandas as pd
from pandas import DataFrame
import numpy as np
import xlsxwriter
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor


def Q_purchase_price_difference(old_price,new_price):
    try:
        if new_price ==None or (old_price - new_price)<0:
            return None
        else:
            jiagecha = old_price - new_price
            return jiagecha
    except:
        return None
def P_purchase_price_difference(old_price,new_price):
    try:
        if new_price ==None or((new_price-old_price)<0):
            return None
        else:
            jiagecha = new_price-old_price
            return jiagecha
    except:
        return None
    
def eachSKU_gross_profit(grossProfit,saleAmount):
    try:
        if (grossProfit ==None) or (saleAmount ==None):
            return "None"
        else:
            eachSku_gross_profit_money = pd.to_numeric(grossProfit)/pd.to_numeric(saleAmount)
            return eachSku_gross_profit_money
    except:
        return 'xx'
def eachSKU_gross_profit_rate(Molecular,denominator):
    try:
        if (Molecular ==None) or (denominator ==None):
            return "None"
        else:
            eachSku_gross_profit_rate = pd.to_numeric(Molecular)/pd.to_numeric(denominator)
            return eachSku_gross_profit_rate
    except:
        return 'xx'

def evaluate_new_columns(file_address):
    xls_file = file_address
    df = pd.read_excel(xls_file,index_cols=0)
    print(df.columns)
    df['合并码'] = df.apply(lambda df: df['企业']+str(df['国条码']),axis = 1)
    df['价格差']= df.apply(lambda df: Q_purchase_price_difference(df['现进价'], df['谈判后采最新进价：元（开票价）']),axis = 1)
    df['返利差']= df.apply(lambda df: P_purchase_price_difference(df['谈判前（不填任何文字,  返利金额：元,  折算到单盒）'], df['谈判后（不填任何文字,  返利金额：元,  折算到单盒）']),axis = 1) 
    df['周原采购成本']=None
    df['降本率']=None
    print(df.columns)
    file = file_address
    df.to_excel(file_address,index=False)
    return file

    

def vlookup_amount_sale(file1,file2,file3):
    df1 = pd.read_excel(file1,index_cols=0)
    df2 = pd.read_excel(file2,index_cols=0)
    df2 = df2.rename(columns={"行标签":"合并码","地采":"地采销售数量"})
    df3 = pd.read_excel(file3,index_cols=0)
    df3 = df3.rename(columns={"行标签":"企业","地采":"地采销售额","总计":"全品销售额"})
    df = pd.merge(df1,df2.loc[:,["合并码","地采销售数量"]],left_on=["合并码"],right_on = ["合并码"],how='left',sort=False)
    df["周综合成本收益"]=None
    df["收益率（对地采）"]=None
    df["收益率（对全品）"]=None
    df5 = pd.merge(df,df3.loc[:,["企业","地采销售额","全品销售额"]],left_on = ["企业"],right_on=["企业"],how='left',sort=False)
    df5 = df5.reset_index(drop=True)
    print(df5.columns)
#     df5['标识']=df5.apply
#     df5['价格差返利差异常值标识']=df5.apply

    return df5
    

def draw_figure(file_address):
    data = pd.read_excel(file_address,index_cols=0)
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    df = pd.DataFrame(data)
    # col_names = df.iloc[1,:]
    # df = df.rename(columns=col_names)
    # df.drop(index=[0,1],axis=0,inplace = True)

    print(df.columns)
    
    x =pd.to_numeric(df["现进价"])
    y =pd.to_numeric(df['谈判后采最新进价：元（开票价）'])
    result = pd.concat([x,y],axis=1,names=["谈判前进价","谈判后进价"])
    print(result)
    result.plot()
    plt.figure()
    
if __name__ == "__main__":
    lunshu= 3
    zhoushu = 45
    file_address = r"D:\商采-绩效分析-供应链\比价-进价-跟进\test\py第{}轮地采明细汇总_{}周.xlsx".format(lunshu,zhoushu)
#     file = evaluate_new_columns(file_address)

    file1 = evaluate_new_columns(file_address)
#     file2应为，周销售数量明细透视，表头"合并码","销售数量"]
    file2 = r"D:\商采-绩效分析-供应链\比价-进价-跟进\test\周销售数量透视-地采企业级.xlsx"
#     file3应为，周销售额-地采全品透视，表头["企业","地采","总计"]]
    file3 = r"D:\商采-绩效分析-供应链\比价-进价-跟进\test\周销售额透视-地采全品.xlsx"
    df = vlookup_amount_sale(file1,file2,file3)
    df.to_excel(r'D:\商采-绩效分析-供应链\比价-进价-跟进\test\收益核算{0}_{1}周-所有列已匹配.xlsx'.format(lunshu,zhoushu),sheet_name = "收益核算{0}_{1}周".format(lunshu,zhoushu),index=False,)
    print("over")
    
    



