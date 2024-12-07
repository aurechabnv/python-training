# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        if not Calculator.objectName():
            Calculator.setObjectName(u"Calculator")
        Calculator.resize(376, 358)
        self.verticalLayout = QVBoxLayout(Calculator)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Calculator)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(48, 48))
        self.pushButton.setFlat(True)

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(48, 48))
        self.pushButton_2.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_2, 1, 3, 1, 1)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QSize(48, 48))
        self.pushButton_3.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QSize(48, 48))
        self.pushButton_4.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_4, 2, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QSize(48, 48))
        self.pushButton_5.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_5, 2, 2, 1, 1)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QSize(48, 48))
        self.pushButton_6.setStyleSheet(u"")
        self.pushButton_6.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_6, 2, 3, 1, 1)

        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QSize(48, 48))
        self.pushButton_7.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_7, 3, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QSize(48, 48))
        self.pushButton_8.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_8, 3, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMinimumSize(QSize(48, 48))
        self.pushButton_9.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_9, 3, 2, 1, 1)

        self.pushButton_10 = QPushButton(self.frame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setMinimumSize(QSize(48, 48))
        self.pushButton_10.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_10, 3, 3, 1, 1)

        self.pushButton_14 = QPushButton(self.frame)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setMinimumSize(QSize(48, 48))
        self.pushButton_14.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_14, 4, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.frame)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setMinimumSize(QSize(48, 48))
        self.pushButton_12.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_12, 4, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.frame)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setMinimumSize(QSize(48, 48))
        self.pushButton_13.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_13, 4, 2, 1, 1)

        self.pushButton_11 = QPushButton(self.frame)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setMinimumSize(QSize(48, 48))
        self.pushButton_11.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_11, 4, 3, 1, 1)

        self.pushButton_15 = QPushButton(self.frame)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setMinimumSize(QSize(48, 48))
        self.pushButton_15.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_15, 5, 0, 1, 2)

        self.pushButton_16 = QPushButton(self.frame)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setMinimumSize(QSize(48, 48))
        self.pushButton_16.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_16, 5, 2, 1, 1)

        self.compute_result = QPushButton(self.frame)
        self.compute_result.setObjectName(u"compute_result")
        sizePolicy.setHeightForWidth(self.compute_result.sizePolicy().hasHeightForWidth())
        self.compute_result.setSizePolicy(sizePolicy)
        self.compute_result.setMinimumSize(QSize(48, 48))
        self.compute_result.setFlat(True)

        self.gridLayout.addWidget(self.compute_result, 5, 3, 1, 1)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 4)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Calculator)

        QMetaObject.connectSlotsByName(Calculator)
    # setupUi

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(QCoreApplication.translate("Calculator", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Calculator", u"C", None))
        self.pushButton_2.setText(QCoreApplication.translate("Calculator", u"/", None))
        self.pushButton_3.setText(QCoreApplication.translate("Calculator", u"7", None))
        self.pushButton_4.setText(QCoreApplication.translate("Calculator", u"8", None))
        self.pushButton_5.setText(QCoreApplication.translate("Calculator", u"9", None))
        self.pushButton_6.setText(QCoreApplication.translate("Calculator", u"*", None))
        self.pushButton_7.setText(QCoreApplication.translate("Calculator", u"4", None))
        self.pushButton_8.setText(QCoreApplication.translate("Calculator", u"5", None))
        self.pushButton_9.setText(QCoreApplication.translate("Calculator", u"6", None))
        self.pushButton_10.setText(QCoreApplication.translate("Calculator", u"-", None))
        self.pushButton_14.setText(QCoreApplication.translate("Calculator", u"1", None))
        self.pushButton_12.setText(QCoreApplication.translate("Calculator", u"2", None))
        self.pushButton_13.setText(QCoreApplication.translate("Calculator", u"3", None))
        self.pushButton_11.setText(QCoreApplication.translate("Calculator", u"+", None))
        self.pushButton_15.setText(QCoreApplication.translate("Calculator", u"0", None))
        self.pushButton_16.setText(QCoreApplication.translate("Calculator", u".", None))
        self.compute_result.setText(QCoreApplication.translate("Calculator", u"=", None))
    # retranslateUi

