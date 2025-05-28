# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WeatherMonitor.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_WeatherMonitor(object):
    def setupUi(self, WeatherMonitor):
        if not WeatherMonitor.objectName():
            WeatherMonitor.setObjectName(u"WeatherMonitor")
        WeatherMonitor.resize(450, 350)
        self.verticalLayout = QVBoxLayout(WeatherMonitor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lat_label = QLabel(WeatherMonitor)
        self.lat_label.setObjectName(u"lat_label")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(13)
        self.lat_label.setFont(font)

        self.verticalLayout.addWidget(self.lat_label)

        self.lat_input = QLineEdit(WeatherMonitor)
        self.lat_input.setObjectName(u"lat_input")

        self.verticalLayout.addWidget(self.lat_input)

        self.lon_label = QLabel(WeatherMonitor)
        self.lon_label.setObjectName(u"lon_label")
        self.lon_label.setFont(font)

        self.verticalLayout.addWidget(self.lon_label)

        self.lon_input = QLineEdit(WeatherMonitor)
        self.lon_input.setObjectName(u"lon_input")

        self.verticalLayout.addWidget(self.lon_input)

        self.delay_label = QLabel(WeatherMonitor)
        self.delay_label.setObjectName(u"delay_label")
        self.delay_label.setFont(font)

        self.verticalLayout.addWidget(self.delay_label)

        self.delay_input = QLineEdit(WeatherMonitor)
        self.delay_input.setObjectName(u"delay_input")

        self.verticalLayout.addWidget(self.delay_input)

        self.weather_label = QLabel(WeatherMonitor)
        self.weather_label.setObjectName(u"weather_label")
        self.weather_label.setFont(font)

        self.verticalLayout.addWidget(self.weather_label)

        self.weather_info = QTextEdit(WeatherMonitor)
        self.weather_info.setObjectName(u"weather_info")

        self.verticalLayout.addWidget(self.weather_info)

        self.control_button = QPushButton(WeatherMonitor)
        self.control_button.setObjectName(u"control_button")

        self.verticalLayout.addWidget(self.control_button)


        self.retranslateUi(WeatherMonitor)

        QMetaObject.connectSlotsByName(WeatherMonitor)
    # setupUi

    def retranslateUi(self, WeatherMonitor):
        WeatherMonitor.setWindowTitle(QCoreApplication.translate("WeatherMonitor", u"Form", None))
        self.lat_label.setText(QCoreApplication.translate("WeatherMonitor", u"\u0428\u0438\u0440\u043e\u0442\u0430: ", None))
        self.lat_input.setPlaceholderText(QCoreApplication.translate("WeatherMonitor", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0448\u0438\u0440\u043e\u0442\u0443", None))
        self.lon_label.setText(QCoreApplication.translate("WeatherMonitor", u"\u0414\u043e\u043b\u0433\u043e\u0442\u0430:", None))
        self.lon_input.setPlaceholderText(QCoreApplication.translate("WeatherMonitor", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u043e\u043b\u0433\u043e\u0442\u0443", None))
        self.delay_label.setText(QCoreApplication.translate("WeatherMonitor", u"\u0417\u0430\u0434\u0435\u0440\u0436\u043a\u0430 (\u0441\u0435\u043a):", None))
        self.delay_input.setPlaceholderText(QCoreApplication.translate("WeatherMonitor", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0440\u0435\u043c\u044f \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0438", None))
        self.weather_label.setText(QCoreApplication.translate("WeatherMonitor", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u043e\u0433\u043e\u0434\u0435:", None))
        self.control_button.setText(QCoreApplication.translate("WeatherMonitor", u"\u0421\u0442\u0430\u0440\u0442", None))
    # retranslateUi

