"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.+
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).+
    * Кол-во экранов+
    * Текущее основное окно+
    * Разрешение экрана+
    * На каком экране окно находится+
    * Размеры окна+
    * Минимальные размеры окна+
    * Текущее положение (координаты) окна+
    * Координаты центра приложения+
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)+
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""


from PySide6 import QtCore, QtWidgets
from c_signals_events_form import Ui_Form
from datetime import datetime


class Window(QtWidgets.QWidget, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.uinitSignals()

        self.wight_screen, self.height_screen = QtWidgets.QApplication.primaryScreen().size().toTuple()
        self.screen = QtWidgets.QApplication.primaryScreen()

        #Координаты центра экрана
        self.center = self.screen.availableGeometry().center()
        self.center_window = QtCore.QPoint(self.width() // 2, self.height() // 2)

        #Координаты левого нижнего края
        self.pos_lb = self.screen.availableGeometry().bottomLeft() - QtCore.QPoint(0, self.height())

        #Координаты правого нинего окна
        self.pos_rb = self.screen.availableGeometry().bottomRight() - QtCore.QPoint(self.width(), self.height())

        #Координаты правого верхнего окна

        self.pos_rt = self.wight_screen, self.height_screen

    def uinitSignals(self):
        self.pushButtonMoveCoords.clicked.connect(lambda: self.move(int(self.spinBoxX.value()), self.spinBoxY.value())) #Перемещение окна по заданным координатам
        self.pushButtonLT.clicked.connect(lambda: self.move(0, 0)) #Перемещение окна в верхний левый угол
        self.pushButtonRT.clicked.connect(lambda: self.move(int(self.pos_rt)))
        self.pushButtonCenter.clicked.connect(lambda: self.move(self.center - self.center_window)) #Перемещение окна по центру
        self.pushButtonLB.clicked.connect(lambda: self.move(self.pos_lb))#Перемещение окна в левый нижний угол
        self.pushButtonRB.clicked.connect(lambda: self.move(self.pos_rb))#Перемещение окна в правый верхний угол
        self.pushButtonGetData.clicked.connect(self.getScreenInfo) #Получение текста в lineEdit

    def moveRT(self):
        screen = QtWidgets.QApplication.primaryScreen()
        right = screen.availableGeometry().right() - self.width()
        top = screen.availableGeometry().top()
        self.move(right, top)

    def getScreenInfo(self):

        info = f"""
        Информация о системе: 
        Количество экранов: {len(QtWidgets.QApplication.screens())}
        Основное окно: {QtWidgets.QApplication.primaryScreen().name()}
        Разрешение экрана: Ширина - {self.wight_screen}, Высота - {self.height_screen}
        Минимальный размер: {self.minimumSize()}
        Размеры окна: {self.size().width()} x {self.size().height()}
        Координты окна: {self.pos().toTuple()}
        Состояние: {self.windowState().name}
        """

        self.plainTextEdit.setPlainText(info)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
