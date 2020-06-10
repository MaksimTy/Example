# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exceleditor.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 302)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src\main\icons\Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTipDuration(-4)
        MainWindow.setStyleSheet("\n"
"QPushButton {\n"
"    font-weight: bold;\n"
"    padding: .375rem 1rem;\n"
"    @include transition (all 0.4s ease-in-out);\n"
"}\n"
"\n"
"QPushButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"}\n"
"")
        MainWindow.setIconSize(QtCore.QSize(24, 23))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_file = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_file.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_file.setObjectName("pushButton_file")
        self.horizontalLayout.addWidget(self.pushButton_file)
        spacerItem = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit_file = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_file.sizePolicy().hasHeightForWidth())
        self.lineEdit_file.setSizePolicy(sizePolicy)
        self.lineEdit_file.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineEdit_file.setObjectName("lineEdit_file")
        self.horizontalLayout.addWidget(self.lineEdit_file)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(100, 20))
        self.label.setMaximumSize(QtCore.QSize(100, 20))
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        self.label.setBaseSize(QtCore.QSize(100, 20))
        self.label.setTabletTracking(True)
        self.label.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label.setToolTip("")
        self.label.setToolTipDuration(0)
        self.label.setAutoFillBackground(False)
        self.label.setMidLineWidth(5)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lineEdit_worksheet = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_worksheet.sizePolicy().hasHeightForWidth())
        self.lineEdit_worksheet.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.lineEdit_worksheet.setPalette(palette)
        self.lineEdit_worksheet.setObjectName("lineEdit_worksheet")
        self.horizontalLayout_2.addWidget(self.lineEdit_worksheet)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(3, 3, -1, 3)
        self.gridLayout.setObjectName("gridLayout")
        self.text = QtWidgets.QTextEdit(self.centralwidget)
        self.text.setReadOnly(False)
        self.text.setPlaceholderText("")
        self.text.setObjectName("text")
        self.gridLayout.addWidget(self.text, 1, 1, 2, 2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_col = QtWidgets.QLabel(self.centralwidget)
        self.label_col.setMinimumSize(QtCore.QSize(41, 0))
        self.label_col.setBaseSize(QtCore.QSize(30, 20))
        self.label_col.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label_col.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_col.setObjectName("label_col")
        self.horizontalLayout_9.addWidget(self.label_col)
        self.lineEdit_col1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_col1.setMinimumSize(QtCore.QSize(60, 0))
        self.lineEdit_col1.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_col1.setBaseSize(QtCore.QSize(70, 20))
        self.lineEdit_col1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_col1.setAutoFillBackground(False)
        self.lineEdit_col1.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.lineEdit_col1.setMaxLength(15)
        self.lineEdit_col1.setCursorPosition(0)
        self.lineEdit_col1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lineEdit_col1.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_col1.setObjectName("lineEdit_col1")
        self.horizontalLayout_9.addWidget(self.lineEdit_col1, 0, QtCore.Qt.AlignLeft)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        self.lineEdit_col2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_col2.setMinimumSize(QtCore.QSize(60, 0))
        self.lineEdit_col2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_col2.setBaseSize(QtCore.QSize(70, 20))
        self.lineEdit_col2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_col2.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.lineEdit_col2.setMaxLength(15)
        self.lineEdit_col2.setCursorPosition(0)
        self.lineEdit_col2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lineEdit_col2.setObjectName("lineEdit_col2")
        self.horizontalLayout_9.addWidget(self.lineEdit_col2)
        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_row = QtWidgets.QLabel(self.centralwidget)
        self.label_row.setBaseSize(QtCore.QSize(30, 20))
        self.label_row.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label_row.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_row.setAutoFillBackground(False)
        self.label_row.setObjectName("label_row")
        self.horizontalLayout_10.addWidget(self.label_row, 0, QtCore.Qt.AlignLeft)
        self.lineEdit_row1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_row1.setMinimumSize(QtCore.QSize(60, 0))
        self.lineEdit_row1.setMaximumSize(QtCore.QSize(57, 16777215))
        self.lineEdit_row1.setBaseSize(QtCore.QSize(70, 20))
        self.lineEdit_row1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_row1.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_row1.setMaxLength(15)
        self.lineEdit_row1.setObjectName("lineEdit_row1")
        self.horizontalLayout_10.addWidget(self.lineEdit_row1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_10.addWidget(self.label_2)
        self.lineEdit_row2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_row2.setMinimumSize(QtCore.QSize(60, 0))
        self.lineEdit_row2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_row2.setBaseSize(QtCore.QSize(70, 20))
        self.lineEdit_row2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_row2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_row2.setAutoFillBackground(False)
        self.lineEdit_row2.setMaxLength(15)
        self.lineEdit_row2.setPlaceholderText("")
        self.lineEdit_row2.setObjectName("lineEdit_row2")
        self.horizontalLayout_10.addWidget(self.lineEdit_row2, 0, QtCore.Qt.AlignLeft)
        self.gridLayout.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 1)
        self.gridLayout.setColumnMinimumWidth(1, 1)
        self.gridLayout.setColumnMinimumWidth(2, 25)
        self.gridLayout.setRowMinimumHeight(0, 1)
        self.gridLayout.setRowMinimumHeight(1, 1)
        self.gridLayout.setRowMinimumHeight(2, 25)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 25)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 25)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(0, 23))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 23))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setEnabled(True)
        self.pushButton_save.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_save.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_save.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_4.addWidget(self.pushButton_save)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.lineEdit_col1.textEdited['QString'].connect(self.lineEdit_col2.setText)
        self.lineEdit_row1.textEdited['QString'].connect(self.lineEdit_row2.setText)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Excel Editor"))
        self.pushButton_file.setText(_translate("MainWindow", "Файл"))
        self.label.setText(_translate("MainWindow", "рабочий лист"))
        self.label_col.setText(_translate("MainWindow", "столбец"))
        self.label_3.setText(_translate("MainWindow", ":"))
        self.label_row.setText(_translate("MainWindow", "строка"))
        self.label_2.setText(_translate("MainWindow", ":"))
        self.pushButton_save.setText(_translate("MainWindow", "Сохранить"))