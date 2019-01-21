# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'metrictens.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!
from PySide import QtGui, QtCore
import sys
from matplotlib.figure import Figure
import matplotlib.lines as mlines
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np

# from PyQt4 import QtCore, QtGui

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


class Ui_MetricTens(object):
    def setupUi(self, MetricTens):
        MetricTens.setObjectName(_fromUtf8("MetricTens"))
        MetricTens.setFixedSize(775, 693)
        self.centralWidget = QtGui.QWidget(MetricTens)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBox_2 = QtGui.QComboBox(self.centralWidget)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_2, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.comboBox = QtGui.QComboBox(self.centralWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)

        self.graphicsView = MatplotlibWidget(MetricTens)  # MetricTens also works
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 1, 1, 3, 2)

        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(44, 40, 41, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(94, 40, 41, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(144, 40, 41, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(44, 80, 41, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(94, 80, 41, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(144, 80, 41, 20))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(41, 25, 47, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_24 = QtGui.QLabel(self.groupBox)
        self.label_24.setGeometry(QtCore.QRect(40, 120, 151, 21))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_25 = QtGui.QLabel(self.groupBox)
        self.label_25.setGeometry(QtCore.QRect(91, 25, 47, 13))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.label_26 = QtGui.QLabel(self.groupBox)
        self.label_26.setGeometry(QtCore.QRect(141, 25, 47, 13))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_27 = QtGui.QLabel(self.groupBox)
        self.label_27.setGeometry(QtCore.QRect(41, 65, 47, 13))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.label_28 = QtGui.QLabel(self.groupBox)
        self.label_28.setGeometry(QtCore.QRect(91, 65, 47, 13))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.label_29 = QtGui.QLabel(self.groupBox)
        self.label_29.setGeometry(QtCore.QRect(141, 65, 47, 13))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.spinBox = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(20, 46, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox_2 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_2.setGeometry(QtCore.QRect(63, 46, 42, 22))
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.spinBox_3 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_3.setGeometry(QtCore.QRect(106, 46, 42, 22))
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.spinBox_3.setValue(1)
        self.radioButton = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(170, 38, 51, 17))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(170, 58, 51, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.spinBox_4 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_4.setGeometry(QtCore.QRect(172, 110, 42, 22))
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.spinBox_4.setMaximum(360)
        self.spinBox_4.setMinimum(-360)
        self.spinBox_5 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_5.setGeometry(QtCore.QRect(20, 110, 42, 22))
        self.spinBox_5.setObjectName(_fromUtf8("spinBox_5"))
        self.spinBox_5.setMaximum(360)
        self.spinBox_5.setMinimum(-360)
        self.spinBox_6 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_6.setGeometry(QtCore.QRect(63, 110, 42, 22))
        self.spinBox_6.setObjectName(_fromUtf8("spinBox_6"))
        self.spinBox_6.setMaximum(360)
        self.spinBox_6.setMinimum(-360)
        self.spinBox_7 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_7.setGeometry(QtCore.QRect(106, 110, 42, 22))
        self.spinBox_7.setObjectName(_fromUtf8("spinBox_7"))
        self.spinBox_7.setMaximum(360)
        self.spinBox_7.setMinimum(-360)
        self.label_30 = QtGui.QLabel(self.groupBox_2)
        self.label_30.setGeometry(QtCore.QRect(23, 91, 81, 16))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.label_31 = QtGui.QLabel(self.groupBox_2)
        self.label_31.setGeometry(QtCore.QRect(23, 27, 81, 16))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.label_32 = QtGui.QLabel(self.groupBox_2)
        self.label_32.setGeometry(QtCore.QRect(170, 90, 51, 16))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.checkBox = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox.setGeometry(QtCore.QRect(30, 40, 70, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_2.setGeometry(QtCore.QRect(120, 40, 91, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.pushButton = QtGui.QPushButton(self.groupBox_4)
        self.pushButton.setGeometry(QtCore.QRect(30, 80, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 80, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.checkBox.raise_()
        self.checkBox_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.gridLayout.addWidget(self.groupBox_4, 3, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.spinBox_8 = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox_8.setGeometry(QtCore.QRect(44, 31, 37, 20))
        self.spinBox_8.setObjectName(_fromUtf8("spinBox_8"))
        self.spinBox_9 = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox_9.setGeometry(QtCore.QRect(82, 31, 37, 20))
        self.spinBox_9.setObjectName(_fromUtf8("spinBox_9"))
        self.spinBox_10 = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox_10.setGeometry(QtCore.QRect(120, 31, 37, 20))
        self.spinBox_10.setObjectName(_fromUtf8("spinBox_10"))
        self.spinBox_11 = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox_11.setGeometry(QtCore.QRect(44, 50, 37, 20))
        self.spinBox_11.setObjectName(_fromUtf8("spinBox_11"))
        self.spinBox_12 = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox_12.setGeometry(QtCore.QRect(82, 50, 37, 20))
        self.spinBox_12.setObjectName(_fromUtf8("spinBox_12"))
        self.spinBox_14 = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox_14.setGeometry(QtCore.QRect(44, 91, 37, 20))
        self.spinBox_14.setObjectName(_fromUtf8("spinBox_14"))
        self.spinBox_15 = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox_15.setGeometry(QtCore.QRect(82, 91, 37, 20))
        self.spinBox_15.setObjectName(_fromUtf8("spinBox_15"))
        self.spinBox_16 = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox_16.setGeometry(QtCore.QRect(120, 91, 37, 20))
        self.spinBox_16.setObjectName(_fromUtf8("spinBox_16"))
        self.spinBox_17 = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox_17.setGeometry(QtCore.QRect(44, 110, 37, 20))
        self.spinBox_17.setObjectName(_fromUtf8("spinBox_17"))
        self.spinBox_18 = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox_18.setGeometry(QtCore.QRect(82, 110, 37, 20))
        self.spinBox_18.setObjectName(_fromUtf8("spinBox_18"))
        self.spinBox_19 = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox_19.setGeometry(QtCore.QRect(120, 110, 37, 20))
        self.spinBox_19.setObjectName(_fromUtf8("spinBox_19"))
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(196, 20, 111, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(190, 80, 121, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(380, 20, 111, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(387, 80, 111, 20))
        self.label_6.setGeometry(QtCore.QRect(387, 80, 111, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(546, 20, 111, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(231, 40, 41, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(370, 40, 41, 20))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(410, 40, 41, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(450, 40, 41, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(370, 60, 41, 20))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(410, 60, 41, 20))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(450, 60, 41, 20))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(410, 98, 41, 20))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(370, 118, 41, 20))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.groupBox_3)
        self.label_17.setGeometry(QtCore.QRect(450, 118, 41, 20))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.groupBox_3)
        self.label_18.setGeometry(QtCore.QRect(410, 118, 41, 20))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.groupBox_3)
        self.label_19.setGeometry(QtCore.QRect(450, 98, 41, 20))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.groupBox_3)
        self.label_20.setGeometry(QtCore.QRect(370, 98, 41, 20))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.groupBox_3)
        self.label_21.setGeometry(QtCore.QRect(230, 100, 41, 20))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(self.groupBox_3)
        self.label_22.setGeometry(QtCore.QRect(548, 60, 41, 20))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(self.groupBox_3)
        self.label_23.setGeometry(QtCore.QRect(548, 40, 41, 20))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_33 = QtGui.QLabel(self.groupBox_3)
        self.label_33.setGeometry(QtCore.QRect(8, 34, 31, 16))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_34 = QtGui.QLabel(self.groupBox_3)
        self.label_34.setGeometry(QtCore.QRect(8, 53, 31, 16))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.label_35 = QtGui.QLabel(self.groupBox_3)
        self.label_35.setGeometry(QtCore.QRect(8, 95, 31, 16))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.label_36 = QtGui.QLabel(self.groupBox_3)
        self.label_36.setGeometry(QtCore.QRect(8, 112, 31, 16))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.spinBox_13 = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox_13.setGeometry(QtCore.QRect(120, 50, 37, 20))
        self.spinBox_13.setObjectName(_fromUtf8("spinBox_13"))
        self.spinBox_8.raise_()
        self.spinBox_8.setValue(1)
        self.spinBox_8.setMinimum(-99)
        self.spinBox_9.raise_()
        self.spinBox_9.setValue(1)
        self.spinBox_9.setMinimum(-99)
        self.spinBox_10.raise_()
        self.spinBox_10.setValue(1)
        self.spinBox_10.setMinimum(-99)
        self.spinBox_11.raise_()
        self.spinBox_11.setValue(2)
        self.spinBox_11.setMinimum(-99)
        self.spinBox_12.raise_()
        self.spinBox_12.setValue(1)
        self.spinBox_12.setMinimum(-99)
        self.spinBox_13.raise_()
        self.spinBox_13.setValue(1)
        self.spinBox_13.setMinimum(-99)
        self.spinBox_14.raise_()
        self.spinBox_14.setValue(2)
        self.spinBox_14.setMinimum(-99)
        self.spinBox_15.raise_()
        self.spinBox_15.setMinimum(-99)
        self.spinBox_15.setValue(1)
        self.spinBox_16.raise_()
        self.spinBox_16.setValue(1)
        self.spinBox_16.setMinimum(-99)
        self.spinBox_17.raise_()
        self.spinBox_17.setValue(1)
        self.spinBox_17.setMinimum(-99)
        self.spinBox_18.raise_()
        self.spinBox_18.setValue(1)
        self.spinBox_18.setMinimum(-99)
        self.spinBox_19.raise_()
        self.spinBox_19.setValue(1)
        self.spinBox_19.setMinimum(-99)
        self.label_2.raise_()
        self.spinBox_13.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_33.raise_()
        self.label_34.raise_()
        self.label_35.raise_()
        self.label_36.raise_()
        self.gridLayout.addWidget(self.groupBox_3, 4, 0, 1, 3)
        MetricTens.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MetricTens)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 721, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MetricTens.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MetricTens)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MetricTens.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MetricTens)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MetricTens.setStatusBar(self.statusBar)

        self.retranslateUi(MetricTens)
        QtCore.QMetaObject.connectSlotsByName(MetricTens)

        self.lineEdit.setText(_translate("MetricTens", "5", None))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setText(_translate("MetricTens", "5", None))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setVisible(False)

        self.lineEdit_3.setText(_translate("MetricTens", "5", None))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setVisible(False)

        self.lineEdit_4.setText(_translate("MetricTens", "90", None))
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setVisible(False)

        self.lineEdit_5.setText(_translate("MetricTens", "90", None))
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setVisible(False)

        self.lineEdit_6.setText(_translate("MetricTens", "90", None))
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setVisible(False)

        self.label_25.setVisible(False)
        self.label_26.setVisible(False)
        self.label_27.setVisible(False)
        self.label_28.setVisible(False)
        self.label_29.setVisible(False)

        # Starting Crystal Structure Parameter
        self.a = self.lineEdit.text()
        self.b = self.lineEdit_2.text()
        self.c = self.lineEdit_3.text()
        self.alpha = self.lineEdit_4.text()
        self.beta = self.lineEdit_5.text()
        self.gam = self.lineEdit_6.text()
        self.n = 1

    def retranslateUi(self, MetricTens):
        MetricTens.setWindowTitle(_translate("MetricTens", "MetricTens", None))
        MetricTens.setWindowIcon(QtGui.QIcon('MetricTens Icon2_Icon.png'))
        self.comboBox_2.setItemText(0, _translate("MetricTens", "Cubic", None))
        self.comboBox_2.setItemText(1, _translate("MetricTens", "Tetragonal", None))
        self.comboBox_2.setItemText(2, _translate("MetricTens", "Hexagonal", None))
        self.comboBox_2.setItemText(3, _translate("MetricTens", "Rhombohedral", None))
        self.comboBox_2.setItemText(4, _translate("MetricTens", "Orthorhombic", None))
        self.comboBox_2.setItemText(5, _translate("MetricTens", "Monoclinic", None))
        self.comboBox_2.setItemText(6, _translate("MetricTens", "Triclinic", None))
        self.comboBox_2.activated.connect(lambda: self.crystalsystems(self.comboBox_2.currentText()))
        self.label.setText(_translate("MetricTens", "Wulff Net", None))
        self.comboBox.setItemText(0, _translate("MetricTens", "Stereographic Projection", None))
        self.comboBox.setItemText(1, _translate("MetricTens", "3D Diffract", None))
        self.groupBox.setTitle(_translate("MetricTens", "Crystal Structure Parameters", None))
        self.label_3.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">a</p></body></html>", None))
        self.label_24.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">Unit Cell Volume:</p></body></html>",
                       None))
        self.label_25.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">b</p></body></html>", None))
        self.label_26.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">c</p></body></html>", None))
        self.label_27.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">α</p></body></html>", None))
        self.label_28.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">&Beta;</p></body></html>", None))
        self.label_29.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">&gamma;</p></body></html>", None))
        self.groupBox_2.setTitle(_translate("MetricTens", "Set View and Rotation", None))
        self.radioButton.setText(_translate("MetricTens", "[HKL]", None))
        self.radioButton_2.setText(_translate("MetricTens", "(HKL)", None))
        self.label_30.setText(_translate("MetricTens", "<html><head/><body><p>X-Y-Z [Order]</p></body></html>", None))
        self.label_31.setText(_translate("MetricTens", "<html><head/><body><p>HKL</p></body></html>", None))
        self.label_32.setText(_translate("MetricTens", "<html><head/><body><p>Wulff Net</p></body></html>", None))
        self.groupBox_4.setTitle(_translate("MetricTens", "Execute Computation", None))
        self.checkBox.setText(_translate("MetricTens", "Plot Poles", None))
        self.checkBox_2.setText(_translate("MetricTens", "Plot Directions", None))
        self.pushButton.setText(_translate("MetricTens", "Compute", None))
        # self.pushButton.clicked.connect(lambda: self.crystalcomp(int(self.a), int(self.b),
        #                                                          int(self.c),
        #                                                          int(self.alpha),
        #                                                          int(self.beta),
        #                                                          int(self.gam)))  # first callback
        self.pushButton.clicked.connect(lambda: self.crystalconstraint(self.comboBox_2.currentText()))
        # self.pushButton.clicked.connect(lambda: self.graphicsView.plotDataPoints()) # when making a button run two things, this can be done inside the class init in line above
        self.pushButton_2.setText(_translate("MetricTens", "Reset HKL", None))
        self.pushButton_2.clicked.connect(lambda: self.hklreset())
        self.groupBox_3.setTitle(_translate("MetricTens", "Crystallographic Computations", None))
        self.label_2.setText(_translate("MetricTens", "<html>Angel Between Planes", None))
        self.label_4.setText(_translate("MetricTens", "<html>Angel Between Directions", None))
        self.label_5.setText(_translate("MetricTens", "Direction Normal", None))
        self.label_6.setText(_translate("MetricTens", "Plane Normal", None))
        self.label_7.setText(_translate("MetricTens", "<html><i>d</i>-space</html>", None))
        self.label_8.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">1</p></body></html>", None))
        self.label_9.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">2</p></body></html>", None))
        self.label_10.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">3</p></body></html>", None))
        self.label_11.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">4</p></body></html>", None))
        self.label_12.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">5</p></body></html>", None))
        self.label_13.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">6</p></body></html>", None))
        self.label_14.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">7</p></body></html>", None))
        self.label_15.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">8</p></body></html>", None))
        self.label_16.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">9</p></body></html>", None))
        self.label_17.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">10</p></body></html>", None))
        self.label_18.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">11</p></body></html>", None))
        self.label_19.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">12</p></body></html>", None))
        self.label_20.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">13</p></body></html>", None))
        self.label_21.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">14</p></body></html>", None))
        self.label_22.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">15</p></body></html>", None))
        self.label_23.setText(
            _translate("MetricTens", "<html><head/><body><p align=\"center\">16</p></body></html>", None))
        self.label_33.setText(_translate("MetricTens", "<html><head/><body><p>(HKL)1</p></body></html>", None))
        self.label_34.setText(_translate("MetricTens", "<html><head/><body><p>(HKL)2</p></body></html>", None))
        self.label_35.setText(_translate("MetricTens", "<html><head/><body><p>[HKL]1</p></body></html>", None))
        self.label_36.setText(_translate("MetricTens", "<html><head/><body><p>[HKL]2</p></body></html>", None))
        self.graphicsView.setVisible(False)

        self.lineEdit_4.textChanged.connect(lambda: self.editboxcallback())
        self.lineEdit_5.textChanged.connect(lambda: self.editboxcallback())

    def editboxcallback(self):
        cs = self.comboBox_2.currentText()
        if cs == 'Rhombohedral':
            self.lineEdit_5.setText(self.lineEdit_4.text())
            self.lineEdit_6.setText(self.lineEdit_4.text())
        elif cs == 'Monoclinic':
            self.lineEdit_4.setText(self.lineEdit_5.text())
            self.lineEdit_6.setText(self.lineEdit_5.text())

    def crystalsystems(self, cs):
        self.boxreset()

        if cs == 'Cubic':
            self.lineEdit_2.setVisible(False)
            self.b = self.a
            self.lineEdit_3.setVisible(False)
            self.c = self.a
            self.lineEdit_4.setVisible(False)
            self.alpha = 90
            self.beta = self.alpha
            self.gam = self.alpha
            self.lineEdit_5.setVisible(False)
            self.lineEdit_6.setVisible(False)

            self.label_25.setVisible(False)
            self.label_26.setVisible(False)
            self.label_27.setVisible(False)
            self.label_28.setVisible(False)
            self.label_29.setVisible(False)
            # start with self.a=self.lineEdit_2.text(), make sure this is specicifed on default then modify here to mimic MetricTens MATLAB
        elif cs == 'Tetragonal':

            self.lineEdit_2.setVisible(False)
            self.lineEdit_4.setVisible(False)
            self.lineEdit_5.setVisible(False)
            self.lineEdit_6.setVisible(False)
            self.label_25.setVisible(False)
            self.label_27.setVisible(False)
            self.label_28.setVisible(False)
            self.label_29.setVisible(False)
        elif cs == 'Hexagonal':

            self.lineEdit_2.setVisible(False)
            self.lineEdit_4.setVisible(False)
            self.lineEdit_5.setVisible(False)
            self.label_25.setVisible(False)
            self.label_27.setVisible(False)
            self.label_28.setVisible(False)
            self.lineEdit_6.setText('120')
            self.lineEdit_6.setReadOnly(True)

        elif cs == 'Rhombohedral':

            self.lineEdit_2.setVisible(False)
            self.lineEdit_3.setVisible(False)
            self.label_25.setVisible(False)
            self.label_26.setVisible(False)
            self.lineEdit_4.setText('90')
            self.lineEdit_5.setText('90')
            self.lineEdit_5.setReadOnly(True)
            self.lineEdit_6.setText('90')
            self.lineEdit_6.setReadOnly(True)

        elif cs == 'Orthorhombic':

            self.lineEdit_4.setVisible(False)
            self.lineEdit_5.setVisible(False)
            self.lineEdit_6.setVisible(False)

            self.label_27.setVisible(False)
            self.label_28.setVisible(False)
            self.label_29.setVisible(False)
        elif cs == 'Monoclinic':
            self.lineEdit.setVisible(True)
            self.lineEdit_4.setText('90')
            self.lineEdit_5.setText('90')
            self.lineEdit_6.setText('90')

            self.lineEdit_6.setReadOnly(True)
            self.lineEdit_4.setReadOnly(True)

        elif cs == 'Triclinic':
            self.boxreset()

    def boxreset(self):
        self.lineEdit.setVisible(True)
        self.lineEdit_2.setVisible(True)
        self.lineEdit_3.setVisible(True)
        self.lineEdit_4.setVisible(True)
        self.lineEdit_5.setVisible(True)
        self.lineEdit_6.setVisible(True)

        self.lineEdit.setReadOnly(False)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_3.setReadOnly(False)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_5.setReadOnly(False)
        self.lineEdit_6.setReadOnly(False)

        self.label_2.setVisible(True)
        self.label_3.setVisible(True)
        self.label_25.setVisible(True)
        self.label_26.setVisible(True)
        self.label_27.setVisible(True)
        self.label_28.setVisible(True)
        self.label_29.setVisible(True)

    def crystalconstraint(self, cs):
        self.a = float(unicode(self.lineEdit.text()))
        self.b = float(unicode(self.lineEdit_2.text()))
        self.c = float(unicode(self.lineEdit_3.text()))
        self.alpha = float(unicode(self.lineEdit_4.text()))
        self.beta = float(unicode(self.lineEdit_5.text()))
        self.gam = float(unicode(self.lineEdit_6.text()))

        if cs == 'Cubic':
            self.b = self.a
            self.c = self.a
            self.alpha = 90
            self.beta = self.alpha
            self.gam = self.alpha

        elif cs == 'Tetragonal':
            self.b = self.a
            self.alpha = 90
            self.beta = self.alpha
            self.gam = self.alpha

        elif cs == 'Hexagonal':
            self.b = self.a
            self.alpha = 90
            self.beta = self.alpha
            self.gam = 120

        elif cs == 'Rhombohedral':
            self.b = self.a
            self.c = self.a
            self.beta = self.alpha
            self.gam = self.alpha


        elif cs == 'Orthorhombic':
            self.alpha = 90
            self.beta = self.alpha
            self.gam = self.alpha

        elif cs == 'Monoclinic':

            self.alpha = self.beta
            self.gam = self.beta

        elif cs == 'Triclinic':
            a = 1
        self.crystalcomp(self.a, self.b, self.c, self.alpha, self.beta, self.gam)

    def crystalcomp(self, a, b, c, alpha, beta, gam):

        from numpy.linalg import inv
        alpha = np.deg2rad(alpha)
        beta = np.deg2rad(beta)
        gam = np.deg2rad(gam)
        p1 = np.array([self.spinBox_8.value(), self.spinBox_9.value(), self.spinBox_10.value()])
        p2 = np.array([self.spinBox_11.value(), self.spinBox_12.value(), self.spinBox_13.value()])
        d1 = np.array([self.spinBox_14.value(), self.spinBox_15.value(), self.spinBox_16.value()])
        d2 = np.array([self.spinBox_17.value(), self.spinBox_18.value(), self.spinBox_19.value()])

        g = np.array(
            [[a ** 2, a * b * np.cos(gam), a * c * np.cos(beta)], [b * a * np.cos(gam), b ** 2, b * c * np.cos(alpha)],
             [c * a * np.cos(beta), c * b * np.cos(alpha), c ** 2]])
        g = np.mat(g)
        g1 = np.mat(inv(g))

        p1 = np.mat(p1)
        p2 = np.mat(p2)
        d1 = np.mat(d1)
        d2 = np.mat(d2)

        dspace1 = (np.sqrt(p1 * g1 * p1.T)) ** -1
        dspace2 = (np.sqrt(p2 * g1 * p2.T)) ** -1
        Dir_norm_p1 = p1 * g1 * 10
        Dir_norm_p2 = p2 * g1 * 10
        Plane_norm_d1 = d1 * g / 10
        Plane_norm_d2 = d2 * g / 10

        Ang_Directions = np.rad2deg(np.arccos(((d1 * g * d2.T) / (np.sqrt(d1 * g * d1.T) * np.sqrt(d2 * g * d2.T)))))
        Ang_Planes = np.rad2deg(np.arccos(((p1 * g1 * p2.T) / (np.sqrt(p1 * g1 * p1.T) * np.sqrt(p2 * g1 * p2.T)))))
        V_Cell = np.sqrt(a ** 2 * b ** 2 * c ** 2 * (
            1 - np.cos(alpha) ** 2 - np.cos(beta) ** 2 - np.cos(gam) ** 2 + 2 * np.cos(alpha) * np.cos(beta) * np.cos(
                gam)))

        self.label_8.setText(str(np.round(float(Ang_Planes), 4)))  # sets the angle between planes box
        self.label_21.setText(str(np.round(float(Ang_Directions), 4)))  # sets the angle between planes box

        # Normals
        d = 3  # controls rounding for Plane/Direction Normals
        self.label_9.setText(str(np.round(np.array(Dir_norm_p1)[0][0], d)))  #
        self.label_10.setText(str(np.round(np.array(Dir_norm_p1)[0][1], d)))  #
        self.label_11.setText(str(np.round(np.array(Dir_norm_p1)[0][2], d)))  #
        self.label_12.setText(str(np.round(np.array(Dir_norm_p2)[0][0], d)))  #
        self.label_13.setText(str(np.round(np.array(Dir_norm_p2)[0][1], d)))  #
        self.label_14.setText(str(np.round(np.array(Dir_norm_p2)[0][2], d)))  #

        self.label_20.setText(str(np.round(np.array(Plane_norm_d1)[0][0], d)))  #
        self.label_15.setText(str(np.round(np.array(Plane_norm_d1)[0][1], d)))  #
        self.label_19.setText(str(np.round(np.array(Plane_norm_d1)[0][2], d)))  #
        self.label_16.setText(str(np.round(np.array(Plane_norm_d2)[0][0], d)))  #
        self.label_18.setText(str(np.round(np.array(Plane_norm_d2)[0][1], d)))  #
        self.label_17.setText(str(np.round(np.array(Plane_norm_d2)[0][2], d)))  #

        # Dspace
        self.label_23.setText(str(np.round(float(np.array(dspace1)), 4)))  #
        self.label_22.setText(str(np.round(float(np.array(dspace2)), 4)))  #

        # Unit Cell Volume
        ucv = "<html><head/><p align=\"center\">Unit Cell Volume: " + str(np.round(V_Cell, 4)) + "</p></html>"

        self.label_24.setText(ucv)

        # self.graphicsView.plotWulf()  # this will work, self from Matplotlib is passed by default other inputs are add.

        # Stereographic projections
        self.Mat_dir = [[np.sqrt(g[0, 0]), g[1, 0] / np.sqrt(g[0, 0]), g[2, 0] / np.sqrt(g[0, 0])],
                        [0, V_Cell * np.sqrt(g1[2, 2] / g[0, 0]), - V_Cell * g1[2, 1] / np.sqrt(g1[2, 2] * g[0, 0])],
                        [0, 0, 1 / np.sqrt(g1[2, 2])]]
        self.Mat_pole = self.Mat_dir * g1
        if self.checkBox.isChecked() == False and self.checkBox_2.isChecked() == False:
            self.graphicsView.setVisible(False)
        else:
            self.graphicsView.plotWulf(self)  # for when calling from another function

        self.hd1 = d1
        self.hd2 = d2
        self.hp1 = p1
        self.hp2 = p2
        if self.n == 1:
            self.hkld = d1
            self.hklp = p1
        self.hkld = np.vstack([self.hkld, d1, d2])
        self.hklp = np.vstack([self.hklp, p1, p2])
        self.n = self.n + 1

        self.StereographicProjPlot(self.hklp, self.hkld)

    def StereographicProjPlot(self, hklp, hkld):
        hklp = hklp[::-1] # flips order
        hkld = hkld[::-1]

        danx = self.spinBox.value()
        dany = self.spinBox_2.value()
        danz = self.spinBox_3.value()
        def1 = np.array([danx, dany, danz])

        if self.radioButton.isChecked() == True:
            set1 = self.Mat_dir * np.matrix(def1).T
            set1 = set1 / np.linalg.norm(set1)
        else:
            set1 = self.Mat_pole * np.matrix(def1).T
            set1 = set1 / np.linalg.norm(set1)

        azi_ele = self.cart2sph(set1[0], set1[1], set1[2])
        sanz = azi_ele[0] - np.pi/2
        sanx = azi_ele[1] - np.pi/2
        sany = 0

        # First Rotations to Set View [Order dependent Z-Y-X]
        transx = np.array([[1, 0, 0], [0, np.cos(sanx), -np.sin(sanx)], [0, np.sin(sanx), np.cos(sanx)]])
        transy = np.array([[np.cos(sany), 0, -np.sin(sany)], [0, 1, 0], [np.sin(sany), 0, np.cos(sany)]])
        transz = np.array([[np.cos(sanz), -np.sin(sanz), 0], [np.sin(sanz), np.cos(sanz), 0], [0, 0, 1]])

        # Second Rotations for Additional Rotations [Order dependent X-Y-Z]
        sanx2 = np.deg2rad(180 + self.spinBox_5.value())
        sany2 = np.deg2rad(self.spinBox_6.value())
        sanz2 = np.deg2rad(-90 + self.spinBox_7.value())
        transx2 = np.array([[1, 0, 0], [0, np.cos(sanx2), -np.sin(sanx2)], [0, np.sin(sanx2), np.cos(sanx2)]])
        transy2 = np.array([[np.cos(sany2), 0, -np.sin(sany2)], [0, 1, 0], [np.sin(sany2), 0, np.cos(sany2)]])
        transz2 = np.array([[np.cos(sanz2), -np.sin(sanz2), 0], [np.sin(sanz2), np.cos(sanz2), 0], [0, 0, 1]])

        # Compute Carterian and Stereographic Projections Coordinates
        poles_cart = np.empty([len(hklp), 3])
        poles_stereo_x = np.empty([len(hklp)])
        poles_stereo_y = np.empty([len(hklp)])
        dir_cart = np.empty([len(hklp), 3])
        dir_stereo_x = np.empty([len(hklp)])
        dir_stereo_y = np.empty([len(hklp)])

        for jj in range(0, len(hklp), 1):
            poles_cart[jj, 0:3] = (self.Mat_pole * hklp[jj, 0:3].T).T
            poles_cart[jj, 0:3] = poles_cart[jj, 0:3] / np.linalg.norm(poles_cart[jj, 0:3])
            poles_cart[jj, 0:3] = reduce(np.dot, [poles_cart[jj, 0:3], transz, transy, transx, transx2, transy2, transz2])

            poles_stereo_x[jj] = poles_cart[jj, 0] / (1 + np.abs(poles_cart[jj, 2]))
            poles_stereo_y[jj] = poles_cart[jj, 1] / (1 + np.abs(poles_cart[jj, 2]))

        for jj in range(0, len(hkld), 1):
            dir_cart[jj, 0:3] = (self.Mat_dir * hkld[jj, 0:3].T).T
            dir_cart[jj, 0:3] = dir_cart[jj, 0:3] / np.linalg.norm(dir_cart[jj, 0:3])
            dir_cart[jj, 0:3] = reduce(np.dot, [dir_cart[jj, 0:3], transz, transy, transx, transx2, transy2, transz2])

            dir_stereo_x[jj] = dir_cart[jj, 0] / (1 + np.abs(dir_cart[jj, 2]))
            dir_stereo_y[jj] = dir_cart[jj, 1] / (1 + np.abs(dir_cart[jj, 2]))

        # Plotting Stereo
        ax = self.graphicsView.figure.add_subplot(111)

        if self.checkBox.isChecked() and self.checkBox_2.isChecked():
            pp = ax.plot(poles_stereo_x, poles_stereo_y, 'o', color='black', markersize=4, markeredgecolor='blue', label='Poles')
            dd = ax.plot(dir_stereo_x, dir_stereo_y, 's', color='red', markersize=4, markeredgecolor='blue', label='Directions')
            for a in range(0, len(hkld), 1):
                an = str(hklp[a, 0]), str(hklp[a, 1]), str(hklp[a, 2])
                ax.annotate(an[0]+an[1]+an[2], (poles_stereo_x[a], poles_stereo_y[a]))
                an = str(hkld[a, 0]), str(hkld[a, 1]), str(hkld[a, 2])
                ax.annotate(an[0]+an[1]+an[2], (dir_stereo_x[a], dir_stereo_y[a]))

        elif self.checkBox.isChecked():
            pp = ax.plot(poles_stereo_x, poles_stereo_y, 'o', color='black', markersize=4, markeredgecolor='blue', label='Poles')
            for a in range(0, len(hklp), 1):
                an = str(hklp[a, 0]), str(hklp[a, 1]), str(hklp[a, 2])
                ax.annotate(an[0] + an[1] + an[2], (poles_stereo_x[a], poles_stereo_y[a]))
        else:
            dd = ax.plot(dir_stereo_x, dir_stereo_y, 's', color='red', markersize=4, markeredgecolor='blue', label= 'Directions')
            for a in range(0, len(hkld), 1):
                an = str(hkld[a, 0]), str(hkld[a, 1]), str(hkld[a, 2])
                ax.annotate(an[0]+an[1]+an[2], (dir_stereo_x[a], dir_stereo_y[a]))

        blue_line = mlines.Line2D([], [], linestyle='none', marker='s', color='red', markersize=5, markeredgecolor='blue', label='Directions')
        green_line = mlines.Line2D([], [], linestyle='none', marker='o',color='black', markersize=5, markeredgecolor='blue', label='Poles')
        ax.legend(handles=[blue_line, green_line], loc='best')

        self.graphicsView.canvas.draw()
        self.resethit = 1

    def cart2sph(self, x, y, z):
        hxy = np.hypot(x, y)
        r = np.hypot(hxy, z)
        el = np.arctan2(z, hxy)
        az = np.arctan2(np.round(y, 10), np.round(x, 10))
        return az, el, r

    def hklreset(self):
        ax = self.graphicsView.figure.add_subplot(111)

        if self.resethit:
            if self.checkBox.isChecked() and self.checkBox_2.isChecked():
                lines = ax.lines.pop(-1)
                lines = ax.lines.pop(-1)
            else:
                lines = ax.lines.pop(-1)

        self.graphicsView.canvas.draw()

        p1 = np.array([self.spinBox_8.value(), self.spinBox_9.value(), self.spinBox_10.value()])
        p2 = np.array([self.spinBox_11.value(), self.spinBox_12.value(), self.spinBox_13.value()])
        d1 = np.array([self.spinBox_14.value(), self.spinBox_15.value(), self.spinBox_16.value()])
        d2 = np.array([self.spinBox_17.value(), self.spinBox_18.value(), self.spinBox_19.value()])

        self.hklp = np.vstack([p1, p2])
        self.hkld = np.vstack([d1, d2])
        self.resethit = 0  # prevents from hitting reset multiple times and deleting wulf plot

class MatplotlibWidget(QtGui.QWidget, Ui_MetricTens):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        self.canvas.setParent(self)
        self.canvas.setFocus()
        self.canvas.setGeometry(0, 0, 500, 450)  # needed if layout is not specified

        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.setGeometry(0, 0, 500, 25)

        # layout = QtGui.QVBoxLayout()  #layout needs to be added for this to be implemented and working with resize
        # layout.addWidget(self.toolbar)
        # layout.addWidget(self.canvas)
        # layout.setParent(self.canvas)
        # self.setLayout(layout)


        ax = self.figure.add_subplot(111)

        # data = [random.random() for i in range(10)]
        # ax.plot(data, '*-')
        # self.canvas.draw()
        FigureCanvas.updateGeometry(self)
        self.canvas.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)

    def plotWulf(self, mgui):
        self.setVisible(True)

        ax = self.figure.add_subplot(111)
        ax.cla()
        outter = np.arange(0, 2 * np.pi + 0.01, .01)
        xc = np.cos(outter);
        yc = np.sin(outter);
        ax.plot(xc, yc, 'k')
        # ax.set_visible(False)
        # ax.axes.get_xaxis().set_ticks([])
        # ax.axes.get_yaxis().set_ticks([])
        ax.axis('off')
        ax.axis('equal')
        self.figure.tight_layout()
        self.figure.subplots_adjust(top=0.96, right=1, left=0, bottom=0)
        xa = np.array([[-1, 1, 0], [0, 0, 0]])
        ya = np.array([[0, 0, 0], [-1, 1, 0]])
        ang = np.deg2rad(mgui.spinBox_4.value())
        trans = np.matrix([[np.cos(ang), np.sin(ang), 0], [-np.sin(ang), np.cos(ang), 0], [0, 0, 1]])
        transx = trans * np.matrix([1, 0, 0]).T
        transy = trans * np.matrix([0, 1, 0]).T
        nxa = np.array(np.concatenate((transx, -transx), axis=1))
        nya = np.array(np.concatenate((-transy, transy), axis=1))
        if ang == 0:
            ax.plot(xa[0, 0:2], ya[0, 0:2], 'k', xa[1, 0:2], ya[1, 0:2], 'k')
        else:
            ax.plot(nxa[0], nya[0], 'k', nxa[1], nya[1], 'k')

        phi = np.arange(0, np.pi + 0.0001, 0.0001)

        self.canvas.draw()
        for i in range(1, 9, 1):
            Beta = np.arctan((np.tan(i * np.pi / 18) * np.sin(phi)))
            xgc1 = np.sin(phi) * np.tan(np.pi / 4 - Beta / 2)
            xgc2 = -np.sin(phi) * np.tan(np.pi / 4 - Beta / 2)
            ygc = np.cos(phi) * np.tan(np.pi / 4 - Beta / 2)
            comb1 = xgc1
            comb2 = ygc
            combx = np.zeros(len(xgc1))

            comb = np.vstack([comb1, comb2, combx])
            comb3 = xgc2
            comb4 = ygc
            comb0 = np.vstack([comb3, comb4, combx])
            nrotgc = np.array(trans * comb)
            nrotgc2 = np.array(trans * comb0)

            ax.plot(nrotgc[0], nrotgc[1], ':k', nrotgc2[0], nrotgc2[1], ':k')

        for o in range(1, 9, 1):
            alpha = o * np.pi / 18
            rcone = np.sin(alpha)
            xres = np.arange(-rcone, rcone + .001, .001)
            openangle = np.tan(alpha)
            d = 1 / np.cos(alpha)
            sc1 = np.sqrt(openangle ** 2 - xres ** 2)
            sctop = d - sc1
            scbot = -d + sc1
            combsc = np.vstack([xres, scbot, np.zeros(len(scbot))])
            nrotsc = np.array(trans * combsc)
            ax.plot(nrotsc[0], nrotsc[1], ':k', -nrotsc[0], -nrotsc[1], ':k')
        self.canvas.draw()

    def plotData(self, x, y, color):
        ax = self.figure.add_subplot(111)
        ax.plot(x, y, 'o', color=color)
        self.canvas.draw()

if __name__ == "__main__":

    app = QtGui.QApplication.instance()  # Introduced for when running with Canopy (IPython)
    standalone = app is None
    if standalone:
        app = QtGui.QApplication(sys.argv)
        font = app.font()
        font.setPointSize(8)
        app.setFont(font)
    MetricTens = QtGui.QMainWindow()
    ui = Ui_MetricTens()
    mpl = MatplotlibWidget()
    # mpl.show()
    ui.setupUi(MetricTens)
    MetricTens.show()
    if standalone:
        sys.exit(app.exec_())
    else:
        print "We're back with the Qt window still active"
