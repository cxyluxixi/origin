
# -*- coding: utf-8 -*-
import xlrd
import xlwt
import sys

def read(file_list,):

    # 创建新的workbook
    out_work_book = xlwt.Workbook(encoding = 'utf-8')
    # 为了将多个文件的相同表头的sheet和并到一个sheet内，定义新sheet写入的行号位置
    out_work_book_rows = [0,0]

    # 取得传入的文件列表 （第一个参数为脚本名字）
    for file_name in file_list[1:]:
        # 打开文件
        workbook = xlrd.open_workbook(file_name)
        # 取得当前文档的sheet列表
        sheet_names = workbook.sheet_names()


        for sheet_idx in range(len(sheet_names)):
            sheet_name = sheet_names[sheet_idx]
            
            # sheet = workbook.sheet_by_index(sheet_idx)
            sheet = workbook.sheet_by_name(sheet_name)

            # sheet.row_values(n)   获取整行数据
            # sheet.col_values(n)   获取整列数据

            # 获取行数
            rows_count = sheet.nrows
            # 获取列数
            cols_count = sheet.ncols
            # 存储写入的列数
            write_col_count

            # 创建新的sheet
            if len(out_work_book_sheet) <= sheet_idx:
                out_work_book_sheet[sheet_idx] = out_work_book.add_sheet('sheet'+sheet_idx)

            # 写入sheet
            for curr_col_num in range(cols_count):
                # 当前列的内容
                col = sheet.col_values(curr_col_num)
                # 遍历当前列的所有选项
                for index in range(len(col)):
                    # 当前列第index的内容
                    value = col[index]
                    # 在写入的sheet的行号上，加入上一个表写到的位置行号，继续向后追加内容
                    out_work_book_sheet[sheet_idx].write(out_work_book_rows[sheet_idx] + index, write_col_count, value)
                write_col_count++
            out_work_book_rows[sheet_idx] += cols_count
    # 输出目标文件
    out_work_book.save('out.xls')

    
# 如何处理合并单元格数据的自动补充
def get_merged_cells_value(sheet, row_index, col_index):

    # 获得当前sheet的所有合并单元格数据
    merged = sheet.merged_cells
    # 判断给定的单元格，是否属于合并单元格，如果是合并单元格，就返回合并单元格的内容
    for (rlow, rhigh, clow, chigh) in merged:
        if (row_index >= rlow and row_index < rhigh):
            if (col_index >= clow and col_index < chigh):
                cell_value = sheet.cell_value(rlow, clow)
                return cell_value
    return None



# 单元格里数据类型不同如何处理
from datetime import datetime,date

def get_merged_cells_value(workbook, sheet, row_index, col_index):

    # 获得当前sheet的所有合并单元格数据
    merged = sheet.merged_cells
    # 判断给定的单元格，是否属于合并单元格，如果是合并单元格，就返回合并单元格的内容
    for (rlow, rhigh, clow, chigh) in merged:
        if (row_index >= rlow and row_index < rhigh):
            if (col_index >= clow and col_index < chigh):

                if sheet.cell(rlow, clow).ctype == 3:
                    date_value = xlrd.xldate_as_tuple(sheet.cell(rlow, clow), workbook.datemode)
                    # 转换显示格式为2019/05/05
                    cell_value = date(*date_value[:3]).strftime('%Y/%m/%d')
                else:
                    cell_value = sheet.cell_value(rlow, clow)
                
                return cell_value
    return None

if __name__ == "__main__":
    read(file_list)
