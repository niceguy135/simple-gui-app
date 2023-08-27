# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addEmplToReport_maket.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QTableView,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(590, 286)
        Form.setMinimumSize(QSize(590, 286))
        Form.setMaximumSize(QSize(590, 286))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 70, 261, 16))
        self.spinBox = QSpinBox(Form)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(320, 100, 251, 26))
        self.spinBox.setMaximum(100)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 160, 251, 101))
        self.employeeTable = QTableView(Form)
        self.employeeTable.setObjectName(u"employeeTable")
        self.employeeTable.setGeometry(QRect(10, 10, 291, 251))
        self.employeeTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.employeeTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.addEmployee)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0446\u0435\u043d\u0442 \u043e\u0442 \u043e\u0442\u0447\u0435\u0442\u0430, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043e\u043d \u043f\u043e\u043b\u0443\u0447\u0438\u0442:", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a \u043e\u0442\u0447\u0435\u0442\u0443!", None))
    # retranslateUi

