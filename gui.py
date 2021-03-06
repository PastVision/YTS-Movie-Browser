# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(563, 544)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.searchText = QtWidgets.QLineEdit(self.centralwidget)
        self.searchText.setObjectName("searchText")
        self.horizontalLayout.addWidget(self.searchText)
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.sortBox = QtWidgets.QComboBox(self.centralwidget)
        self.sortBox.setObjectName("sortBox")
        self.horizontalLayout_4.addWidget(self.sortBox)
        self.sortOrder = QtWidgets.QCheckBox(self.centralwidget)
        self.sortOrder.setObjectName("sortOrder")
        self.horizontalLayout_4.addWidget(self.sortOrder)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.searchResults = QtWidgets.QListWidget(self.centralwidget)
        self.searchResults.setObjectName("searchResults")
        self.verticalLayout.addWidget(self.searchResults)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.movMediumCover = QtWidgets.QLabel(self.centralwidget)
        self.movMediumCover.setText("")
        self.movMediumCover.setPixmap(QtGui.QPixmap("medium-cover.jpg"))
        self.movMediumCover.setScaledContents(False)
        self.movMediumCover.setObjectName("movMediumCover")
        self.horizontalLayout_2.addWidget(self.movMediumCover)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.movTitle = QtWidgets.QLabel(self.centralwidget)
        self.movTitle.setObjectName("movTitle")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.movTitle)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.movYear = QtWidgets.QLabel(self.centralwidget)
        self.movYear.setObjectName("movYear")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.movYear)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.movIMDB = QtWidgets.QLabel(self.centralwidget)
        self.movIMDB.setObjectName("movIMDB")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.movIMDB)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.movRuntime = QtWidgets.QLabel(self.centralwidget)
        self.movRuntime.setObjectName("movRuntime")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.movRuntime)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.movGenre = QtWidgets.QLabel(self.centralwidget)
        self.movGenre.setObjectName("movGenre")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.movGenre)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.movSummary = QtWidgets.QTextBrowser(self.centralwidget)
        self.movSummary.setObjectName("movSummary")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.movSummary)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.movTrailer = QtWidgets.QLabel(self.centralwidget)
        self.movTrailer.setTextFormat(QtCore.Qt.RichText)
        self.movTrailer.setObjectName("movTrailer")
        self.movTrailer.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.movTrailer.setOpenExternalLinks(True)
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.movTrailer)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.movLang = QtWidgets.QLabel(self.centralwidget)
        self.movLang.setObjectName("movLang")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.movLang)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.movQualCount = QtWidgets.QLabel(self.centralwidget)
        self.movQualCount.setObjectName("movQualCount")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.movQualCount)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.movQuals = QtWidgets.QComboBox(self.centralwidget)
        self.movQuals.setObjectName("movQuals")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.movQuals)
        self.horizontalLayout_2.addLayout(self.formLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(330, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.copyMagnet = QtWidgets.QPushButton(self.centralwidget)
        self.copyMagnet.setObjectName("copyMagnet")
        self.horizontalLayout_7.addWidget(self.copyMagnet)
        self.downloadMagnet = QtWidgets.QPushButton(self.centralwidget)
        self.downloadMagnet.setObjectName("downloadMagnet")
        self.horizontalLayout_7.addWidget(self.downloadMagnet)
        self.downloadTorrent = QtWidgets.QPushButton(self.centralwidget)
        self.downloadTorrent.setObjectName("downloadTorrent")
        self.horizontalLayout_7.addWidget(self.downloadTorrent)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YTS Movie Browser by PastVision"))
        self.label.setText(_translate("MainWindow", "Enter a keyword to search: "))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.label_4.setText(_translate("MainWindow", "Select a movie from Results:"))
        self.label_10.setText(_translate("MainWindow", "Sort Results by:"))
        self.sortOrder.setText(_translate("MainWindow", "Ascending"))
        self.label_5.setText(_translate("MainWindow", "Name:"))
        self.movTitle.setText(_translate("MainWindow", ""))
        self.label_7.setText(_translate("MainWindow", "Release Year:"))
        self.movYear.setText(_translate("MainWindow", ""))
        self.label_8.setText(_translate("MainWindow", "IMdB Score:"))
        self.movIMDB.setText(_translate("MainWindow", ""))
        self.label_9.setText(_translate("MainWindow", "Runtime:"))
        self.movRuntime.setText(_translate("MainWindow", ""))
        self.label_11.setText(_translate("MainWindow", "Genres:"))
        self.movGenre.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", "Summary:"))
        self.movSummary.setHtml(_translate("MainWindow", ""))
        self.label_13.setText(_translate("MainWindow", "Trailer:"))
        self.movTrailer.setText(_translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", "Language:"))
        self.movLang.setText(_translate("MainWindow", ""))
        self.label_6.setText(_translate("MainWindow", "Available qualities:"))
        self.movQualCount.setText(_translate("MainWindow", ""))
        self.label_12.setText(_translate("MainWindow", "Select quality:"))
        self.copyMagnet.setText(_translate("MainWindow", "Copy Magnet to clipboard"))
        self.downloadMagnet.setText(_translate("MainWindow", "Magnet"))
        self.downloadTorrent.setText(_translate("MainWindow", "Torrent"))

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''