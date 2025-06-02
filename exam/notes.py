# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notes.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QHBoxLayout, QHeaderView,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Note(object):
    def setupUi(self, Note):
        if not Note.objectName():
            Note.setObjectName(u"Note")
        Note.resize(600, 500)
        self.verticalLayout = QVBoxLayout(Note)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_deadline = QLabel(Note)
        self.label_deadline.setObjectName(u"label_deadline")
        self.label_deadline.setMinimumSize(QSize(100, 0))
        self.label_deadline.setMaximumSize(QSize(100, 22))

        self.horizontalLayout.addWidget(self.label_deadline)

        self.dateTimeEdit = QDateTimeEdit(Note)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.dateTimeEdit)

        self.horizontalSpacer_2 = QSpacerItem(348, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_head = QLabel(Note)
        self.label_head.setObjectName(u"label_head")
        self.label_head.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.label_head)

        self.plainTextEdit_head = QPlainTextEdit(Note)
        self.plainTextEdit_head.setObjectName(u"plainTextEdit_head")
        self.plainTextEdit_head.setMinimumSize(QSize(0, 2))
        self.plainTextEdit_head.setMaximumSize(QSize(16777215, 54))

        self.horizontalLayout_2.addWidget(self.plainTextEdit_head)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_text = QLabel(Note)
        self.label_text.setObjectName(u"label_text")
        self.label_text.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.label_text)

        self.plainTextEdit_text = QPlainTextEdit(Note)
        self.plainTextEdit_text.setObjectName(u"plainTextEdit_text")
        self.plainTextEdit_text.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_3.addWidget(self.plainTextEdit_text)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(228, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton_save = QPushButton(Note)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.horizontalLayout_4.addWidget(self.pushButton_save)

        self.pushButton_del = QPushButton(Note)
        self.pushButton_del.setObjectName(u"pushButton_del")

        self.horizontalLayout_4.addWidget(self.pushButton_del)

        self.pushButton_new = QPushButton(Note)
        self.pushButton_new.setObjectName(u"pushButton_new")

        self.horizontalLayout_4.addWidget(self.pushButton_new)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.treeWidget = QTreeWidget(Note)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(10)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(2, font);
        __qtreewidgetitem.setFont(1, font);
        __qtreewidgetitem.setFont(0, font);
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout.addWidget(self.treeWidget)


        self.retranslateUi(Note)

        QMetaObject.connectSlotsByName(Note)
    # setupUi

    def retranslateUi(self, Note):
        Note.setWindowTitle(QCoreApplication.translate("Note", u"Form", None))
        self.label_deadline.setText(QCoreApplication.translate("Note", u"\u0414\u0435\u0434\u043b\u0430\u0439\u043d:", None))
        self.label_head.setText(QCoreApplication.translate("Note", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a:", None))
        self.label_text.setText(QCoreApplication.translate("Note", u"\u0422\u0435\u043a\u0441\u0442:", None))
        self.pushButton_save.setText(QCoreApplication.translate("Note", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButton_del.setText(QCoreApplication.translate("Note", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_new.setText(QCoreApplication.translate("Note", u"\u041d\u043e\u0432\u0430\u044f", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Note", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Note", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Note", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0430", None));
    # retranslateUi

