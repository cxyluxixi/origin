import pandas as pd 

def split_test(wait_splitFile_address,split_col_1,split_col_2):
    xls_file = wait_splitFile_address
    data = pd.read_excel(xls_file, 0)
    rows = data.shape[0]  # 获取行数 shape[1]获取列数
    department_dict = {} #平台和企业列表
    department_list = [] #平台列表
    for i in range(rows):
        temp = data[split_col_1][i]
        key = data[split_col_2][i]
        if temp not in department_list:
            department_list.append(temp)  # 将分类存在一个列表中
            department_dict[temp] = [key]  # 建立分类字典
        else:
            # 分类字典添加数据
            key_list = department_dict[temp]
            key_list.append(key)
            department_dict[temp] = key_list
    print(len(department_list), rows, len(department_dict))
 
    # for di in department_dict:
    #     print di, department_dict[di]
    ret_data =  {'list': department_list, 'dict': department_dict}
    split_work = {"xls_file": r"D:\商采-绩效分析-供应链\比价-进价-跟进\\dicai第二轮43周明细.xlsx", "xls_fld1":split_col_2 , "file_head": split_col_1, "dir": "D:\商采-绩效分析-供应链\比价-进价-跟进"}
    split_work['dict_list'] = ret_data['dict']
    split_work['file_list'] = ret_data['list']  #平台
 
    xls_file = split_work['xls_file']
    fld_key = split_work['xls_fld1']
 
    # 工作表数量
    xl = pd.ExcelFile(xls_file)
    xls_sheet_len = len(xl.sheet_names)
 
    # 获取平台列表、机构代码名称对应表、平台字典
    department_list = split_work['file_list']
    department_dict = split_work['dict_list']
    print(department_list)
    print(department_dict)
    # 按分类遍历数据、写入数据
    work_info = []
    for department in department_list:
        print(department)
        file_name = u"{0}\{1}{2}.xlsx".format(split_work['dir'], split_work['file_head'], department)
        work_item = [department, file_name]
        xls_save_file = pd.ExcelWriter(file_name)
        # 遍历工作表
        for sheet_i in range(xls_sheet_len):
            data = pd.read_excel(xls_file, sheet_i)
            rows = data.shape[0]  # 获取行数 shape[1]获取列数
            new_df = pd.DataFrame()
            # 遍历行，筛选数据
            for i in range(0, rows):
                if data[fld_key][i] in department_dict[department]:
                    new_df = pd.concat([new_df, data.iloc[[i], :]], axis=0, ignore_index=True)
            # 写入工作表
            work_item.append(len(new_df))
            new_df.to_excel(xls_save_file, sheet_name=xl.sheet_names[sheet_i], index=False)
        # 保存文件
        xls_save_file.save()
        work_info.append(work_item)
        for w in work_item:
            print(w)
        print("完成")
        
if __name__ == '__main__':
#     第一个参数是需要拆分的目标文件，第二参数是按照哪一些拆分，第三个是所有要填入第二个参数的列的行
    split_test('D:\商采-绩效分析-供应链\比价-进价-跟进\\dicai第二轮43周明细.xlsx','平台','企业')
