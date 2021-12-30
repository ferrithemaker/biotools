# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_biotools.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionInformation = QAction(MainWindow)
        self.actionInformation.setObjectName(u"actionInformation")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input_sequence = QTextEdit(self.centralwidget)
        self.input_sequence.setObjectName(u"input_sequence")
        self.input_sequence.setGeometry(QRect(30, 70, 491, 161))
        self.IS_label = QLabel(self.centralwidget)
        self.IS_label.setObjectName(u"IS_label")
        self.IS_label.setGeometry(QRect(30, 40, 121, 16))
        self.output_sequence = QTextEdit(self.centralwidget)
        self.output_sequence.setObjectName(u"output_sequence")
        self.output_sequence.setGeometry(QRect(30, 320, 491, 161))
        self.OS_label = QLabel(self.centralwidget)
        self.OS_label.setObjectName(u"OS_label")
        self.OS_label.setGeometry(QRect(30, 280, 121, 16))
        self.preprocessingButton = QPushButton(self.centralwidget)
        self.preprocessingButton.setObjectName(u"preprocessingButton")
        self.preprocessingButton.setGeometry(QRect(580, 40, 131, 31))
        self.autodetectionButton = QPushButton(self.centralwidget)
        self.autodetectionButton.setObjectName(u"autodetectionButton")
        self.autodetectionButton.setGeometry(QRect(580, 90, 131, 31))
        self.autodetection_label = QLabel(self.centralwidget)
        self.autodetection_label.setObjectName(u"autodetection_label")
        self.autodetection_label.setGeometry(QRect(580, 140, 141, 21))
        self.reverseButton = QPushButton(self.centralwidget)
        self.reverseButton.setObjectName(u"reverseButton")
        self.reverseButton.setGeometry(QRect(580, 180, 131, 31))
        self.complementButton = QPushButton(self.centralwidget)
        self.complementButton.setObjectName(u"complementButton")
        self.complementButton.setGeometry(QRect(580, 230, 131, 31))
        self.RCButton = QPushButton(self.centralwidget)
        self.RCButton.setObjectName(u"RCButton")
        self.RCButton.setGeometry(QRect(580, 280, 181, 31))
        self.transcriptionButton = QPushButton(self.centralwidget)
        self.transcriptionButton.setObjectName(u"transcriptionButton")
        self.transcriptionButton.setGeometry(QRect(580, 330, 131, 31))
        self.translationButton = QPushButton(self.centralwidget)
        self.translationButton.setObjectName(u"translationButton")
        self.translationButton.setGeometry(QRect(580, 380, 131, 31))
        self.countButton = QPushButton(self.centralwidget)
        self.countButton.setObjectName(u"countButton")
        self.countButton.setGeometry(QRect(540, 440, 81, 71))
        self.a_label = QLabel(self.centralwidget)
        self.a_label.setObjectName(u"a_label")
        self.a_label.setGeometry(QRect(630, 430, 16, 16))
        self.c_label = QLabel(self.centralwidget)
        self.c_label.setObjectName(u"c_label")
        self.c_label.setGeometry(QRect(630, 450, 16, 16))
        self.g_label = QLabel(self.centralwidget)
        self.g_label.setObjectName(u"g_label")
        self.g_label.setGeometry(QRect(630, 470, 16, 16))
        self.u_label = QLabel(self.centralwidget)
        self.u_label.setObjectName(u"u_label")
        self.u_label.setGeometry(QRect(630, 490, 16, 16))
        self.t_label = QLabel(self.centralwidget)
        self.t_label.setObjectName(u"t_label")
        self.t_label.setGeometry(QRect(630, 510, 16, 16))
        self.a_count = QLabel(self.centralwidget)
        self.a_count.setObjectName(u"a_count")
        self.a_count.setGeometry(QRect(650, 430, 51, 21))
        self.c_count = QLabel(self.centralwidget)
        self.c_count.setObjectName(u"c_count")
        self.c_count.setGeometry(QRect(650, 450, 51, 21))
        self.g_count = QLabel(self.centralwidget)
        self.g_count.setObjectName(u"g_count")
        self.g_count.setGeometry(QRect(650, 470, 51, 21))
        self.u_count = QLabel(self.centralwidget)
        self.u_count.setObjectName(u"u_count")
        self.u_count.setGeometry(QRect(650, 490, 51, 21))
        self.t_count = QLabel(self.centralwidget)
        self.t_count.setObjectName(u"t_count")
        self.t_count.setGeometry(QRect(650, 510, 51, 21))
        self.length_label = QLabel(self.centralwidget)
        self.length_label.setObjectName(u"length_label")
        self.length_label.setGeometry(QRect(590, 530, 61, 21))
        self.count_length = QLabel(self.centralwidget)
        self.count_length.setObjectName(u"count_length")
        self.count_length.setGeometry(QRect(650, 530, 91, 21))
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionInformation.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.IS_label.setText(QCoreApplication.translate("MainWindow", u"Input sequence:", None))
        self.OS_label.setText(QCoreApplication.translate("MainWindow", u"Output sequence:", None))
        self.preprocessingButton.setText(QCoreApplication.translate("MainWindow", u"Preprocessing", None))
        self.autodetectionButton.setText(QCoreApplication.translate("MainWindow", u"Autodetection", None))
        self.autodetection_label.setText(QCoreApplication.translate("MainWindow", u"Autodetected type", None))
        self.reverseButton.setText(QCoreApplication.translate("MainWindow", u"Reverse", None))
        self.complementButton.setText(QCoreApplication.translate("MainWindow", u"Complement", None))
        self.RCButton.setText(QCoreApplication.translate("MainWindow", u"Reverse + Complement", None))
        self.transcriptionButton.setText(QCoreApplication.translate("MainWindow", u"Transcription", None))
        self.translationButton.setText(QCoreApplication.translate("MainWindow", u"Translation", None))
        self.countButton.setText(QCoreApplication.translate("MainWindow", u"Nucleotids \n"
"Count", None))
        self.a_label.setText(QCoreApplication.translate("MainWindow", u"a:", None))
        self.c_label.setText(QCoreApplication.translate("MainWindow", u"c:", None))
        self.g_label.setText(QCoreApplication.translate("MainWindow", u"g:", None))
        self.u_label.setText(QCoreApplication.translate("MainWindow", u"u:", None))
        self.t_label.setText(QCoreApplication.translate("MainWindow", u"t:", None))
        self.a_count.setText(QCoreApplication.translate("MainWindow", u"valor a", None))
        self.c_count.setText(QCoreApplication.translate("MainWindow", u"valor c", None))
        self.g_count.setText(QCoreApplication.translate("MainWindow", u"valor g", None))
        self.u_count.setText(QCoreApplication.translate("MainWindow", u"valor u", None))
        self.t_count.setText(QCoreApplication.translate("MainWindow", u"valor t", None))
        self.length_label.setText(QCoreApplication.translate("MainWindow", u"length:", None))
        self.count_length.setText(QCoreApplication.translate("MainWindow", u"valor length", None))
    # retranslateUi

