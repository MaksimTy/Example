import openpyxl

class ExcelException(Exception):
   pass

class ExcelWorker:

    def execute(self, object):
        try:
            wb = openpyxl.reader.excel.load_workbook(object["path"])
        except Exception:
            try:
                raise ExcelException("Файл не найден.")
            except ExcelException as e:
                return "Ошибка: " + str(e)
        try:
            if wb is not None:
                self.getWb(object, wb)
        except Exception:
            try:
                raise ExcelException("Рабочий лист не найден.")
            except ExcelException as e:
                return "Ошибка: " + str(e)


    def getWb(self, object, wb):
        if object["worksheet"] == '':
            sheet = wb.active
            object["worksheet"] = sheet.title
        else:
            sheet = wb.get_sheet_by_name(object["worksheet"])
        leftIndex = "{}{}".format(object["col1"], object["row1"])
        rightIndex = "{}{}".format(object["col2"], object["row2"])
        cell_range = sheet[leftIndex:rightIndex]
        for cell in cell_range:
            cell[0].value = object["text"]
        wb.save(object["path"])
        wb.close()
