from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtWidgets


import sys
import excelgui  # Это наш конвертированный файл дизайна
import validator
import openexcelworker


class AppWindow(QtWidgets.QMainWindow, excelgui.Ui_MainWindow):
    file_name = ""

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.explorer = openexcelworker.ExcelWorker()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_file.clicked.connect(self.browseFile)
        self.pushButton_save.clicked.connect(self.execute)

    def browseFile(self):
        files = QtWidgets.QFileDialog()
        filter = "Excel files (*.xml *.xlsx *.xlsm *.xlsb *.xltx *.xltm *.xls *.xlt *.xlam *.xla *.xlw *.кслр)"
        directory = files.getOpenFileName(None, caption="Выберите файл", filter=filter)

        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории
        if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
             self.lineEdit_file.setText(directory[0])  # добавить файл в lineEdit

    def execute(self):
        if not self.validate():
            self.statusBar().show()
            return

        object = {"path": self.lineEdit_file.text(),
                  "worksheet": self.lineEdit_worksheet.text(),
                  "col1": self.lineEdit_col1.text(),
                  "col2": self.lineEdit_col2.text(),
                  "row1": self.lineEdit_row1.text(),
                  "row2": self.lineEdit_row2.text(),
                  "text": self.text.toPlainText()}

        message = self.explorer.execute(object)
        if message is None:
            self.statusBar().showMessage("Ячейки успешно заменены.")
        else:
            self.statusBar().showMessage(message)


    def validate(self):
        self.row1Validator = validator.Validator(self.lineEdit_row1,
                                                 self.pushButton_save,
                                                 self.statusbar)
        self.row1Validator.numberValidator()
        if not self.statusBarIsEmpty():
            return

        self.row2Validator = validator.Validator(self.lineEdit_row2,
                                                 self.pushButton_save,
                                                 self.statusbar,
                                                 self.lineEdit_row1)
        self.row2Validator.rowValidator()
        if not self.statusBarIsEmpty():
            return
        self.col1Validator = validator.Validator(self.lineEdit_col1,
                                                 self.pushButton_save,
                                                 self.statusbar)
        self.col1Validator.letterValidator()
        if not self.statusBarIsEmpty():
            return
        self.col2Validator = validator.Validator(self.lineEdit_col2,
                                                 self.pushButton_save,
                                                 self.statusbar,
                                                 self.lineEdit_col1)
        self.col2Validator.colValidator()
        if not self.statusBarIsEmpty():
            return

        return self.row1Validator.isValid() or \
               self.row2Validator.isValid() or \
               self.col1Validator.isValid() or \
               self.col2Validator.isValid()

    def statusBarIsEmpty(self):
        return self.statusBar().currentMessage() == ""




if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = AppWindow()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)