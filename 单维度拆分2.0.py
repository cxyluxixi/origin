import time
import pandas as pd 

def split_test(wait_splitFile_address,split_col_1,split_col_2):
    xls_file = wait_splitFile_address
    # 工作表数量
    xl = pd.ExcelFile(xls_file)
    xls_sheet_len = len(xl.sheet_names)
    for x in range(xls_sheet_len):
        data = pd.read_excel(xls_file, x)
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
        split_work = {"xls_file": wait_splitFile_address, "xls_fld1":split_col_1 , "file_head": split_col_1, "dir": "D:"}
        split_work['dict_list'] = ret_data['dict']
        split_work['file_list'] = ret_data['list']  #平台

        xls_file = split_work['xls_file']
        fld_key = split_work['xls_fld1']

        # 获取平台列表、机构代码名称对应表、平台字典
        department_list = split_work['file_list']
        department_dict = split_work['dict_list']
    #     print(department_list)
    #     print(department_dict)
        #备份平台列表，用于删除已读写过的行，见“循环”最后面的几行

        # 按分类遍历数据、写入数据
        work_info = []
        # 遍历工作表
        data2= pd.read_excel(xls_file, x)
        depa_drop = split_work['file_list'] 

        for department in department_list:
            print(department)
            file_name = u"{0}\{1}{2}{3}.xlsx".format(split_work['dir'], split_work['file_head'], department,x)
            work_item = [x,department, file_name]
            xls_save_file = pd.ExcelWriter(file_name)
            if depa_drop ==[]:
                pass
            else:

    # 方法1 ：遍历工作表
    #         for sheet_i in range(xls_sheet_len):
    #             data = pd.read_excel(xls_file, sheet_i)
    #             rows = data.shape[0]  # 获取行数 shape[1]获取列数
    #             new_df = pd.DataFrame()
    #             # 遍历行，筛选数据
    #             for i in range(0, rows):
    #                 if data[fld_key][i] == department_dict[department]:
    #                     new_df1 = pd.concat([new_df, data.iloc[[i], :]], axis=0, ignore_index=True)
    #             # 写入工作表
    #             work_item.append(len(new_df))
    #             new_df.to_excel(xls_save_file, sheet_name=xl.sheet_names[sheet_i], index=False)
#             # 保存文件
#             xls_save_file.save()
#             work_info.append(work_item)
#             for w in work_item:
#                 print(w)
#         print("完成")


    # 方法2 ： 每次遍历一类平台之后，删除已处理过的行，缩小data2
#                 rows = data2.shape[0]  # 获取行数 shape[1]获取列数
#                 print(rows)
#                 new_df = pd.DataFrame()
#                 for index,row in data2.iterrows():
#                     if row[fld_key] == department:
                        # 这里特别注意，iloc用的是位置（数字) , loc用的是列名，行名或数字
                        # new_df = pd.concat([new_df,data2.loc[[index], :]], axis=0, ignore_index=True)
#                     else:
#                         pass

#                 # 写入工作表
#                 print(len(new_df))
#                 work_item.append(len(new_df))
#                 new_df.to_excel(xls_save_file, sheet_name=xl.sheet_names[sheet_i], index=False)

#                 # 删除已处理过的数据，缩小data2
#             depa_drop.remove(department)
#             print(depa_drop)
#             data2 = data2[data2['平台'].isin(depa_drop)]
#             print(data2.head)
#             # 保存文件
#             xls_save_file.save()
#             work_info.append(work_item)
#             for w in work_item:
#                 print(w)
#         print("完成")


    # 方法3：
                new_df = data2[data2[split_col_1].isin([department])]
                print(len(new_df))
                work_item.append(len(new_df))
                new_df.to_excel(xls_save_file, sheet_name=xl.sheet_names[x], index=False)
            
            # 删除已处理过的数据，缩小data2
            depa_drop.remove(department)
            print(depa_drop)
            data2 = data2[data2[split_col_1].isin(depa_drop)]
            # 保存文件
            xls_save_file.save()
            work_info.append(work_item)
            for w in work_item:
                print(w)
        print("完成")
        
if __name__ == '__main__':
#     第一个参数是需要拆分的目标文件，第二参数是按照哪一些拆分，第三个是所有要填入第二个参数的列的行
    since = time.time()
    split_test("D:\商采-绩效分析-供应链\\10月21日淘汰库存-相关信息确认.xlsx",'平台','平台')
    # 程序执行部分
    ...
    ...
    time_elapsed = time.time() - since
    print('Training complete in {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed % 60))
