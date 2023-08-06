# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addEmployee_maket.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(490, 360)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(490, 360))
        Form.setMaximumSize(QSize(490, 360))
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 471, 346))
        self.MainLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.MainLayout.setSpacing(15)
        self.MainLayout.setObjectName(u"MainLayout")
        self.MainLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.fullNameLayout = QHBoxLayout()
        self.fullNameLayout.setObjectName(u"fullNameLayout")
        self.fullNameLable = QLabel(self.verticalLayoutWidget)
        self.fullNameLable.setObjectName(u"fullNameLable")
        self.fullNameLable.setEnabled(True)

        self.fullNameLayout.addWidget(self.fullNameLable)

        self.fullNameEdit = QLineEdit(self.verticalLayoutWidget)
        self.fullNameEdit.setObjectName(u"fullNameEdit")

        self.fullNameLayout.addWidget(self.fullNameEdit)


        self.MainLayout.addLayout(self.fullNameLayout)

        self.roomLayout = QHBoxLayout()
        self.roomLayout.setObjectName(u"roomLayout")
        self.roomLable = QLabel(self.verticalLayoutWidget)
        self.roomLable.setObjectName(u"roomLable")

        self.roomLayout.addWidget(self.roomLable)

        self.roomEdit = QLineEdit(self.verticalLayoutWidget)
        self.roomEdit.setObjectName(u"roomEdit")

        self.roomLayout.addWidget(self.roomEdit)


        self.MainLayout.addLayout(self.roomLayout)

        self.isFixPay = QCheckBox(self.verticalLayoutWidget)
        self.isFixPay.setObjectName(u"isFixPay")

        self.MainLayout.addWidget(self.isFixPay)

        self.fixPayPin = QSpinBox(self.verticalLayoutWidget)
        self.fixPayPin.setObjectName(u"fixPayPin")
        self.fixPayPin.setEnabled(False)
        self.fixPayPin.setLayoutDirection(Qt.LeftToRight)
        self.fixPayPin.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.fixPayPin.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.fixPayPin.setProperty("showGroupSeparator", False)
        self.fixPayPin.setMaximum(1000000)
        self.fixPayPin.setSingleStep(1000)

        self.MainLayout.addWidget(self.fixPayPin)

        self.isRecalcNeed = QCheckBox(self.verticalLayoutWidget)
        self.isRecalcNeed.setObjectName(u"isRecalcNeed")

        self.MainLayout.addWidget(self.isRecalcNeed)

        self.startValueBox = QSpinBox(self.verticalLayoutWidget)
        self.startValueBox.setObjectName(u"startValueBox")
        self.startValueBox.setEnabled(False)
        self.startValueBox.setMaximum(100000)
        self.startValueBox.setSingleStep(500)

        self.MainLayout.addWidget(self.startValueBox)

        self.workedDaysBox = QSpinBox(self.verticalLayoutWidget)
        self.workedDaysBox.setObjectName(u"workedDaysBox")
        self.workedDaysBox.setEnabled(False)
        self.workedDaysBox.setMaximum(31)

        self.MainLayout.addWidget(self.workedDaysBox)

        self.createEmployee = QPushButton(self.verticalLayoutWidget)
        self.createEmployee.setObjectName(u"createEmployee")

        self.MainLayout.addWidget(self.createEmployee)


        self.retranslateUi(Form)
        self.isFixPay.toggled.connect(self.fixPayPin.setEnabled)
        self.isRecalcNeed.toggled.connect(self.startValueBox.setEnabled)
        self.isRecalcNeed.toggled.connect(self.workedDaysBox.setEnabled)
        self.createEmployee.clicked.connect(Form.createEmployeeTouched)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.fullNameLable.setText(QCoreApplication.translate("Form", u"\u0424\u0418\u041e \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.fullNameEdit.setText("")
        self.roomLable.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0431\u0438\u043d\u0435\u0442 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.isFixPay.setText(QCoreApplication.translate("Form", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u0430 \u043b\u0438 \u0444\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u0430\u044f \u0437\u0430\u0440\u043f\u043b\u0430\u0442\u0430?", None))
        self.fixPayPin.setSpecialValueText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0444\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u0443\u044e \u0437\u0430\u0440\u043f\u043b\u0430\u0442\u0443...", None))
        self.isRecalcNeed.setText(QCoreApplication.translate("Form", u"\u0411\u0443\u0434\u0435\u0442 \u043b\u0438 \u043f\u0440\u043e\u0432\u043e\u0434\u0438\u0442\u044c\u0441\u044f \u043f\u0435\u0440\u0435\u0440\u0430\u0441\u0447\u0435\u0442 \u043f\u043e \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0443 \u0434\u043d\u0435\u0439?", None))
        self.startValueBox.setSpecialValueText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u0435\u0440\u0435\u0440\u0430\u0441\u0447\u0435\u0442\u0430", None))
        self.workedDaysBox.setSpecialValueText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0442\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u044b\u0445 \u0434\u043d\u0435\u0439", None))
        self.createEmployee.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
    # retranslateUi

