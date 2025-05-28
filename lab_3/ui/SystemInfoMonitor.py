# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SystemInfoMonitor.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_SystemInfoWindow(object):
    def setupUi(self, SystemInfoWindow):
        if not SystemInfoWindow.objectName():
            SystemInfoWindow.setObjectName(u"SystemInfoWindow")
        SystemInfoWindow.resize(450, 100)
        self.verticalLayout = QVBoxLayout(SystemInfoWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.delayLayout = QHBoxLayout()
        self.delayLayout.setObjectName(u"delayLayout")
        self.delayLabel = QLabel(SystemInfoWindow)
        self.delayLabel.setObjectName(u"delayLabel")

        self.delayLayout.addWidget(self.delayLabel)

        self.delaySpinBox = QSpinBox(SystemInfoWindow)
        self.delaySpinBox.setObjectName(u"delaySpinBox")
        self.delaySpinBox.setMinimum(1)
        self.delaySpinBox.setMaximum(60)
        self.delaySpinBox.setValue(1)

        self.delayLayout.addWidget(self.delaySpinBox)


        self.verticalLayout.addLayout(self.delayLayout)

        self.cpuLayout = QHBoxLayout()
        self.cpuLayout.setObjectName(u"cpuLayout")
        self.cpuLabel = QLabel(SystemInfoWindow)
        self.cpuLabel.setObjectName(u"cpuLabel")

        self.cpuLayout.addWidget(self.cpuLabel)

        self.cpuValue = QLabel(SystemInfoWindow)
        self.cpuValue.setObjectName(u"cpuValue")

        self.cpuLayout.addWidget(self.cpuValue)


        self.verticalLayout.addLayout(self.cpuLayout)

        self.ramLayout = QHBoxLayout()
        self.ramLayout.setObjectName(u"ramLayout")
        self.ramLabel = QLabel(SystemInfoWindow)
        self.ramLabel.setObjectName(u"ramLabel")

        self.ramLayout.addWidget(self.ramLabel)

        self.ramValue = QLabel(SystemInfoWindow)
        self.ramValue.setObjectName(u"ramValue")

        self.ramLayout.addWidget(self.ramValue)


        self.verticalLayout.addLayout(self.ramLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SystemInfoWindow)

        QMetaObject.connectSlotsByName(SystemInfoWindow)
    # setupUi

    def retranslateUi(self, SystemInfoWindow):
        SystemInfoWindow.setWindowTitle(QCoreApplication.translate("SystemInfoWindow", u"System Info Monitor", None))
        self.delayLabel.setText(QCoreApplication.translate("SystemInfoWindow", u"\u0417\u0430\u0434\u0435\u0440\u0436\u043a\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f (\u0441\u0435\u043a):", None))
        self.cpuLabel.setText(QCoreApplication.translate("SystemInfoWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 CPU:", None))
        self.cpuValue.setText(QCoreApplication.translate("SystemInfoWindow", u"0%", None))
        self.ramLabel.setText(QCoreApplication.translate("SystemInfoWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 RAM:", None))
        self.ramValue.setText(QCoreApplication.translate("SystemInfoWindow", u"0%", None))
    # retranslateUi

