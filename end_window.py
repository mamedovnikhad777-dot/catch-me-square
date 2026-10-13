# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'end_window.ui'
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

class Ui_EndWindow(object):
    def setupUi(self, EndWindow):
        if not EndWindow.objectName():
            EndWindow.setObjectName(u"EndWindow")
        EndWindow.resize(520, 520)
        EndWindow.setMinimumSize(QSize(520, 520))
        EndWindow.setMaximumSize(QSize(520, 520))
        EndWindow.setStyleSheet(u"QMainWindow { background-color: #e9ecee; }")
        self.centralwidget = QWidget(EndWindow)
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
        self.labelScoreTitle.setAlignment(Qt.AlignCenter)
        self.labelScoreValue = QLabel(self.statScore)
        self.labelScoreValue.setObjectName(u"labelScoreValue")
        self.labelScoreValue.setGeometry(QRect(0, 20, 78, 20))
        self.labelScoreValue.setFont(font)
        self.labelScoreValue.setStyleSheet(u"color: #1976d2;")
        self.labelScoreValue.setAlignment(Qt.AlignCenter)
        self.statRecord = QFrame(self.card)
        self.statRecord.setObjectName(u"statRecord")
        self.statRecord.setGeometry(QRect(390, 6, 78, 48))
        self.statRecord.setStyleSheet(u"QFrame#statRecord { background-color: #e9ecee; border-radius: 8px; }")
        self.labelRecordTitle = QLabel(self.statRecord)
        self.labelRecordTitle.setObjectName(u"labelRecordTitle")
        self.labelRecordTitle.setGeometry(QRect(0, 4, 78, 14))
        self.labelRecordTitle.setFont(font1)
        self.labelRecordTitle.setStyleSheet(u"color: #7a8a98;")
        self.labelRecordTitle.setAlignment(Qt.AlignCenter)
        self.labelRecordValue = QLabel(self.statRecord)
        self.labelRecordValue.setObjectName(u"labelRecordValue")
        self.labelRecordValue.setGeometry(QRect(0, 20, 78, 20))
        self.labelRecordValue.setFont(font)
        self.labelRecordValue.setStyleSheet(u"color: #f57c00;")
        self.labelRecordValue.setAlignment(Qt.AlignCenter)
        self.contentArea = QFrame(self.card)
        self.contentArea.setObjectName(u"contentArea")
        self.contentArea.setGeometry(QRect(20, 70, 448, 374))
        self.contentArea.setStyleSheet(u"QFrame#contentArea { background-color: #e8ebed; border-radius: 12px; }")
        self.labelGameOver = QLabel(self.contentArea)
        self.labelGameOver.setObjectName(u"labelGameOver")
        self.labelGameOver.setGeometry(QRect(124, 100, 200, 28))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.labelGameOver.setFont(font2)
        self.labelGameOver.setStyleSheet(u"color: #263238;")
        self.labelGameOver.setAlignment(Qt.AlignCenter)
        self.labelMessage = QLabel(self.contentArea)
        self.labelMessage.setObjectName(u"labelMessage")
        self.labelMessage.setGeometry(QRect(24, 140, 400, 40))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        self.labelMessage.setFont(font3)
        self.labelMessage.setStyleSheet(u"color: #607d8b;")
        self.labelMessage.setAlignment(Qt.AlignCenter)
        self.labelMessage.setWordWrap(True)
        self.labelFinalScore = QLabel(self.contentArea)
        self.labelFinalScore.setObjectName(u"labelFinalScore")
        self.labelFinalScore.setGeometry(QRect(174, 190, 100, 60))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(38)
        font4.setBold(True)
        self.labelFinalScore.setFont(font4)
        self.labelFinalScore.setStyleSheet(u"color: #1976d2;")
        self.labelFinalScore.setAlignment(Qt.AlignCenter)
        self.btnPlayAgain = QPushButton(self.contentArea)
        self.btnPlayAgain.setObjectName(u"btnPlayAgain")
        self.btnPlayAgain.setGeometry(QRect(144, 270, 160, 44))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(11)
        font5.setBold(True)
        self.btnPlayAgain.setFont(font5)
        self.btnPlayAgain.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnPlayAgain.setStyleSheet(u"QPushButton {\n"
"    background-color: #1976d2;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover { background-color: #1565c0; }\n"
"QPushButton:pressed { background-color: #0d47a1; }")
        self.progressBar = QProgressBar(self.card)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 449, 330, 8))
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
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.btnRestart = QPushButton(self.card)
        self.btnRestart.setObjectName(u"btnRestart")
        self.btnRestart.setGeometry(QRect(362, 436, 106, 34))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(10)
        font6.setBold(True)
        self.btnRestart.setFont(font6)
        self.btnRestart.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnRestart.setStyleSheet(u"QPushButton {\n"
"    background-color: #1976d2;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover { background-color: #1565c0; }\n"
"QPushButton:pressed { background-color: #0d47a1; }")
        EndWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EndWindow)

        QMetaObject.connectSlotsByName(EndWindow)
    # setupUi

    def retranslateUi(self, EndWindow):
        EndWindow.setWindowTitle(QCoreApplication.translate("EndWindow", u"\u041f\u043e\u0439\u043c\u0430\u0439 \u043a\u0432\u0430\u0434\u0440\u0430\u0442", None))
        self.labelTitle.setText(QCoreApplication.translate("EndWindow", u"\u041f\u043e\u0439\u043c\u0430\u0439 \u043a\u0432\u0430\u0434\u0440\u0430\u0442", None))
        self.labelScoreTitle.setText(QCoreApplication.translate("EndWindow", u"\u0421\u0447\u0451\u0442", None))
        self.labelScoreValue.setText(QCoreApplication.translate("EndWindow", u"0", None))
        self.labelRecordTitle.setText(QCoreApplication.translate("EndWindow", u"\u0420\u0435\u043a\u043e\u0440\u0434", None))
        self.labelRecordValue.setText(QCoreApplication.translate("EndWindow", u"0", None))
        self.labelGameOver.setText(QCoreApplication.translate("EndWindow", u"\u0412\u0440\u0435\u043c\u044f \u0432\u044b\u0448\u043b\u043e!", None))
        self.labelMessage.setText(QCoreApplication.translate("EndWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0440\u0435\u043a\u043e\u0440\u0434! \u041e\u0442\u043b\u0438\u0447\u043d\u044b\u0439 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442!", None))
        self.labelFinalScore.setText(QCoreApplication.translate("EndWindow", u"0", None))
        self.btnPlayAgain.setText(QCoreApplication.translate("EndWindow", u"\u0418\u0433\u0440\u0430\u0442\u044c \u0441\u043d\u043e\u0432\u0430", None))
        self.btnRestart.setText(QCoreApplication.translate("EndWindow", u"\u0417\u0430\u043d\u043e\u0432\u043e", None))
    # retranslateUi

