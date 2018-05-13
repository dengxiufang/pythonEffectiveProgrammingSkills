#coding:utf8
# 如何读写 excel 文件


# 使用第三方库 xlrd  xlwt

#import xlrd

#book = xlrd.open_workbook('fifth_example/demo.xlsx')

#sheet = book.sheet_by_index(0)


# 行列
#print(sheet.nrows)
#print(sheet.ncols)

# 获取第一行第一格
#cell = sheet.cell(0,0)

# 获取了第一行的数据
#print(sheet.row_values(1,1))

# 添加一格
#sheet.put_cell()


#import xlwt

#wbook = xlwt.Workbook()


# 实际案例
import xlrd, xlwt

rbook = xlrd.open_workbook('fifth_example/demo.xlsx')
rsheet = rbook.sheet_by_index(0)

nc = rsheet.ncols
rsheet.put_cell(0, nc, xlrd.XL_CELL_TEXT, u'总分', None)

for row in range(1, rsheet.nrows):
    t = sum(rsheet.row_values(row, 1))
    rsheet.put_cell(row, nc, xlrd.XL_CELL_NUMBER, t, None)


wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)
style = xlwt.easyxf('align: vertical center, horizontal center')

for r in range(rsheet.nrows):
    for c in range(rsheet.ncols):
        wsheet.write(r, c, rsheet.cell_value(r, c), style)

wbook.save('fifth_example/output.xlsx')
