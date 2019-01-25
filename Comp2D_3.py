# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Comp2D_1.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!
import sys
import os
import time
from matplotlib.figure import Figure
import matplotlib.lines as mlines
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np

owd=os.getcwd()


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
        MainWindow.resize(1163, 750)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.progressBar = QtGui.QProgressBar(self.centralWidget)
        self.progressBar.setGeometry(QtCore.QRect(1040, 670, 108, 20))
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(220, 30, 281, 141))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)

        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 5, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 5, 1, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(self.groupBox)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.gridLayout.addWidget(self.comboBox_3, 2, 1, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.groupBox)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout.addWidget(self.spinBox, 6, 3, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.groupBox)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.gridLayout.addWidget(self.comboBox_2, 6, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton.setChecked(True)
        self.gridLayout.addWidget(self.radioButton, 5, 0, 2, 1)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_2.setChecked(True)

        self.gridLayout.addWidget(self.radioButton_2, 1, 0, 2, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 30, 171, 141))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        # self.gridLayout_2.setMargin(11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_3.clicked.connect(lambda: self.FileBrowse(self.centralWidget,'Baseline'))
        self.comboBox_6 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.comboBox_6.currentIndexChanged.connect(lambda: self.comboBox_6.setCurrentIndex(0))

        self.comboBox_7 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.comboBox_7.currentIndexChanged.connect(lambda: self.comboBox_7.setCurrentIndex(0))

        self.gridLayout_2.addWidget(self.comboBox_6, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.comboBox_7, 3, 0, 1, 1)


        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.clicked.connect(lambda: self.FileBrowse(self.centralWidget,'Test'))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 190, 511, 471))
        self.groupBox_3.setFlat(False)
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))


        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.comboBox_4 = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_4.setGeometry(QtCore.QRect(240, 30, 141, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.DistMetricPlot = DMPlot(self.groupBox_3)
        self.DistMetricPlot.setGeometry(QtCore.QRect(10, 60, 491, 400))
        self.DistMetricPlot.setObjectName(_fromUtf8("DistMetricPlot"))
        self.comboBox_5 = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_5.setGeometry(QtCore.QRect(420, 30, 51, 22))
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))

        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(400, 10, 101, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_4.setGeometry(QtCore.QRect(530, 20, 621, 641))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))

        self.pushButton_4 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_4.setGeometry( 50, 30, 60, 25)
        self.pushButton_4.clicked.connect(lambda: self.CompDM())

        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_4)
        # self.gridLayout_3.setMargin(11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.comboBox = QtGui.QComboBox(self.groupBox_4)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.currentIndexChanged.connect(lambda: self.ZScorePlot.plotZscore(self.z[:,:,self.comboBox.currentIndex()]))

        self.gridLayout_3.addWidget(self.comboBox, 0, 0, 1, 1)
        self.ZScorePlot = ZSPlot(self.groupBox_4)
        self.ZScorePlot.setObjectName(_fromUtf8("ZScorePlot"))
        self.gridLayout_3.addWidget(self.ZScorePlot, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1163, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menuBar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Comp2D", None))
        MainWindow.setWindowIcon(QtGui.QIcon('Python1.png'))

        self.groupBox.setTitle(_translate("MainWindow", "Z-Score Grid Preference", None))
        self.label_3.setText(_translate("MainWindow", "Radial Increment", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Slice Width</p></body></html>", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Square Side Length</p></body></html>", None))
        self.radioButton.setText(_translate("MainWindow", "Polar", None))
        self.radioButton_2.setText(_translate("MainWindow", "Square", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "File Input", None))
        self.pushButton_3.setText(_translate("MainWindow", "Select Baseline Data", None))
        self.pushButton.setText(_translate("MainWindow", "Select Test Data", None))
        self.pushButton_4.setText(_translate("MainWindow", "Compute", None))

        self.groupBox_3.setTitle(_translate("MainWindow", "Distance Metric", None))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Sum of Absolute Values", None))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Sum of Squared Errors", None))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "95%", None))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "50%", None))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "68%", None))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "75%", None))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "90%", None))
        self.comboBox_5.setItemText(5, _translate("MainWindow", "99%", None))

        self.comboBox_3.setItemText(0, _translate("MainWindow", "0", None))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "2", None))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "3", None))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "4", None))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "5", None))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "6", None))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "7", None))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "8", None))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "9", None))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "10", None))


        self.label_4.setText(_translate("MainWindow", "Confidence Interval", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Pixel Z-Score", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))


    def FileBrowse(self,pon,id):
        # Files= QtGui.QFileDialog.getOpenFileNames()
        dlg = QtGui.QFileDialog()
        # Files = dlg.getOpenFileNames(pon, 'Select ' + id + ' Image(s)', owd, id + " image files (*.tif *.tiff)")


        if id=='Baseline':
            if self.comboBox_6.currentIndex()==-1:
                print 'Default Directory'
                self.Files = dlg.getOpenFileNames(pon, 'Select ' + id + ' Image(s)', owd, id + " image files (*.tif *.tiff)")
                self.bndir = os.path.split(self.Files[0][0])[0]
            elif self.bndir==0:
                self.Files = dlg.getOpenFileNames(pon, 'Select ' + id + ' Image(s)', owd, id + " image files (*.tif *.tiff)")
                self.bndir = os.path.split(self.Files[0][0])[0]

            else:
                self.Files = dlg.getOpenFileNames(pon, 'Select ' + id + ' Image(s)', self.bndir, id + " image files (*.tif *.tiff)")
                self.bndir = os.path.split(self.Files[0][0])[0]

            if self.Files[0] != []:
                self.ImgListB=self.Files[:]
                self.comboBox_6.clear()
                for i in range(0,len(self.Files[0])):
                    self.comboBox_6.addItems([(os.path.split(self.Files[0][i])[1])])
            else:
                self.bndir == owd

        elif id=='Test':

            if self.comboBox_7.currentIndex()==-1:
                print 'Default Directory'
                self.Files = dlg.getOpenFileNames(pon, 'Select ' + id + ' Image(s)', owd, id + " image files (*.tif *.tiff)")
                self.endir = os.path.split(self.Files[0][0])[0]

            elif self.endir==0:
                self.Files = dlg.getOpenFileNames(pon, 'Select ' + id + ' Image(s)', owd, id + " image files (*.tif *.tiff)")
                self.endir = os.path.split(self.Files[0][0])[0]

            else:
                self.Files = dlg.getOpenFileNames(pon, 'Select ' + id + ' Image(s)', self.endir, id + " image files (*.tif *.tiff)")
                self.endir = os.path.split(self.Files[0][0])[0]

            if self.Files[0] != []:
                self.ImgListE=self.Files[:]
                self.comboBox_7.clear()
                self.comboBox.clear()
                for i in range(0,len(self.Files[0])):
                    self.comboBox.addItems([(os.path.split(self.Files[0][i])[1])])
                    self.comboBox_7.addItems([(os.path.split(self.Files[0][i])[1])])
            elif self.Files[0] != [] and self.endir !=[]:
                self.endir = owd

    def CompDM(self):
        try:
            self.ImgListB
        except AttributeError:
            print "Select Baseline Image(s)!"
        try:
            self.ImgListE
        except AttributeError:
            print "Select Test Image(s)!"

        self.p1 = len(self.ImgListB[0])
        self.p2 = len(self.ImgListE[0])


        self.ImgB = np.zeros([2048, 2048, self.p1], dtype=np.float32)
        self.Imgb = np.zeros([self.p1, 2048 * 2048], dtype=np.float32)
        self.d = np.zeros([self.p1, self.p1], dtype=np.float32)
        self.z = np.zeros([2048, 2048, self.p2], dtype=np.float32)
        self.time1 = time.time()
        self.Img = np.zeros([self.p2, 2048 * 2048], dtype=np.float32)
        self.ImgE = np.zeros([2048, 2048, self.p2], dtype=np.float32)
        self.e = np.zeros([self.p1, self.p2], dtype=np.float32)
        self.zstd = np.zeros([self.p1, self.p2], dtype=np.float32)

        self.progressBar.setValue(0)
        self.RBaseline(self.ImgListB[0], self.p1)
        self.RTest(self.ImgListE[0], self.p2)
        self.Zscore(self.p2)
        self.DistMetric(self.p1, self.p2)

    def ReadTif(self, p):
        File = open(p, 'rb')
        Npix = 2048 * 2048
        time0 = time.time()
        image = np.array(np.frombuffer(File.read(Npix * 4), dtype=np.float32), dtype=np.int32)  # reads Tif image
        image2 = np.reshape(image, (2048, 2048))
        co = image2[:, 0:2]
        image3 = np.concatenate([image2[:, 2:2048], co], axis=1)
        File.close()
        return image3, image, time0

    def RBaseline(self,p,p1):
        for i in range(0, p1):
            self.progressBar.setValue(i/float(4*self.p1+3*self.p2)*100)
            image3, image, time0 = self.ReadTif(p[i])
            self.Imgb[i][:] = image[:]
            image2 = np.reshape(self.Imgb[:][:][i], (2048, 2048))
            co = image2[:, 0:2]
            image3 = np.concatenate([image2[:, 2:2048], co], axis=1)
            self.ImgB[:, :, i] = image3  # check to see if {} list makes this a faster approach?
            print i
        # print image3

    def RTest(self, po, p2):

        for k in range(0, p2):
            self.progressBar.setValue((k+self.p1)/float(4*self.p1+3*self.p2)*100)

            image3, image, time0 = self.ReadTif(po[k])
            self.Img[k][:] = image[:]
            image2 = np.reshape(self.Img[:][:][k], (2048, 2048))
            co = image2[:, 0:2]
            image3 = np.concatenate([image2[:, 2:2048], co], axis=1)
            self.ImgE[:, :, k] = image3
            print k
        # print image3

    def Zscore(self,p2):

        Imgavg = np.mean(self.ImgB, axis=2, dtype=np.float32)
        if p2==1:
            Imgstd=np.sqrt(self.ImgB)
        else:
            Imgstd = np.std(self.ImgB, axis=2, dtype=np.float32, ddof=1)
        Nor = 2048 ** 2
        alpha = 1
        for m in range(0, p2):
            self.progressBar.setValue((self.p1+self.p2+m)/float(4*self.p1+3*self.p2)*100)
            Errs = self.ImgE[:, :, m] - Imgavg
            self.z[:, :, m] = Errs / Imgstd
        low_limit = 0.0082
        up_limit = .992
        k = 0
        m1 = 2048
        n1 = 2048

        ImgID = np.sort(self.Img[k, :])
        v_min = ImgID[int(np.ceil(low_limit * m1 * n1))]
        v_max = ImgID[int(np.ceil(up_limit * m1 * n1))]
        z1 = (self.z[:,:,self.comboBox.currentIndex()] - v_min) / (v_max - v_min)
        self.ZScorePlot.plotZscore(z1)

    def DistMetric(self,p1,p2):
        print 'Computing DM'
        alpha = self.comboBox_4.currentIndex()+1
        for h in range(0, p1):  # stricly for baseline
            for f in range(0, p1):
                self.d[h, f] = np.sum(abs(self.Imgb[f, :] - self.Imgb[h, :])**alpha, axis=0, dtype=np.float32)
            self.progressBar.setValue((self.p1 + self.p2 * 2 + h + f) / float(4 * self.p1 + 3 * self.p2) * 100)

        if p1==1:
            davg = 0
            dstd = 0
        else:
            davg = np.sum(self.d, axis=0, dtype=np.float32) / (p1 - 1)
            dstd = np.sqrt((p1 - 1)**-1 * np.sum(abs(self.d - davg) ** 2, axis=0))

        for y in range(0, p2):
            for s in range(0, p1):
                self.e[s, y] = np.sum(abs(self.Img[y, :] - self.Imgb[s, :])**alpha, dtype=np.float32)
            if p1==1:
                self.zstd[:, y] = self.e[:, y]
            else:
                self.zstd[:, y] = (self.e[:, y] - np.mean(davg, dtype=np.float32)) / np.mean(dstd, dtype=np.float32)
            self.progressBar.setValue((self.p1*3 + self.p2 * 2 + y + s) / float(4 * self.p1 + 3 * self.p2) * 100)

        zavg = np.mean(self.zstd, axis=0, dtype=np.float32)
        z1 = self.comboBox_5.currentIndex()
        print z1

        if p1==1:
            bstd=np.sum(np.sqrt(abs(self.Imgb)))
        else:
            bstd=0
        DMPlot.plotDM(self.DistMetricPlot, range(1, p2 + 1), zavg, self.zstd, z1, bstd)
        self.progressBar.setValue(100)

class DMPlot(QtGui.QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super(DMPlot, self).__init__(parent)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(self)
        self.canvas.setFocus()
        self.canvas.setGeometry(0, 0, 500, 450)  # needed if layout is not specified
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.setGeometry(0, 0, 500, 25)

        layout = QtGui.QVBoxLayout()  #layout needs to be added for this to be implemented and working with resize
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.setParent(self.canvas)
        self.setLayout(layout)

        ax = self.figure.add_subplot(111)

        FigureCanvas.updateGeometry(self)
        self.canvas.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)

    def plotDM(self,x,y,zstd,z1, bstd):
        ax = self.figure.add_subplot(111)
        ax.cla()

        if z1==1:
            zz=0.67449
        elif z1==2:
            zz=1
        elif z1==3:
            zz=1.15035
        elif z1==4:
            zz=1.64485
        elif z1==5:
            zz=2.57583
        else:
            zz=1.95996

        print zz
        if bstd != 0:
            ax.errorbar(x[1:-1], y[1:-1], bstd/2048**2 * zz, fmt='-o', ecolor='g', capsize=5) # std of the distance metric, not the best estimator since it cant
            print 'Skip'
        else:
            ax.errorbar(x, y, np.std(zstd, ddof=1, axis=0)*zz, fmt='-o', ecolor='g', capsize=5)

        ax.set
        ax.set_xlabel('File Number')
        ax.set_ylabel('Distance Metric')
        self.figure.tight_layout()
        self.canvas.draw()

class ZSPlot(QtGui.QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ZSPlot, self).__init__(parent)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(self)
        self.canvas.setFocus()
        self.canvas.setGeometry(0, 0, 500, 450)  # needed if layout is not specified
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.setGeometry(0, 0, 500, 25)


        layout = QtGui.QVBoxLayout()  #layout needs to be added for this to be implemented and working with resize
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.setParent(self.canvas)
        self.setLayout(layout)

        ax1 = self.figure.add_subplot(111)
        ax1.axis('off')

        FigureCanvas.updateGeometry(self)
        self.canvas.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)

    def plotZscore(self, Img):
        ax = self.figure.add_subplot(111)

        ax.imshow(Img)
        ax.axis('off')
        self.figure.tight_layout()

        self.canvas.draw()
    print 'ImgZScorePlot Done'

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("Python1.png"))

    Comp2D = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Comp2D)
    Comp2D.show()
    sys.exit(app.exec_())

