# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(200, 275)
        MainWindow.setMinimumSize(QSize(200, 275))
        MainWindow.setMaximumSize(QSize(200, 275))
        icon = QIcon()
        icon.addFile(u"../icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.nameLabel = QLabel(self.centralwidget)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(60, 10, 81, 16))
        self.buttonBox = QGroupBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 30, 181, 171))
        self.verticalLayoutWidget = QWidget(self.buttonBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 20, 181, 141))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.genNumButton = QPushButton(self.verticalLayoutWidget)
        self.genNumButton.setObjectName(u"genNumButton")

        self.verticalLayout.addWidget(self.genNumButton)

        self.changeFlashImageButton = QPushButton(self.verticalLayoutWidget)
        self.changeFlashImageButton.setObjectName(u"changeFlashImageButton")

        self.verticalLayout.addWidget(self.changeFlashImageButton)

        self.closeSeewoNoteButton = QPushButton(self.verticalLayoutWidget)
        self.closeSeewoNoteButton.setObjectName(u"closeSeewoNoteButton")

        self.verticalLayout.addWidget(self.closeSeewoNoteButton)

        self.checkUpdateButton = QPushButton(self.verticalLayoutWidget)
        self.checkUpdateButton.setObjectName(u"checkUpdateButton")

        self.verticalLayout.addWidget(self.checkUpdateButton)

        self.settingButton = QPushButton(self.centralwidget)
        self.settingButton.setObjectName(u"settingButton")
        self.settingButton.setGeometry(QRect(10, 210, 91, 24))
        self.hideButton = QPushButton(self.centralwidget)
        self.hideButton.setObjectName(u"hideButton")
        self.hideButton.setGeometry(QRect(100, 210, 91, 24))
        self.aboutButton = QPushButton(self.centralwidget)
        self.aboutButton.setObjectName(u"aboutButton")
        self.aboutButton.setGeometry(QRect(10, 240, 91, 24))
        self.closeButton = QPushButton(self.centralwidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(100, 240, 91, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wosea", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Wosea\u5de5\u5177\u7bb1", None))
        self.buttonBox.setTitle(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u5217\u8868", None))
        self.genNumButton.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u53f7\u751f\u6210", None))
        self.changeFlashImageButton.setText(QCoreApplication.translate("MainWindow", u"\u95ea\u5c4f\u56fe\u7247\u4fee\u6539", None))
        self.closeSeewoNoteButton.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u5e0c\u6c83\u767d\u677f", None))
        self.checkUpdateButton.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.settingButton.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.hideButton.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf\u81f3\u6258\u76d8", None))
        self.aboutButton.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.closeButton.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
    # retranslateUi

