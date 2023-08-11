# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addReport_maket.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QTableView, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(520, 570)
        Form.setMinimumSize(QSize(520, 570))
        Form.setMaximumSize(QSize(520, 570))
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 501, 551))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.reportNameLayout = QHBoxLayout()
        self.reportNameLayout.setObjectName(u"reportNameLayout")
        self.reportLabel = QLabel(self.verticalLayoutWidget)
        self.reportLabel.setObjectName(u"reportLabel")

        self.reportNameLayout.addWidget(self.reportLabel)

        self.reportEdit = QLineEdit(self.verticalLayoutWidget)
        self.reportEdit.setObjectName(u"reportEdit")

        self.reportNameLayout.addWidget(self.reportEdit)


        self.verticalLayout.addLayout(self.reportNameLayout)

        self.totalEarnLabel = QLabel(self.verticalLayoutWidget)
        self.totalEarnLabel.setObjectName(u"totalEarnLabel")

        self.verticalLayout.addWidget(self.totalEarnLabel)

        self.spinBox = QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(10000000)
        self.spinBox.setSingleStep(1000)

        self.verticalLayout.addWidget(self.spinBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.percConsumableLayout = QVBoxLayout()
        self.percConsumableLayout.setObjectName(u"percConsumableLayout")
        self.percConsLabel = QLabel(self.verticalLayoutWidget)
        self.percConsLabel.setObjectName(u"percConsLabel")

        self.percConsumableLayout.addWidget(self.percConsLabel)

        self.percConsumSpin = QSpinBox(self.verticalLayoutWidget)
        self.percConsumSpin.setObjectName(u"percConsumSpin")
        self.percConsumSpin.setMaximum(100)

        self.percConsumableLayout.addWidget(self.percConsumSpin)


        self.horizontalLayout_3.addLayout(self.percConsumableLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.percPayLabel = QLabel(self.verticalLayoutWidget)
        self.percPayLabel.setObjectName(u"percPayLabel")

        self.verticalLayout_2.addWidget(self.percPayLabel)

        self.percPaySpin = QSpinBox(self.verticalLayoutWidget)
        self.percPaySpin.setObjectName(u"percPaySpin")
        self.percPaySpin.setMaximum(100)

        self.verticalLayout_2.addWidget(self.percPaySpin)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.tableView = QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.addEmplButton = QPushButton(self.verticalLayoutWidget)
        self.addEmplButton.setObjectName(u"addEmplButton")

        self.buttonsLayout.addWidget(self.addEmplButton)

        self.delEmplButton = QPushButton(self.verticalLayoutWidget)
        self.delEmplButton.setObjectName(u"delEmplButton")

        self.buttonsLayout.addWidget(self.delEmplButton)


        self.verticalLayout.addLayout(self.buttonsLayout)

        self.createReportButton = QPushButton(self.verticalLayoutWidget)
        self.createReportButton.setObjectName(u"createReportButton")

        self.verticalLayout.addWidget(self.createReportButton)


        self.retranslateUi(Form)
        self.delEmplButton.clicked.connect(Form.deleteEmployee)
        self.addEmplButton.clicked.connect(Form.addEmployee)
        self.createReportButton.clicked.connect(Form.createReport)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.reportLabel.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0442\u0447\u0435\u0442\u0430", None))
        self.totalEarnLabel.setText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0443\u043c\u043c\u0443 \u0437\u0430\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u043f\u043e \u0434\u0430\u043d\u043d\u043e\u043c\u0443 \u043e\u0442\u0447\u0435\u0442\u0443:", None))
        self.percConsLabel.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0446\u0435\u043d\u0442 \u043d\u0430 \u0440\u0430\u0441\u0445\u043e\u0434\u043d\u0438\u043a\u0438:", None))
        self.percPayLabel.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0446\u0435\u043d\u0442 \u043d\u0430 \u0437\u0430\u0440\u043f\u043b\u0430\u0442\u044b:", None))
        self.addEmplButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430 \u043a \u043e\u0442\u0447\u0435\u0442\u0443", None))
        self.delEmplButton.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0438\u0437 \u043e\u0442\u0447\u0435\u0442\u0430 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.createReportButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043e\u0442\u0447\u0435\u0442", None))
    # retranslateUi

