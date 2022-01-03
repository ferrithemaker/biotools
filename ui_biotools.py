# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_biotools.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionInformation = QAction(MainWindow)
        self.actionInformation.setObjectName(u"actionInformation")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionExit_2 = QAction(MainWindow)
        self.actionExit_2.setObjectName(u"actionExit_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.t_label = QLabel(self.centralwidget)
        self.t_label.setObjectName(u"t_label")

        self.gridLayout.addWidget(self.t_label, 14, 2, 1, 2)

        self.autodetection_label = QLabel(self.centralwidget)
        self.autodetection_label.setObjectName(u"autodetection_label")

        self.gridLayout.addWidget(self.autodetection_label, 2, 1, 1, 5)

        self.u_label = QLabel(self.centralwidget)
        self.u_label.setObjectName(u"u_label")

        self.gridLayout.addWidget(self.u_label, 12, 2, 1, 1)

        self.a_label = QLabel(self.centralwidget)
        self.a_label.setObjectName(u"a_label")

        self.gridLayout.addWidget(self.a_label, 9, 2, 1, 2)

        self.g_count = QLabel(self.centralwidget)
        self.g_count.setObjectName(u"g_count")

        self.gridLayout.addWidget(self.g_count, 11, 4, 1, 1)

        self.t_count = QLabel(self.centralwidget)
        self.t_count.setObjectName(u"t_count")

        self.gridLayout.addWidget(self.t_count, 14, 4, 1, 1)

        self.c_label = QLabel(self.centralwidget)
        self.c_label.setObjectName(u"c_label")

        self.gridLayout.addWidget(self.c_label, 10, 2, 1, 2)

        self.length_label = QLabel(self.centralwidget)
        self.length_label.setObjectName(u"length_label")

        self.gridLayout.addWidget(self.length_label, 16, 2, 1, 1)

        self.OS_label = QLabel(self.centralwidget)
        self.OS_label.setObjectName(u"OS_label")

        self.gridLayout.addWidget(self.OS_label, 5, 0, 1, 1)

        self.input_sequence = QTextEdit(self.centralwidget)
        self.input_sequence.setObjectName(u"input_sequence")

        self.gridLayout.addWidget(self.input_sequence, 1, 0, 3, 1)

        self.preprocessingButton = QPushButton(self.centralwidget)
        self.preprocessingButton.setObjectName(u"preprocessingButton")

        self.gridLayout.addWidget(self.preprocessingButton, 0, 1, 1, 5)

        self.a_count = QLabel(self.centralwidget)
        self.a_count.setObjectName(u"a_count")

        self.gridLayout.addWidget(self.a_count, 9, 4, 1, 1)

        self.reverseButton = QPushButton(self.centralwidget)
        self.reverseButton.setObjectName(u"reverseButton")

        self.gridLayout.addWidget(self.reverseButton, 3, 1, 1, 5)

        self.complementButton = QPushButton(self.centralwidget)
        self.complementButton.setObjectName(u"complementButton")

        self.gridLayout.addWidget(self.complementButton, 4, 1, 1, 5)

        self.transcriptionButton = QPushButton(self.centralwidget)
        self.transcriptionButton.setObjectName(u"transcriptionButton")

        self.gridLayout.addWidget(self.transcriptionButton, 6, 1, 1, 5)

        self.IS_label = QLabel(self.centralwidget)
        self.IS_label.setObjectName(u"IS_label")

        self.gridLayout.addWidget(self.IS_label, 0, 0, 1, 1)

        self.translationButton = QPushButton(self.centralwidget)
        self.translationButton.setObjectName(u"translationButton")

        self.gridLayout.addWidget(self.translationButton, 7, 1, 1, 5)

        self.output_sequence = QTextEdit(self.centralwidget)
        self.output_sequence.setObjectName(u"output_sequence")

        self.gridLayout.addWidget(self.output_sequence, 6, 0, 7, 1)

        self.g_label = QLabel(self.centralwidget)
        self.g_label.setObjectName(u"g_label")

        self.gridLayout.addWidget(self.g_label, 11, 2, 1, 1)

        self.u_count = QLabel(self.centralwidget)
        self.u_count.setObjectName(u"u_count")

        self.gridLayout.addWidget(self.u_count, 12, 4, 1, 1)

        self.autodetectionButton = QPushButton(self.centralwidget)
        self.autodetectionButton.setObjectName(u"autodetectionButton")

        self.gridLayout.addWidget(self.autodetectionButton, 1, 1, 1, 5)

        self.revCompButton = QPushButton(self.centralwidget)
        self.revCompButton.setObjectName(u"revCompButton")

        self.gridLayout.addWidget(self.revCompButton, 5, 1, 1, 5)

        self.count_length = QLabel(self.centralwidget)
        self.count_length.setObjectName(u"count_length")

        self.gridLayout.addWidget(self.count_length, 16, 4, 1, 1)

        self.c_count = QLabel(self.centralwidget)
        self.c_count.setObjectName(u"c_count")

        self.gridLayout.addWidget(self.c_count, 10, 4, 1, 1)

        self.countButton = QPushButton(self.centralwidget)
        self.countButton.setObjectName(u"countButton")

        self.gridLayout.addWidget(self.countButton, 8, 1, 1, 5)

        self.copy2inputButton = QPushButton(self.centralwidget)
        self.copy2inputButton.setObjectName(u"copy2inputButton")

        self.gridLayout.addWidget(self.copy2inputButton, 15, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionInformation.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionExit_2.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.t_label.setText(QCoreApplication.translate("MainWindow", u"t:", None))
        self.autodetection_label.setText(QCoreApplication.translate("MainWindow", u"Autodetected type", None))
        self.u_label.setText(QCoreApplication.translate("MainWindow", u"u:", None))
        self.a_label.setText(QCoreApplication.translate("MainWindow", u"a:", None))
        self.g_count.setText(QCoreApplication.translate("MainWindow", u"valor g", None))
        self.t_count.setText(QCoreApplication.translate("MainWindow", u"valor t", None))
        self.c_label.setText(QCoreApplication.translate("MainWindow", u"c:", None))
        self.length_label.setText(QCoreApplication.translate("MainWindow", u"Length:", None))
        self.OS_label.setText(QCoreApplication.translate("MainWindow", u"Output sequence:", None))
        self.preprocessingButton.setText(QCoreApplication.translate("MainWindow", u"Preprocessing", None))
        self.a_count.setText(QCoreApplication.translate("MainWindow", u"valor a", None))
        self.reverseButton.setText(QCoreApplication.translate("MainWindow", u"Reverse", None))
        self.complementButton.setText(QCoreApplication.translate("MainWindow", u"Complement", None))
        self.transcriptionButton.setText(QCoreApplication.translate("MainWindow", u"Transcription", None))
        self.IS_label.setText(QCoreApplication.translate("MainWindow", u"Input sequence:", None))
        self.translationButton.setText(QCoreApplication.translate("MainWindow", u"Translation", None))
        self.g_label.setText(QCoreApplication.translate("MainWindow", u"g:", None))
        self.u_count.setText(QCoreApplication.translate("MainWindow", u"valor u", None))
        self.autodetectionButton.setText(QCoreApplication.translate("MainWindow", u"Autodetection", None))
        self.revCompButton.setText(QCoreApplication.translate("MainWindow", u"Reverse + Complement", None))
        self.count_length.setText(QCoreApplication.translate("MainWindow", u"valor length", None))
        self.c_count.setText(QCoreApplication.translate("MainWindow", u"valor c", None))
        self.countButton.setText(QCoreApplication.translate("MainWindow", u"Nucleotids \n"
"Count", None))
        self.copy2inputButton.setText(QCoreApplication.translate("MainWindow", u"Copy sequence to input", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

