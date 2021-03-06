# 清洗excel特定的行
import xlrd
# import pandas as pd
# from pandas import DataFrame
# import numpy as np
import xlsxwriter


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
def read_excelData(file,shnum):
    fh=open_xls(file)
    table=fh.sheets()[shnum]
    num=table.nrows
    for row in range(num):
        rdata=table.row_values(row)
        datavalue.append(rdata)
    return datavalue

# 获取所有表格的所有数据
def getAllSheetsData(file_address_list):
    for fl in file_address_list:
        fh=open_xls(fl)
        x=getshnum(fh)
        for shnum in range(x):
            print("正在读取文件："+str(fl)+"的第"+str(shnum)+"个sheet表的内容...")
            rvalue=read_excelData(fl,shnum)
    return rvalue #rvalue是一个list

#定义最终合并后生成的新文件
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

# sheet1格式处理之后，保存新文件
def write_sheet_into_new_file(data,newFileName):
    newfile=newFileName
#     data是个字典，包含一个或多个sheet表数据
    wb1=xlsxwriter.Workbook(newfile)
    #创建一个sheet工作对象
    ws=wb1.add_worksheet()
    for a in data.keys():
        for b in range(len(data[a])):
            for c in range(len(data[a][b])):
                d = data[a][b][c]
                print(d)
                ws.write(b,c,d)
    wb1.close()
    print("文件合并完成")
    return newfile

# 统一表格的数据格式
def set_sheet_type(filename):
    all_content = {} #定义一个字典用于装纳不同sheet的值
#     如果是C数据文件，则filename = filename.decode('utf-8')
    print(filename)
#     filename = filename.decode('utf-8')
    #打开一个EXCEL对象
    rbook = xlrd.open_workbook(filename)
    #获取excel的sheet个数
    sheetnum = rbook.sheets().__len__()
    for i in range(sheetnum):
        #通过下标的方式获取对应的sheet
        sheet = rbook.sheet_by_index(i)

        rows = sheet.nrows#获取当前sheet的行数
        cols = sheet.ncols#获取当前sheet的列数
        for i in range(rows):
            row_content = []
            for j in range(cols):
                ctype = sheet.cell(i, j).ctype  # 表格的数据类型
                cell = sheet.cell_value(i, j)
                if ctype == 2 and cell % 1 == 0:  # 如果是整形
                    cell = int(cell)
                elif ctype == 3 and (61 < int(cell) < 2958466): #源码中此处有限制,如Python规定日期会抛出异常
                    # 转成datetime对象
                    date = datetime(*xldate_as_tuple(cell,0))
                    cell = date.strftime('%Y%m%d')
                elif ctype == 3 and (int(cell) >= 2958466 or int(cell) <= 61 ):
                    cell = int(cell)
                elif ctype == 4:
                    cell = True if cell == 1 else False

                row_content.append(cell)

            key = str(sheet.name)#获取当前sheet的名称
            if key in all_content.keys():
                all_content[key].append(row_content)
            else:
                all_content[key] = [row_content]
#     print(all_content.ctype) 是个字典，dict
    return write_sheet_into_new_file(all_content,'E:\\商采-绩效分析-供应链\\比价-进价-跟进\\格式合并第一轮地采42周.xlsx')
    
    
# pandas读取excel，生成df数据，开始准备清洗
def read_excel_intoDataFrame(file):
    df = pd.read_excel(file)
    print(df.head())
    

# 检查df中缺失的数据
def check_missing_data(df):
    return df.isnull().sum().sort_values(ascending=False)

# 删除数据矩阵中的前后的空格
def remove_col_white_space(df):
    df[col] = df[col].str.lstrip()
    
# 转换时间戳
# def convert_str_datatime(df):
#     INPUT df 
#     OUTPUT  2019
#     df.insert(loc=时间行的index，column="timestamp",value=pd.to_datetime(df.transdatae,format="%Y-%m-%d %H:%M:%S.%f"))
    
# 替换表格L列（现进价），U列（最新进价）
# def replace_row(df):
#     wait_for_replace =df.loc[[哪几行用index写],['列名1','列名2',"列名3"]] #想要替换的行和列
#     wait_for_replace =df.loc[]
    
          
if __name__=='__main__':
    file_address = ["E:\商采-绩效分析-供应链\比价-进价-跟进\python第一轮地采汇总xxx.xlsx"] # 想打开的文件名，一次处理一个表
    datavalue = []
    rvalue = getAllSheetsData(file_address) #返回一个包含所有表所有行的data
    newfile = write_into_new_file(rvalue,'E:\商采-绩效分析-供应链\比价-进价-跟进\\dicai第一轮42周明细.xlsx')
#     import pandas as pd
#     df = pd.DataFrame.from_dict(order_dict,orient='index',columns=['file_path'])
#     df = df.reset_index().rename(columns = {'index':'order_num'})
#     writer = pd.ExcelWriter(r'C:\Users\User\Desktop\test.xlsx')
    set_sheet_type(newfile)
