# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Qt\LIPRAS_QT\LIPRAS_Qt\mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1280,820)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 820))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11,11,11,11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setMinimumSize(QtCore.QSize(491, 601))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(11,11,11,11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widget = QtGui.QWidget(self.groupBox)
        self.widget.setMinimumSize(QtCore.QSize(1, 550))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 2)
        self.widget_2 = QtGui.QWidget(self.groupBox)
        self.widget_2.setMinimumSize(QtCore.QSize(1, 1))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout.addWidget(self.widget_2, 2, 0, 1, 2)
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setMinimumSize(QtCore.QSize(321, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(101, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 1, 5, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(1, 1))
        self.tabWidget.setMaximumSize(QtCore.QSize(800, 800))
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_9 = QtGui.QGridLayout(self.tab)
        self.gridLayout_9.setContentsMargins(11,11,11,11)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setMinimumSize(QtCore.QSize(191, 131))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setContentsMargins(11,11,11,11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.comboBox_2, 0, 1, 1, 4)
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 3)
        self.spinBox = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(25)
   #     self.spinBox.setDisplayIntegerBase(10)

        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout_3.addWidget(self.spinBox, 1, 3, 1, 2)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox_3)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.gridLayout_3.addWidget(self.radioButton_2, 2, 0, 1, 2)
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox_3)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.gridLayout_3.addWidget(self.radioButton_3, 2, 2, 1, 2)
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox_3)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.gridLayout_3.addWidget(self.radioButton_4, 2, 4, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_3.addWidget(self.pushButton_3, 3, 0, 1, 3)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_3.addWidget(self.pushButton_2, 3, 3, 1, 2)
        self.gridLayout_9.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox_9 = QtGui.QGroupBox(self.tab)
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_9)
        self.gridLayout_5.setContentsMargins(11,11,11,11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_2 = QtGui.QLabel(self.groupBox_9)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_9)
        self.doubleSpinBox.setDecimals(4)
        self.doubleSpinBox.setSingleStep(0.05)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))


        self.gridLayout_5.addWidget(self.doubleSpinBox, 0, 2, 1, 1)
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.groupBox_9)
        self.doubleSpinBox_2.setDecimals(4)
        self.doubleSpinBox_2.setSingleStep(0.05)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.gridLayout_5.addWidget(self.doubleSpinBox_2, 0, 1, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_9, 0, 0, 1, 1)
        self.groupBox_12 = QtGui.QGroupBox(self.tab)
        self.groupBox_12.setMinimumSize(QtCore.QSize(1, 1))
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_12)
        self.gridLayout_6.setContentsMargins(11,11,11,11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.tableView_2 = QtGui.QTableView(self.groupBox_12)
        self.tableView_2.setMinimumSize(QtCore.QSize(1, 1))
        self.tableView_2.setObjectName(_fromUtf8("tableView_2"))
        self.gridLayout_6.addWidget(self.tableView_2, 0, 0, 4, 1)
        self.checkBox_9 = QtGui.QCheckBox(self.groupBox_12)
        self.checkBox_9.setMinimumSize(QtCore.QSize(70, 17))
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        self.gridLayout_6.addWidget(self.checkBox_9, 0, 1, 1, 1)
        self.checkBox_10 = QtGui.QCheckBox(self.groupBox_12)
        self.checkBox_10.setMinimumSize(QtCore.QSize(70, 17))
        self.checkBox_10.setObjectName(_fromUtf8("checkBox_10"))
        self.gridLayout_6.addWidget(self.checkBox_10, 1, 1, 1, 1)
        self.checkBox_11 = QtGui.QCheckBox(self.groupBox_12)
        self.checkBox_11.setMinimumSize(QtCore.QSize(70, 17))
        self.checkBox_11.setObjectName(_fromUtf8("checkBox_11"))
        self.gridLayout_6.addWidget(self.checkBox_11, 2, 1, 1, 1)
        self.pushButton_14 = QtGui.QPushButton(self.groupBox_12)
        self.pushButton_14.setMinimumSize(QtCore.QSize(75, 31))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.gridLayout_6.addWidget(self.pushButton_14, 3, 1, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_12, 3, 0, 2, 4)
        self.groupBox_13 = QtGui.QGroupBox(self.tab)
        self.groupBox_13.setMinimumSize(QtCore.QSize(161, 61))
        self.groupBox_13.setObjectName(_fromUtf8("groupBox_13"))
        self.gridLayout_10 = QtGui.QGridLayout(self.groupBox_13)
        self.gridLayout_10.setContentsMargins(11,11,11,11)
        self.gridLayout_10.setSpacing(6)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_13)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(71, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_10.addWidget(self.lineEdit_3, 2, 6, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_13)
        self.label_10.setTextFormat(QtCore.Qt.RichText)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_10.addWidget(self.label_10, 2, 7, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_13)
        self.label_9.setTextFormat(QtCore.Qt.RichText)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_10.addWidget(self.label_9, 2, 5, 1, 1)
        self.groupBox_14 = QtGui.QGroupBox(self.groupBox_13)
        self.groupBox_14.setMinimumSize(QtCore.QSize(1, 1))
        self.groupBox_14.setMaximumSize(QtCore.QSize(200000, 200000))
        self.groupBox_14.setObjectName(_fromUtf8("groupBox_14"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_14)
        self.horizontalLayout.setContentsMargins(11,11,11,11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkBox_12 = QtGui.QCheckBox(self.groupBox_14)
        self.checkBox_12.setMinimumSize(QtCore.QSize(51, 17))
        self.checkBox_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_12.setObjectName(_fromUtf8("checkBox_12"))
        self.horizontalLayout.addWidget(self.checkBox_12)
        self.checkBox_13 = QtGui.QCheckBox(self.groupBox_14)
        self.checkBox_13.setMinimumSize(QtCore.QSize(51, 17))
        self.checkBox_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_13.setObjectName(_fromUtf8("checkBox_13"))
        self.horizontalLayout.addWidget(self.checkBox_13)
        self.checkBox_14 = QtGui.QCheckBox(self.groupBox_14)
        self.checkBox_14.setMinimumSize(QtCore.QSize(51, 17))
        self.checkBox_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_14.setObjectName(_fromUtf8("checkBox_14"))
        self.horizontalLayout.addWidget(self.checkBox_14)
        self.checkBox_16 = QtGui.QCheckBox(self.groupBox_14)
        self.checkBox_16.setMinimumSize(QtCore.QSize(51, 17))
        self.checkBox_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_16.setObjectName(_fromUtf8("checkBox_16"))
        self.horizontalLayout.addWidget(self.checkBox_16)
        self.checkBox_15 = QtGui.QCheckBox(self.groupBox_14)
        self.checkBox_15.setMinimumSize(QtCore.QSize(51, 17))
        self.checkBox_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_15.setObjectName(_fromUtf8("checkBox_15"))
        self.horizontalLayout.addWidget(self.checkBox_15)
        self.gridLayout_10.addWidget(self.groupBox_14, 4, 4, 1, 7)
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_13)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(71, 21))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout_10.addWidget(self.lineEdit_4, 2, 8, 1, 1)
        self.pushButton_16 = QtGui.QPushButton(self.groupBox_13)
        self.pushButton_16.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.gridLayout_10.addWidget(self.pushButton_16, 4, 15, 1, 1)
        self.radioButton_8 = QtGui.QRadioButton(self.groupBox_13)
        self.radioButton_8.setMinimumSize(QtCore.QSize(82, 17))
        self.radioButton_8.setObjectName(_fromUtf8("radioButton_8"))
        self.gridLayout_10.addWidget(self.radioButton_8, 2, 4, 1, 1)
        self.radioButton_9 = QtGui.QRadioButton(self.groupBox_13)
        self.radioButton_9.setObjectName(_fromUtf8("radioButton_9"))
        self.gridLayout_10.addWidget(self.radioButton_9, 2, 15, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_13, 2, 0, 1, 4)
        self.groupBox_10 = QtGui.QGroupBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy)
        self.groupBox_10.setMinimumSize(QtCore.QSize(10, 10))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_10)
        self.gridLayout_7.setContentsMargins(11,11,11,11)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_11 = QtGui.QLabel(self.groupBox_10)
        self.label_11.setMinimumSize(QtCore.QSize(101, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_7.addWidget(self.label_11, 0, 0, 1, 1)
        self.spinBox_3 = QtGui.QSpinBox(self.groupBox_10)
        self.spinBox_3.setMinimumSize(QtCore.QSize(42, 22))
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(20)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.gridLayout_7.addWidget(self.spinBox_3, 0, 1, 1, 1)
        self.pushButton_15 = QtGui.QPushButton(self.groupBox_10)
        self.pushButton_15.setMinimumSize(QtCore.QSize(81, 23))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.gridLayout_7.addWidget(self.pushButton_15, 0, 2, 1, 1)
        self.tableView = QtGui.QTableView(self.groupBox_10)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.gridLayout_7.addWidget(self.tableView, 1, 0, 1, 3)
        self.gridLayout_9.addWidget(self.groupBox_10, 0, 1, 2, 3)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_4.setContentsMargins(11,11,11,11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setContentsMargins(11,11,11,11)
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_7)
        self.verticalLayout.setContentsMargins(11,11,11,11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioButton_6 = QtGui.QRadioButton(self.groupBox_7)
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.verticalLayout.addWidget(self.radioButton_6)
        self.radioButton_7 = QtGui.QRadioButton(self.groupBox_7)
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))
        self.verticalLayout.addWidget(self.radioButton_7)
        self.gridLayout_8.addWidget(self.groupBox_7, 0, 0, 1, 1)
        self.listView = QtGui.QListView(self.tab_2)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout_8.addWidget(self.listView, 0, 1, 4, 1)
        self.pushButton_9 = QtGui.QPushButton(self.tab_2)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.gridLayout_8.addWidget(self.pushButton_9, 1, 0, 1, 1)
        self.pushButton_10 = QtGui.QPushButton(self.tab_2)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.gridLayout_8.addWidget(self.pushButton_10, 2, 0, 1, 1)
        self.pushButton_11 = QtGui.QPushButton(self.tab_2)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.gridLayout_8.addWidget(self.pushButton_11, 3, 0, 1, 1)
        self.tableWidget_2 = QtGui.QTableWidget(self.tab_2)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.gridLayout_8.addWidget(self.tableWidget_2, 4, 0, 1, 2)
        self.gridLayout_4.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 4, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(473, 61))
        self.groupBox_2.setMaximumSize(QtCore.QSize(530, 70))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setContentsMargins(11,11,11,11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.scrollArea = QtGui.QScrollArea(self.groupBox_2)
        self.scrollArea.setMinimumSize(QtCore.QSize(201, 31))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 275, 35))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setMinimumSize(QtCore.QSize(75, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.radioButton = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton.setMinimumSize(QtCore.QSize(111, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1144, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.graphicsView = MatplotlibWidget(LIPRAS)  # MetricTens also works
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView,1,0,1,2)

        self.graphicsView2 = MatplotlibWidget2(LIPRAS)  # MetricTens also works
        self.graphicsView2.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView2,2, 0, 1, 2)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        MainWindow.setWindowTitle(_translate("MainWindow", "LIPRAS: Line-Profile Analysis Software", None))
        MainWindow.setWindowIcon(QtGui.QIcon('Python.png'))
        self.groupBox.setTitle(_translate("MainWindow", "Plotting", None))
        self.label.setText(_translate("MainWindow", "File # of #", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Background", None))
        self.label_3.setText(_translate("MainWindow", "Model", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Polynomial", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Spline", None))
        self.label_4.setText(_translate("MainWindow", "Polynomial Order", None))
        self.radioButton_2.setText(_translate("MainWindow", "New", None))
        self.radioButton_3.setText(_translate("MainWindow", "Add", None))
        self.radioButton_4.setText(_translate("MainWindow", "Delete", None))
        self.pushButton_3.setText(_translate("MainWindow", "Update Plot", None))
        self.pushButton_2.setText(_translate("MainWindow", "Select Points", None))
        self.groupBox_9.setTitle(_translate("MainWindow", "Data Range", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>2θ (°)</p></body></html>", None))
        self.groupBox_12.setTitle(_translate("MainWindow", "Fit Bounds", None))
        self.checkBox_9.setText(_translate("MainWindow", "Recycle", None))
        self.checkBox_10.setText(_translate("MainWindow", "Refine Bkg", None))
        self.checkBox_11.setText(_translate("MainWindow", "No Bounds", None))
        self.pushButton_14.setText(_translate("MainWindow", "Fit Data", None))
        self.groupBox_13.setTitle(_translate("MainWindow", "Peak Options", None))
        self.lineEdit_3.setText(_translate("MainWindow", "1.5406", None))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p>Cu-Kα<span style=\" vertical-align:sub;\">2</span></p></body></html>", None))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p>Cu-Kα<span style=\" vertical-align:sub;\">1</span></p></body></html>", None))
        self.groupBox_14.setTitle(_translate("MainWindow", "Constraints", None))
        self.checkBox_12.setText(_translate("MainWindow", "N", None))
        self.checkBox_13.setText(_translate("MainWindow", "x", None))
        self.checkBox_14.setText(_translate("MainWindow", "f", None))
        self.checkBox_16.setText(_translate("MainWindow", "m", None))
        self.checkBox_15.setText(_translate("MainWindow", "w", None))
        self.lineEdit_4.setText(_translate("MainWindow", "1.5444", None))
        self.pushButton_16.setText(_translate("MainWindow", "Update", None))
        self.radioButton_8.setText(_translate("MainWindow", "Lab X-Ray", None))
        self.radioButton_9.setToolTip(_translate("MainWindow", "Forces function to be asymmetric", None))
        self.radioButton_9.setText(_translate("MainWindow", "Asymmetry", None))
        self.groupBox_10.setTitle(_translate("MainWindow", "Line-Profile Function", None))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Number of Peaks:</p></body></html>", None))
        self.pushButton_15.setText(_translate("MainWindow", "Select Peak(s)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "1. Setup", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "Plot", None))
        self.radioButton_6.setText(_translate("MainWindow", "Peak Fit", None))
        self.radioButton_7.setText(_translate("MainWindow", "Coefficient Trend", None))
        self.pushButton_9.setText(_translate("MainWindow", "Fit Statistics", None))
        self.pushButton_10.setText(_translate("MainWindow", "All Fits", None))
        self.pushButton_11.setText(_translate("MainWindow", "Bayesian", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "2. Results", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Dataset", None))
        self.pushButton.setText(_translate("MainWindow", "Browse", None))
        self.radioButton.setText(_translate("MainWindow", "Reverse File Order", None))

        self.pushButton.clicked.connect(lambda: self.FileSelect(self.scrollArea))  # Action upon click
        self.pushButton_2.clicked.connect(lambda: self.SelectPoints())  # Action upon click
        self.pushButton_3.clicked.connect(lambda: self.UpdatePlot())  # Action upon click
        self.pushButton_9.clicked.connect(lambda: self.FitStatistics())  # Action upon click
        self.pushButton_10.clicked.connect(lambda: self.AllFits())  # Action upon click
        self.pushButton_11.clicked.connect(lambda: self.Bayesian())  # Action upon click
        self.pushButton_14.clicked.connect(lambda: self.FitData())  # Action upon click
        self.pushButton_15.clicked.connect(lambda: self.SelectPeaks())  # Action upon click
        self.pushButton_16.clicked.connect(lambda: self.Update())  # Action upon click

        self.doubleSpinBox.valueChanged.connect((lambda: self.Max2T_CB(self)))
        self.doubleSpinBox_2.valueChanged.connect((lambda: self.Min2T_CB(self)))
        self.doubleSpinBox_2.setKeyboardTracking(False)  # Allows user to edit range without triggering callback immediatley
        self.doubleSpinBox.setKeyboardTracking(False)  # Allows user to edit range without triggering callback immediatley


    def FileSelect(self,pon):
        print('Browse')
        dlg = QtGui.QFileDialog()
        self.Files = dlg.getOpenFileNames(pon, 'Select ' + ' File(s)', owd, " Select diffraction file (*.chi *.xy)")

        if len(self.Files) == 0:
            print('No file selected')
            return
        self.Fdir = str(os.path.split(self.Files[0][0])[0])

        if self.Files[0] != []:
            self.FileList = self.Files[:]
            self.comboBox.clear()
            for i in range(0, len(self.Files[0])):
                self.comboBox.addItems([(os.path.split(str(self.Files[0][i]))[1])])
        elif self.Files[0] != [] and self.Fdir != []:
            self.Fdir = owd

        message_label = QtGui.QLabel()
        message_label.setText(self.Fdir)
        self.scrollArea.setWidget(message_label)

        Mode = 'sqrt';
        ax= self.graphicsView.figure.add_subplot(111)
        ax.cla()

        ax.set_xlabel('2Theta')
        ax.set_ylabel('Intensity (a.u.)')

        twotheta = {};
        intensity = {};
        nint = {};

        for i in range(0, len(self.Files[0])):
            x, y = np.loadtxt(self.Files[0][i], skiprows=4, usecols=(0, 1), unpack=True);
            twotheta[i] = x;
            intensity[i] = y;

        self.twotheta=twotheta
        self.intensity=intensity

        self.Min2T=np.min(x)
        self.Max2T=np.max(x)
        self.doubleSpinBox_2.setValue(self.Min2T)
        self.doubleSpinBox.setValue(self.Max2T)
        self.doubleSpinBox_2.setMinimum(self.Min2T)
        self.doubleSpinBox.setMaximum(self.Max2T)

    def Min2T_CB(self,dat):
        print(float(self.doubleSpinBox_2.value()))
        self.Min2T = self.doubleSpinBox_2.value()

        self.rePlot(self.twotheta,self.intensity)

    def Max2T_CB(self,dat):
        print(float(self.doubleSpinBox.value()))
        self.Max2T = self.doubleSpinBox.value()

        self.rePlot(self.twotheta,self.intensity)


    def UpdatePlot(self):
        print('UpdatePlot')

    def SelectPoints(self):
        print('SelectPoints')

    def Update(self):
        print('Update')

    def SelectPeaks(self):
        print('SelectPeaks')

    def FitData(self):
        print('FitData')

    def FitStatistics(self):
        print('FitStatistics')

    def AllFits(self):
        print('AllFits')

    def Bayesian(self):
        print('Bayesian')

    def rePlot(self,x,y):
        print('rePlot')

        ax = self.graphicsView.figure.add_subplot(111)
        ax.cla()

        idx2 = (np.abs(x[0] - self.doubleSpinBox_2.value())).argmin()
        idx1 = (np.abs(x[0] - self.doubleSpinBox.value())).argmin()


        ax.plot(x[0][idx2:idx1], y[0][idx2:idx1], ':o')
        ax.set_xlabel('2Theta')
        ax.set_ylabel('Intensity (a.u.)')

        self.graphicsView.canvas.draw()
        self.graphicsView.figure.tight_layout()


class MatplotlibWidget(QtGui.QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        self.canvas.setParent(self)
        self.canvas.setFocus()
       # self.canvas.setGeometry(0, 0, 500, 450)  # needed if layout is not specified

        self.toolbar = NavigationToolbar(self.canvas, self)
        #self.toolbar.setGeometry(0, 0, 500, 25)

        layout = QtGui.QVBoxLayout()  #layout needs to be added for this to be implemented and working with resize
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.setParent(self.canvas)
        self.setLayout(layout)


        ax = self.figure.add_subplot(111)

        # data = [random.random() for i in range(10)]
        # ax.plot(data, '*-')
        # self.canvas.draw()
        FigureCanvas.updateGeometry(self)
        self.canvas.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)


class MatplotlibWidget2(QtGui.QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MatplotlibWidget2, self).__init__(parent)

        self.figure = Figure()

        self.canvas = FigureCanvas(self.figure)

        self.canvas.setParent(self)
        self.canvas.setFocus()
       # self.canvas.setGeometry(0, 0, 500, 450)  # needed if layout is not specified

        #self.toolbar = NavigationToolbar(self.canvas, self)
        #self.toolbar.setGeometry(0, 0, 500, 25)

        layout = QtGui.QVBoxLayout()  #layout needs to be added for this to be implemented and working with resize
        #layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.setParent(self.canvas)
        self.setLayout(layout)



        ax = self.figure.add_subplot(111)

        # data = [random.random() for i in range(10)]
        # ax.plot(data, '*-')
        # self.canvas.draw()
        FigureCanvas.updateGeometry(self)
        self.canvas.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)


if __name__ == "__main__":
    import sys
    import os
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
    from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

    app = QtGui.QApplication.instance()  # Introduced for when running with Canopy (IPython)
    standalone = app is None
    if standalone:
        app = QtGui.QApplication(sys.argv)
        font = app.font()
        font.setPointSize(10)
        app.setFont(font)
    LIPRAS = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    mpl = MatplotlibWidget()
    #mpl.show()
    ui.setupUi(LIPRAS)
    LIPRAS.show()
    owd = os.getcwd()

    if standalone:
        sys.exit(app.exec_())
    else:
        print "We're back with the Qt window still active"