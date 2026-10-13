# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(520, 520)
        MainWindow.setMinimumSize(QSize(520, 520))
        MainWindow.setMaximumSize(QSize(520, 520))
        MainWindow.setStyleSheet(u"QMainWindow { background-color: #e9ecee; }")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.card = QFrame(self.centralwidget)
        self.card.setObjectName(u"card")
        self.card.setGeometry(QRect(16, 16, 488, 488))
        self.card.setStyleSheet(u"QFrame#card { background-color: #ffffff; border-radius: 14px; }")
        self.labelTitle = QLabel(self.card)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setGeometry(QRect(20, 14, 200, 24))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet(u"color: #263238;")
        self.statScore = QFrame(self.card)
        self.statScore.setObjectName(u"statScore")
        self.statScore.setGeometry(QRect(304, 6, 78, 48))
        self.statScore.setStyleSheet(u"QFrame#statScore { background-color: #e9ecee; border-radius: 8px; }")
        self.labelScoreTitle = QLabel(self.statScore)
        self.labelScoreTitle.setObjectName(u"labelScoreTitle")
        self.labelScoreTitle.setGeometry(QRect(0, 4, 78, 14))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(9)
        self.labelScoreTitle.setFont(font1)
        self.labelScoreTitle.setStyleSheet(u"color: #7a8a98;")
        self.labelScoreTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelScoreValue = QLabel(self.statScore)
        self.labelScoreValue.setObjectName(u"labelScoreValue")
        self.labelScoreValue.setGeometry(QRect(0, 20, 78, 20))
        self.labelScoreValue.setFont(font)
        self.labelScoreValue.setStyleSheet(u"color: #1976d2;")
        self.labelScoreValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.statRecord = QFrame(self.card)
        self.statRecord.setObjectName(u"statRecord")
        self.statRecord.setGeometry(QRect(390, 6, 78, 48))
        self.statRecord.setStyleSheet(u"QFrame#statRecord { background-color: #e9ecee; border-radius: 8px; }")
        self.labelRecordTitle = QLabel(self.statRecord)
        self.labelRecordTitle.setObjectName(u"labelRecordTitle")
        self.labelRecordTitle.setGeometry(QRect(0, 4, 78, 14))
        self.labelRecordTitle.setFont(font1)
        self.labelRecordTitle.setStyleSheet(u"color: #7a8a98;")
        self.labelRecordTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelRecordValue = QLabel(self.statRecord)
        self.labelRecordValue.setObjectName(u"labelRecordValue")
        self.labelRecordValue.setGeometry(QRect(0, 20, 78, 20))
        self.labelRecordValue.setFont(font)
        self.labelRecordValue.setStyleSheet(u"color: #f57c00;")
        self.labelRecordValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.contentArea = QFrame(self.card)
        self.contentArea.setObjectName(u"contentArea")
        self.contentArea.setGeometry(QRect(20, 70, 448, 374))
        self.contentArea.setStyleSheet(u"QFrame#contentArea { background-color: #e8ebed; border-radius: 12px; }")
        self.labelReady = QLabel(self.contentArea)
        self.labelReady.setObjectName(u"labelReady")
        self.labelReady.setGeometry(QRect(124, 130, 200, 26))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(13)
        font2.setBold(True)
        self.labelReady.setFont(font2)
        self.labelReady.setStyleSheet(u"color: #263238;")
        self.labelReady.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelRules = QLabel(self.contentArea)
        self.labelRules.setObjectName(u"labelRules")
        self.labelRules.setGeometry(QRect(24, 175, 400, 50))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        self.labelRules.setFont(font3)
        self.labelRules.setStyleSheet(u"color: #607d8b;")
        self.labelRules.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelRules.setWordWrap(True)
        self.btnStart = QPushButton(self.contentArea)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setGeometry(QRect(144, 265, 160, 44))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.btnStart.setFont(font4)
        self.btnStart.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnStart.setStyleSheet(u"QPushButton {\n"
"    background-color: #1976d2;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover { background-color: #1565c0; }\n"
"QPushButton:pressed { background-color: #0d47a1; }")
        self.progressBar = QProgressBar(self.card)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 460, 448, 8))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    background-color: #e9ecee;\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #1976d2;\n"
"    border-radius: 4px;\n"
"}")
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(100)
        self.progressBar.setTextVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0439\u043c\u0430\u0439 \u043a\u0432\u0430\u0434\u0440\u0430\u0442", None))
        self.labelTitle.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0439\u043c\u0430\u0439 \u043a\u0432\u0430\u0434\u0440\u0430\u0442", None))
        self.labelScoreTitle.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0447\u0451\u0442", None))
        self.labelScoreValue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.labelRecordTitle.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043a\u043e\u0440\u0434", None))
        self.labelRecordValue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.labelReady.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0442\u043e\u0432?", None))
        self.labelRules.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0438\u043a\u0430\u0439 \u043f\u043e \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0443 \u043a\u0430\u043a \u043c\u043e\u0436\u043d\u043e \u0431\u044b\u0441\u0442\u0440\u0435\u0435. \u0423\u0441\u043f\u0435\u0439 \u043f\u043e\u0439\u043c\u0430\u0442\u044c \u0435\u0433\u043e \u043f\u043e\u043a\u0430 \u0432\u0440\u0435\u043c\u044f \u043d\u0435 \u0432\u044b\u0448\u043b\u043e", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0438\u0433\u0440\u0443", None))
    # retranslateUi

