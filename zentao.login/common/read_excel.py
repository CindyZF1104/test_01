import xlrd

class ExcelRead():
    def __init__(self,excelpath,sheetName="Sheet1"):
        self.data = xlrd.open_workbook(excelpath)#打开文件
        self.table = self.data.sheet_by_name(sheetName) #打开sheet
        self.keys = self.table.row_values(0) #以第一行作为key
        self.rowNum = self.table.nrows #获取行数
        self.colNum = self.table.ncols  #获取列数

    def dictData(self):
        if self.rowNum < 1:
            print("总行数小于1")
        else:
            r = []
            j=1
            for i in range (self.rowNum-1):
                s = {}
                values = self.table.row_values(j) #获取第二行数据
                for x in range (self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j +=1
            return r

if __name__ == "__main__":
    filepath = "C:\\Users\\test\\PycharmProjects\\zentao.login\\common\\data.xlsx"
    data = ExcelRead(filepath)
    exceldata = data.dictData()
    print(exceldata)



