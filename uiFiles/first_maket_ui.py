# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'first_maket.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QHBoxLayout,
    QHeaderView, QPushButton, QSizePolicy, QTableView,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(1000, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(1000, 650))
        Form.setMaximumSize(QSize(1000, 650))
        Form.setAutoFillBackground(False)
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(-1, -1, 1001, 121))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.addEmployeeButton = QPushButton(self.horizontalLayoutWidget)
        self.addEmployeeButton.setObjectName(u"addEmployeeButton")

        self.horizontalLayout.addWidget(self.addEmployeeButton)

        self.addRecordButton = QPushButton(self.horizontalLayoutWidget)
        self.addRecordButton.setObjectName(u"addRecordButton")

        self.horizontalLayout.addWidget(self.addRecordButton)

        self.calculateButton = QPushButton(self.horizontalLayoutWidget)
        self.calculateButton.setObjectName(u"calculateButton")

        self.horizontalLayout.addWidget(self.calculateButton)

        self.saveButton = QPushButton(self.horizontalLayoutWidget)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout.addWidget(self.saveButton)

        self.employesTable = QTableView(Form)
        self.employesTable.setObjectName(u"employesTable")
        self.employesTable.setGeometry(QRect(0, 120, 1001, 321))
        self.employesTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.employesTable.setSortingEnabled(True)
        self.repotsTable = QTableView(Form)
        self.repotsTable.setObjectName(u"repotsTable")
        self.repotsTable.setGeometry(QRect(0, 450, 1000, 192))
        sizePolicy.setHeightForWidth(self.repotsTable.sizePolicy().hasHeightForWidth())
        self.repotsTable.setSizePolicy(sizePolicy)
        self.repotsTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.repotsTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.repotsTable.setSortingEnabled(True)
        self.repotsTable.horizontalHeader().setMinimumSectionSize(100)

        self.retranslateUi(Form)
        self.addEmployeeButton.pressed.connect(Form.addEmployeePressed)
        self.addRecordButton.pressed.connect(Form.addReportPressed)
        self.calculateButton.pressed.connect(Form.calcPressed)
        self.saveButton.pressed.connect(Form.savePressed)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0440\u0430\u0441\u0447\u0435\u0442\u0430 \u0437\u0430\u0440\u043f\u043b\u0430\u0442", None))
        self.addEmployeeButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.addRecordButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0442\u0447\u0435\u0442", None))
        self.calculateButton.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0432\u0435\u0441\u0442\u0438 \u0440\u0430\u0441\u0441\u0447\u0435\u0442 \u0437\u0430\u0440\u043f\u043b\u0430\u0442", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
    # retranslateUi

