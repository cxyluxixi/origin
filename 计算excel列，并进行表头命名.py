#!/usr/bin/env python
# coding: utf-8

# In[17]:


# 清洗excel特定的行
import xlrd
import pandas as pd
from pandas import DataFrame
import numpy as np
import xlsxwriter
import matplotlib.pyplot as plt

# E:\商采-绩效分析-供应链\比价-进价-跟进\python_dicai_test.xlsx

#打开一个excel文件
def open_xls(file):
    fh=xlrd.open_workbook(file)
    return fh

#获取excel中所有的sheet表
def getsheet(file):
#         获取第几个表 = fh.sheet_by_index(1) # sheet索引从0开始，
#         获取名称为""的表= fh.sheet_by_name('')
    return file.sheets() #在括号后写[?],表示想打开第几个sheet，如果想打开所有sheet，则去掉[?],

#获取sheet表的个数
def getshnum(fh):
    x=0
    sh=getsheet(fh)
    for sheet in sh:
        x+=1
    return x

# 读取每个表格的数据
def read_excel(file,shnum):
    fh=open_xls(file)
    table=fh.sheets()[shnum]
    num=table.nrows
    for row in range(num):
        rdata=table.row_values(row) #sheet里的第row行数据
        datavalue.append(rdata)     #datavalue，必须要全局定义，这样返回的就是所有文件的所有表格的所有数据，
    return datavalue                #datavalue 是个二维list，把所有sheet的行汇总到一个二维list里，

# 获取所有表格的所有数据
def getAllSheetsData(file_address_list):
    for fl in file_address_list:
        fh=open_xls(fl)
        x=getshnum(fh)
        for shnum in range(x):
            print("正在读取文件："+str(fl)+"的第"+str(shnum)+"个sheet表的内容...")
            rvalue=read_excel(fl,shnum) 
        return rvalue #rvalue是一个二维list

# 列表数据写入文件，定义最终合并后生成的新文件
def write_into_new_file(data,newFileName):
#     data是个list
    newfile=newFileName
    wb1=xlsxwriter.Workbook(newfile)
    #创建一个sheet工作对象
    ws=wb1.add_worksheet()
    for a in range(len(data)):
        for b in range(len(data[a])):
            c=data[a][b]
            ws.write(a,b,c)
    wb1.close()
    print("文件合并完成")
    return newfile

# 字典数据写入文件，数据清洗后，保存新文件
def write_sheet_into_new_file(data,newFileName):
    newfile=newFileName
#     data是个字典，包含一个或多个sheet表数据
    wb1=xlsxwriter.Workbook(newfile)
    #创建一个sheet工作对象
    ws=wb1.add_worksheet()
    print(data.keys)
    for key in data.keys():
#         data[key]是一个sheet表,二维list
        rows = len(data[key])
        for a in range(rows):
            for b in range(len(data[key][a])):
                c=data[key][a][b]
#                 print(c)
                ws.write(a,b,c)
    wb1.close()
    print("文件合并完成")
    return newfile

   
# pandas读取excel，生成df数据，开始准备清洗;
def read_excel_intoDataFrame(old_file):
    df_Excel_Data = pd.read_excel(file)
    print(df_Excel_Data.head())
    return df_Excel_Data


# 判断是否为数字，开始清洗特定的列的数据,两个参数
def washYourDataFrame(df,col_index_list,bool_choice):
#     sum_all_cols_NA_null = df.isnull().sum().sort_values(ascending=False)
    
#     去除该列数据的前后空格
#     df[col_index] = df[col_index].str.lstrip()
    error_loc_list = []
#     使用正则判断是不是数字或空白，是则pass，不是则反馈坐标，用户选择是否替换为空
    for col_index in col_index_list:
        for i in range(3,len(df[col_index])):
            if (df[col_index][i] is None) or (df[col_index][i] == ''):
                pass
            else:
                try:
                    float(df[col_index][i])
                    pass
                except:
                    if bool_choice == True:
                        df[col_index][i] = ''
                    else:
                        error_loc_list.append([i,col_index,df[col_index][i]]) #抛出非数字的异常值及其坐标，形成一个列表
    return df,error_loc_list


# pandas处理过的数据写入新的文件
def write_df_into_excel(data,new_file_address):
    writer = pd.ExcelWriter(new_file_address) 
    data.to_excel(writer,'test_luxixi_201910.21')  #第二个参数为sheet的命名
    writer.save()
    return writer 
 
    
# 转换时间戳
# def convert_str_datatime(df):
#     INPUT df 
#     OUTPUT  2019
#     df.insert(loc=时间行的index，column="timestamp",value=pd.to_datetime(df.transdatae,format="%Y-%m-%d %H:%M:%S.%f"))
    
# 替换表格L列（现进价），U列（最新进价）, 
# 匹配汉字,比如".*?([\u4E00-\u9FA5]+大学)
# def replace_row(data,col_index):
#     wait_for_replace =df.loc[['index1'],['列名1','列名2',"列名3"]] #想要替换的行和列
#     wait_for_replace =df.loc[]

# 画图
# def draw_data(df,col1,col2,row1,row2):
#     x = df_Excel_Data[col1][row1:row2]
#     y = df_Excel_Data[col2][row1:row2]
#     for m in x:
#         m = pd.to_numeric(m)       
#     for n in y:
#         n =  pd.to_numeric(n)
        
# #     t = plt.plot(x,y)
#     plt.figure(num=3,figsize=(8,5))
#     plt.plot(x,y,color='blue',linestyle='dashdot',label='单品sku进价下降趋势')
#     plt.xlabel('现进价[price_old]')
#     plt.ylabel('谈判后进价[price_new]')
#     ax=plt.gca()
#     ax.set_title('单品sku进价下降趋势',fontsize='16',color='black')
#     plt.show()

if __name__=='__main__':
################# 想打开的文件列表，list
    file_address = ["E:\商采-绩效分析-供应链\比价-进价-跟进\\dicai第一轮42周明细"] 
    datavalue = []
    rvalue = getAllSheetsData(file_address) #返回一个包含所有表所有行的data，二维list,所有值变成str
    ############ 直接合并生成明细表
#     newfile= write_into_new_file(rvalue,'E:\商采-绩效分析-供应链\比价-进价-跟进\\dicai第一轮42周明细.xlsx')


################## 想清洗合并后数据的特定列
     # washYourDataFrame 三个参数(1想清洗的数据源; 2.想清洗的列的index_list; 3是否替换为空，是替换，否抛出异常值坐标记录为文件）
    df_Excel_Data = pd.DataFrame(rvalue)
    df_Excel_Data,error_loc_list = washYourDataFrame(df_Excel_Data,[21,24,25],False)
    ############ 使用pandas——df，处理之后写入文件时，会增加列index，和行index，最左上角增加一行一列
    file_e = write_df_into_excel(df_Excel_Data,'E:\商采-绩效分析-供应链\比价-进价-跟进\df_Excel_data.xlsx')
    # 将异常值及其坐标写入新文件
    error_file = write_into_new_file(error_loc_list,'E:\商采-绩效分析-供应链\比价-进价-跟进\非数字的异常值-坐标.xlsx')
    
    
    
    
    
    
    # 画x-y的关系图，数据源，列1，列2，行1至行2
#     draw_data(df_Excel_Data,11,21,3,601)
   


# In[7]:





# In[ ]:




