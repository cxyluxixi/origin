import pandas as pd 

def split_test(wait_splitFile_address,split_col_1,split_col_2):
    xls_file = wait_splitFile_address
    xl = pd.ExcelFile(xls_file)
    xls_sheet_len = len(xl.sheet_names)
    for x in range(xls_sheet_len):
        data = pd.read_excel(xls_file, x)
        rows = data.shape[0]  # 获取行数 shape[1]获取列数
        department_dict = {} #平台和企业列表
        department_list = [] #平台列表
        company_list = []
        for i in range(rows):
            stage = data[split_col_1][i]
            company = data[split_col_2][i]
            if company not in company_list:  
                company_list.append(company)
                if stage not in department_list:
                    department_list.append(stage)# 将分类存在一个列表中
                    department_dict[stage] = [company]  # 建立分类字典
                else:
                    # 分类字典添加数据
                    key_list = department_dict[stage]
                    key_list.append(company)
                    department_dict[stage] = key_list
            else:
                if stage not in department_list:
                    department_list.append(stage)# 将分类存在一个列表中
                    department_dict[stage] = [company]  # 建立分类字典
                else:
                    pass
    #                 # 分类字典添加数据
    #                 key_list = department_dict[stage]
    #                 key_list.append(company)
    #                 department_dict[stage] = key_list
        print(company_list)
        print(department_dict)


        ret_data =  {'list': department_list, 'dict': department_dict}
        split_work = {"xls_file": wait_splitFile_address, "xls_fld1": split_col_2,"xls_fld2":split_col_1, "file_head": u"拆分", "dir": "D:\商采-绩效分析-供应链\比价-进价-跟进"}
        split_work['dict_list'] = ret_data['dict'] #平台：企业
        split_work['file_list'] = ret_data['list'] #平台

        xls_file = split_work['xls_file']
        # fld_key = split_work['xls_fld1']

        # 工作表数量
        xl = pd.ExcelFile(xls_file)
        xls_sheet_len = len(xl.sheet_names)

        # 获取平台列表、机构代码名称对应表、平台字典
        department_list = split_work['file_list']
        department_dict = split_work['dict_list']
    #     print(department_list)
    #     print(department_dict)
        # 按分类遍历数据、写入数据
        depa_drop = split_work['file_list']
        work_info = []
        for department in department_dict:
            data2 = data[data[split_col_1].isin([department])]
            comp_drop = department_dict[department]
            for company in department_dict[department]:
                print(company)
                file_name = u"{0}/{1}{2}{3}.xlsx".format(split_work['dir'], split_work['file_head'],department,company)
                work_item = [department, file_name]
                xls_save_file = pd.ExcelWriter(file_name)

    #             方法1 
    #             遍历工作表
    #             for sheet_i in range(xls_sheet_len):
    #                 data = pd.read_excel(xls_file, sheet_i)
    #                 rows = data.shape[0]  # 获取行数 shape[1]获取列数
    #                 new_df = pd.DataFrame()
    #                 # 遍历行，筛选数据
    #                 for i in range(0, rows):
    #                     if data[fld_key][i] == company :
    #                         new_df = pd.concat([new_df, data.iloc[[i], :]], axis=0, ignore_index=True)
    #                 # 写入工作表
    #                 work_item.append(len(new_df))
    #                 new_df.to_excel(xls_save_file, sheet_name=xl.sheet_names[sheet_i], index=False)
    #             # 保存文件
    #             xls_save_file.save()
    #             work_info.append(work_item)
    #             for w in work_item:
    #                 print(w)
    #             print("完成")


    #            方法2 
                if depa_drop ==[]:
                    pass
                else:
                    new_df = data2[data2[split_col_2].isin([company])]
                    print(len(new_df))
                    work_item.append(len(new_df))
                    new_df.to_excel(xls_save_file, sheet_name=xl.sheet_names[x], index=False)

                # 删除已处理过的数据，缩小data2
                comp_drop.remove(company)
                print(comp_drop)
                data2 = data2[~data2[split_col_2].isin([comp_drop])]
                # 保存文件
                xls_save_file.save()
                work_info.append(work_item)
                for w in work_item:
                    print(w)
                    print('这个公司搞完了')
            print("这个平台搞完了")
        print('over')
            
        
if __name__ == '__main__':
    split_test("D:\商采-绩效分析-供应链\\10月21日淘汰库存-相关信息确认.xlsx",'平台','企业')
