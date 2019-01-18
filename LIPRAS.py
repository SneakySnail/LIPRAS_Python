# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Qt\LIPRAS_QT\LIPRAS_Qt\mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        MainWindow.resize(988, 759)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout_2.setMargin(11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(473, 61))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 61))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.scrollArea = QtGui.QScrollArea(self.groupBox_2)
        self.scrollArea.setGeometry(QtCore.QRect(10, 20, 201, 31))
        self.scrollArea.setMinimumSize(QtCore.QSize(201, 31))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 199, 29))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(220, 20, 75, 31))
        self.pushButton.setMinimumSize(QtCore.QSize(75, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.radioButton = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(310, 28, 111, 17))
        self.radioButton.setMinimumSize(QtCore.QSize(111, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setMinimumSize(QtCore.QSize(491, 601))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setMargin(11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setMinimumSize(QtCore.QSize(321, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(101, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.widget = QtGui.QWidget(self.groupBox)
        self.widget.setMinimumSize(QtCore.QSize(471, 461))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 461))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 2)
        self.widget_2 = QtGui.QWidget(self.groupBox)
        self.widget_2.setMinimumSize(QtCore.QSize(471, 61))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout.addWidget(self.widget_2, 2, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox, 0, 1, 2, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(473, 621))
        self.tabWidget.setMaximumSize(QtCore.QSize(473, 16777215))
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton_4 = QtGui.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 570, 75, 23))
        self.pushButton_4.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.groupBox_9 = QtGui.QGroupBox(self.tab)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 10, 191, 61))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.label_2 = QtGui.QLabel(self.groupBox_9)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.groupBox_9)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(50, 17, 62, 22))
        self.doubleSpinBox_2.setDecimals(4)
        self.doubleSpinBox_2.setSingleStep(0.01)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_9)
        self.doubleSpinBox.setGeometry(QtCore.QRect(120, 17, 62, 22))
        self.doubleSpinBox.setDecimals(4)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.groupBox_11 = QtGui.QGroupBox(self.groupBox_9)
        self.groupBox_11.setGeometry(QtCore.QRect(0, 0, 191, 61))
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.label_8 = QtGui.QLabel(self.groupBox_11)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(self.groupBox_11)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(50, 17, 62, 22))
        self.doubleSpinBox_3.setDecimals(4)
        self.doubleSpinBox_3.setSingleStep(0.01)
        self.doubleSpinBox_3.setObjectName(_fromUtf8("doubleSpinBox_3"))
        self.doubleSpinBox_4 = QtGui.QDoubleSpinBox(self.groupBox_11)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(120, 17, 62, 22))
        self.doubleSpinBox_4.setDecimals(4)
        self.doubleSpinBox_4.setSingleStep(0.01)
        self.doubleSpinBox_4.setObjectName(_fromUtf8("doubleSpinBox_4"))
        self.groupBox_10 = QtGui.QGroupBox(self.tab)
        self.groupBox_10.setGeometry(QtCore.QRect(10, 70, 141, 201))
        self.groupBox_10.setMinimumSize(QtCore.QSize(141, 201))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.tableWidget_3 = QtGui.QTableWidget(self.groupBox_10)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 21, 111, 171))
        self.tableWidget_3.setMinimumSize(QtCore.QSize(111, 171))
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.groupBox_12 = QtGui.QGroupBox(self.tab)
        self.groupBox_12.setGeometry(QtCore.QRect(10, 310, 441, 261))
        self.groupBox_12.setMinimumSize(QtCore.QSize(441, 261))
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.checkBox_9 = QtGui.QCheckBox(self.groupBox_12)
        self.checkBox_9.setGeometry(QtCore.QRect(360, 40, 70, 17))
        self.checkBox_9.setMinimumSize(QtCore.QSize(70, 17))
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        self.checkBox_10 = QtGui.QCheckBox(self.groupBox_12)
        self.checkBox_10.setGeometry(QtCore.QRect(360, 90, 70, 17))
        self.checkBox_10.setMinimumSize(QtCore.QSize(70, 17))
        self.checkBox_10.setObjectName(_fromUtf8("checkBox_10"))
        self.checkBox_11 = QtGui.QCheckBox(self.groupBox_12)
        self.checkBox_11.setGeometry(QtCore.QRect(360, 140, 70, 17))
        self.checkBox_11.setMinimumSize(QtCore.QSize(70, 17))
        self.checkBox_11.setObjectName(_fromUtf8("checkBox_11"))
        self.pushButton_14 = QtGui.QPushButton(self.groupBox_12)
        self.pushButton_14.setGeometry(QtCore.QRect(360, 182, 75, 31))
        self.pushButton_14.setMinimumSize(QtCore.QSize(75, 31))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.tableView_2 = QtGui.QTableView(self.groupBox_12)
        self.tableView_2.setGeometry(QtCore.QRect(10, 20, 341, 231))
        self.tableView_2.setMinimumSize(QtCore.QSize(341, 231))
        self.tableView_2.setObjectName(_fromUtf8("tableView_2"))
        self.groupBox_13 = QtGui.QGroupBox(self.tab)
        self.groupBox_13.setGeometry(QtCore.QRect(270, 210, 161, 61))
        self.groupBox_13.setMinimumSize(QtCore.QSize(161, 61))
        self.groupBox_13.setObjectName(_fromUtf8("groupBox_13"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_13)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 30, 51, 16))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_13)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 30, 51, 16))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_9 = QtGui.QLabel(self.groupBox_13)
        self.label_9.setGeometry(QtCore.QRect(22, 15, 47, 13))
        self.label_9.setTextFormat(QtCore.Qt.RichText)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox_13)
        self.label_10.setGeometry(QtCore.QRect(92, 15, 47, 13))
        self.label_10.setTextFormat(QtCore.Qt.RichText)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.radioButton_8 = QtGui.QRadioButton(self.tab)
        self.radioButton_8.setGeometry(QtCore.QRect(310, 180, 82, 17))
        self.radioButton_8.setMinimumSize(QtCore.QSize(82, 17))
        self.radioButton_8.setObjectName(_fromUtf8("radioButton_8"))
        self.spinBox_3 = QtGui.QSpinBox(self.tab)
        self.spinBox_3.setGeometry(QtCore.QRect(380, 150, 42, 22))
        self.spinBox_3.setMinimumSize(QtCore.QSize(42, 22))
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(20)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(276, 150, 101, 20))
        self.label_11.setMinimumSize(QtCore.QSize(101, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(260, 10, 191, 131))
        self.groupBox_3.setMinimumSize(QtCore.QSize(191, 131))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter_3 = QtGui.QSplitter(self.groupBox_3)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.label_3 = QtGui.QLabel(self.splitter_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.comboBox_2 = QtGui.QComboBox(self.splitter_3)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.splitter_3)
        self.splitter_2 = QtGui.QSplitter(self.groupBox_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.label_4 = QtGui.QLabel(self.splitter_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.spinBox = QtGui.QSpinBox(self.splitter_2)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(25)
        #self.spinBox.setDisplayIntegerBase(10)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.verticalLayout.addWidget(self.splitter_2)
        self.splitter = QtGui.QSplitter(self.groupBox_3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.radioButton_2 = QtGui.QRadioButton(self.splitter)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.splitter)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(self.splitter)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.verticalLayout.addWidget(self.splitter)
        self.splitter_4 = QtGui.QSplitter(self.groupBox_3)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.pushButton_3 = QtGui.QPushButton(self.splitter_4)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_2 = QtGui.QPushButton(self.splitter_4)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.splitter_4)
        self.pushButton_15 = QtGui.QPushButton(self.tab)
        self.pushButton_15.setGeometry(QtCore.QRect(150, 280, 81, 23))
        self.pushButton_15.setMinimumSize(QtCore.QSize(81, 23))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.pushButton_16 = QtGui.QPushButton(self.tab)
        self.pushButton_16.setGeometry(QtCore.QRect(40, 280, 75, 23))
        self.pushButton_16.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.groupBox_14 = QtGui.QGroupBox(self.tab)
        self.groupBox_14.setGeometry(QtCore.QRect(160, 71, 71, 142))
        self.groupBox_14.setMinimumSize(QtCore.QSize(71, 142))
        self.groupBox_14.setObjectName(_fromUtf8("groupBox_14"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_14)
        self.verticalLayout_3.setMargin(11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.checkBox_12 = QtGui.QCheckBox(self.groupBox_14)
        self.checkBox_12.setMinimumSize(QtCore.QSize(51, 17))
        self.checkBox_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_12.setObjectName(_fromUtf8("checkBox_12"))
        self.verticalLayout_3.addWidget(self.checkBox_12)
        self.checkBox_13 = QtGui.QCheckBox(self.groupBox_14)
        self.checkBox_13.setMinimumSize(QtCore.QSize(51, 17))
        self.checkBox_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_13.setObjectName(_fromUtf8("checkBox_13"))
        self.verticalLayout_3.addWidget(self.checkBox_13)
        self.checkBox_14 = QtGui.QCheckBox(self.groupBox_14)
        self.checkBox_14.setMinimumSize(QtCore.QSize(51, 17))
        self.checkBox_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_14.setObjectName(_fromUtf8("checkBox_14"))
        self.verticalLayout_3.addWidget(self.checkBox_14)
        self.checkBox_15 = QtGui.QCheckBox(self.groupBox_14)
        self.checkBox_15.setMinimumSize(QtCore.QSize(51, 17))
        self.checkBox_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_15.setObjectName(_fromUtf8("checkBox_15"))
        self.verticalLayout_3.addWidget(self.checkBox_15)
        self.checkBox_16 = QtGui.QCheckBox(self.groupBox_14)
        self.checkBox_16.setMinimumSize(QtCore.QSize(51, 17))
        self.checkBox_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_16.setObjectName(_fromUtf8("checkBox_16"))
        self.verticalLayout_3.addWidget(self.checkBox_16)
        self.radioButton_9 = QtGui.QRadioButton(self.tab)
        self.radioButton_9.setGeometry(QtCore.QRect(170, 230, 82, 17))
        self.radioButton_9.setObjectName(_fromUtf8("radioButton_9"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 10, 141, 151))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.radioButton_6 = QtGui.QRadioButton(self.groupBox_7)
        self.radioButton_6.setGeometry(QtCore.QRect(20, 30, 82, 17))
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.radioButton_7 = QtGui.QRadioButton(self.groupBox_7)
        self.radioButton_7.setGeometry(QtCore.QRect(20, 70, 121, 17))
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))
        self.listView = QtGui.QListView(self.tab_2)
        self.listView.setGeometry(QtCore.QRect(170, 20, 251, 141))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.pushButton_9 = QtGui.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 190, 75, 23))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10 = QtGui.QPushButton(self.tab_2)
        self.pushButton_10.setGeometry(QtCore.QRect(120, 190, 75, 23))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_11 = QtGui.QPushButton(self.tab_2)
        self.pushButton_11.setGeometry(QtCore.QRect(220, 190, 75, 23))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.tableWidget_2 = QtGui.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 240, 411, 281))
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.pushButton_12 = QtGui.QPushButton(self.tab_2)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 570, 75, 23))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 988, 21))
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

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "LIPRAS: Line-Profile Analysis Software", None))
        MainWindow.setWindowIcon(QtGui.QIcon('Python.png'))
        self.groupBox_2.setTitle(_translate("MainWindow", "Dataset", None))
        self.pushButton.setText(_translate("MainWindow", "Browse", None))
        self.pushButton.clicked.connect(lambda: self.FileSelect())  # Action upon click

        self.radioButton.setText(_translate("MainWindow", "Reverse File Order", None))
        self.groupBox.setTitle(_translate("MainWindow", "Plotting", None))
        self.label.setText(_translate("MainWindow", "File # of #", None))
        self.pushButton_4.setText(_translate("MainWindow", "Next", None))
        self.pushButton_4.clicked.connect(lambda: self.Next())  # Action upon click

        self.groupBox_9.setTitle(_translate("MainWindow", "Data Range", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>2θ (°)</p></body></html>", None))
        self.groupBox_11.setTitle(_translate("MainWindow", "Data Range", None))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>2θ (°)</p></body></html>", None))
        self.groupBox_10.setTitle(_translate("MainWindow", "Line-Profile Function", None))
        self.groupBox_12.setTitle(_translate("MainWindow", "Fit Bounds", None))
        self.checkBox_9.setText(_translate("MainWindow", "Recycle", None))
        self.checkBox_10.setText(_translate("MainWindow", "Refine Bkg", None))
        self.checkBox_11.setText(_translate("MainWindow", "No Bounds", None))
        self.pushButton_14.setText(_translate("MainWindow", "Fit Data", None))
        self.pushButton_14.clicked.connect(lambda: self.FitData())  # Action upon click

        self.groupBox_13.setTitle(_translate("MainWindow", "Wavelength", None))
        self.lineEdit_3.setText(_translate("MainWindow", "1.5406", None))
        self.lineEdit_4.setText(_translate("MainWindow", "1.5444", None))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p>Cu-K&alpha;<sub>1</sub></p></body></html><?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QLineEdit\" name=\"lineEdit\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>20</x>\n"
"     <y>20</y>\n"
"     <width>51</width>\n"
"     <height>16</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string>1.5406</string>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"", None))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p>Cu-Kα<span style=\" vertical-align:sub;\">2</span></p><p>20 20 51 16 1.5406 </p></body></html>", None))
        self.radioButton_8.setText(_translate("MainWindow", "Lab X-ray", None))
        self.label_11.setText(_translate("MainWindow", "Number of Peaks:", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Background", None))
        self.label_3.setText(_translate("MainWindow", "Model", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Polynomial", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Spline", None))
        self.label_4.setText(_translate("MainWindow", "Polynomial Order", None))
        self.radioButton_2.setText(_translate("MainWindow", "New", None))
        self.radioButton_3.setText(_translate("MainWindow", "Add", None))
        self.radioButton_4.setText(_translate("MainWindow", "Delete", None))
        self.pushButton_3.setText(_translate("MainWindow", "Update Plot", None))
        self.pushButton_3.clicked.connect(lambda: self.UpdatePlot())  # Action upon click

        self.pushButton_2.setText(_translate("MainWindow", "Select Points", None))
        self.pushButton_2.clicked.connect(lambda: self.SelectPoints())  # Action upon click

        self.pushButton_15.setText(_translate("MainWindow", "Select Peak(s)", None))
        self.pushButton_15.clicked.connect(lambda: self.SelectPeaks())  # Action upon click

        self.pushButton_16.setText(_translate("MainWindow", "Update", None))
        self.pushButton_16.clicked.connect(lambda: self.Update())  # Action upon click

        self.groupBox_14.setTitle(_translate("MainWindow", "Constraints", None))
        self.checkBox_12.setText(_translate("MainWindow", "N", None))
        self.checkBox_13.setText(_translate("MainWindow", "x", None))
        self.checkBox_14.setText(_translate("MainWindow", "f", None))
        self.checkBox_15.setText(_translate("MainWindow", "w", None))
        self.checkBox_16.setText(_translate("MainWindow", "m", None))
        self.radioButton_9.setToolTip(_translate("MainWindow", "Forces function to be asymmetric", None))
        self.radioButton_9.setText(_translate("MainWindow", "Asymmetry", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "1. Setup", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "Plot", None))
        self.radioButton_6.setText(_translate("MainWindow", "Peak Fit", None))
        self.radioButton_7.setText(_translate("MainWindow", "Coefficient Trend", None))
        self.pushButton_9.setText(_translate("MainWindow", "Fit Statistics", None))
        self.pushButton_9.clicked.connect(lambda: self.FitStatistics())  # Action upon click

        self.pushButton_10.setText(_translate("MainWindow", "All Fits", None))
        self.pushButton_10.clicked.connect(lambda: self.AllFits())  # Action upon click

        self.pushButton_11.setText(_translate("MainWindow", "Bayesian", None))
        self.pushButton_11.clicked.connect(lambda: self.Bayesian())  # Action upon click

        self.pushButton_12.setText(_translate("MainWindow", "Previous", None))
        self.pushButton_12.clicked.connect(lambda: self.Previous())  # Action upon click

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "2. Results", None))



    def FileSelect(self):
        print('Browse')

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

    def Next(self):
        print('Next')
        self.tabWidget.setCurrentIndex(1)


    def Previous(self):
        print('Previous')
        self.tabWidget.setCurrentIndex(0)

    def FitStatistics(self):
        print('FitStatistics')

    def AllFits(self):
        print('AllFits')

    def Bayesian(self):
        print('Bayesian')


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication.instance()  # Introduced for when running with Canopy (IPython)
    standalone = app is None
    if standalone:
        app = QtGui.QApplication(sys.argv)
    LIPRAS = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    #mpl = MatplotlibWidget()
    # mpl.show()
    ui.setupUi(LIPRAS)
    LIPRAS.show()
    if standalone:
        sys.exit(app.exec_())
    else:
        print "We're back with the Qt window still active"