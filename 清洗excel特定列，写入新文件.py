#!/usr/bin/env python
# coding: utf-8

# In[19]:


# 清洗excel特定的行，判断价格列是否为数字，判断国条码是否为空
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
        print(df[col_index])
        
######### 从第几行开始，就把3改为几，注意保护表头
        for i in range(3,len(df[col_index])):
            if (pd.isnull(df[col_index][i])) or (df[col_index][i] == '') or (pd.isna(df[col_index][i])):
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


#判断有无国条码,或编码
def wash_sku_id(df,id_col_index_list,replace_string_list):
#     print(id_col_index_list,replace_string_list)
    for i in id_col_index_list:
        for n in range(3,len(df[i])):
            if(pd.isnull(df[i][n])) or (pd.isna(df[i][n])) or df[i][n]=='':
                df[i][n] = replace_string_list[0]
            else:
                print(df[i][n])
                
    return df
    

# pandas处理过的数据写入新的文件
def write_df_into_excel(data,new_file_address):
    writer = pd.ExcelWriter(new_file_address) 
    data.to_excel(writer,'清洗69码和每一列的格式')  #第二个参数为sheet的命名
    writer.save()
    return writer 
 
    


if __name__=='__main__':
################# 想清洗的文件列表，list
    file_address = ["D:\商采-绩效分析-供应链\比价-进价-跟进\\dicai第二轮43周明细.xlsx"] 
    datavalue = []
    rvalue = getAllSheetsData(file_address) #返回一个包含所有表所有行的data，二维list,所有值变成str

################## 想清洗数据的特定列，本文件只判断是否为数字
     # washYourDataFrame 三个参数(1想清洗的数据源; 2.想清洗的列的index_list; 3是否替换为空，是替换，否抛出异常值坐标记录为文件）
    df_Excel_Data = pd.DataFrame(rvalue)
    print(df_Excel_Data.head())
    df_Excel_Data = wash_sku_id(df_Excel_Data,[5],['xxx'])
    print(df_Excel_Data)
    df_Excel_Data,error_loc_list = washYourDataFrame(df_Excel_Data,[21,24,25],False) #21是谈判后进价，24是谈判前返利，25是谈判后返利
    # 将异常值及其坐标写入新文件
    if error_loc_list == []:
        pass
    else:
        error_file = write_into_new_file(error_loc_list,'D:\商采-绩效分析-供应链\比价-进价-跟进\非数字的异常值-坐标.xlsx')        
    ############## 处理之后的df_Excel_Data写入文件时，会增加列index，和行index，最左上角增加一行一列
#         print(error_file)
    file_e = write_df_into_excel(df_Excel_Data,'D:\商采-绩效分析-供应链\比价-进价-跟进\df_Excel_data_xx周.xlsx')
    
