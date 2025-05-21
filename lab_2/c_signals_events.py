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


from PySide6 import QtWidgets, QtCore
from c_signals_events_form import Ui_Form
from datetime import datetime


class Window(QtWidgets.QWidget, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.uinitSignals()

        self.old_pos = self.pos()
        self.old_size = self.size()

        self.plainTextEdit.clear()


    def uinitSignals(self):
        self.pushButtonMoveCoords.clicked.connect(self.moveWindow)
        self.pushButtonGetData.clicked.connect(self.getScreenInfo)
        self.pushButtonLT.clicked.connect(self.moveLT)
        self.pushButtonRT.clicked.connect(self.moveRT)
        self.pushButtonCenter.clicked.connect(self.moveCenter)
        self.pushButtonLB.clicked.connect(self.moveLB)
        self.pushButtonRB.clicked.connect(self.moveRB)

    def moveLT(self):
        screen = QtWidgets.QApplication.primaryScreen()
        self.move(screen.availableGeometry().topLeft())

    def moveRT(self):
        screen = QtWidgets.QApplication.primaryScreen()
        right = screen.availableGeometry().right() - self.width()
        top = screen.availableGeometry().top()
        self.move(right, top)

    def moveCenter(self):
        screen = QtWidgets.QApplication.primaryScreen()
        center = screen.availableGeometry().center() - QtCore.QPoint(self.width() // 2, self.height() // 2)
        self.move(center)

    def moveLB(self):
        screen = QtWidgets.QApplication.primaryScreen()
        pos = screen.availableGeometry().bottomLeft() - QtCore.QPoint(0, self.height())
        self.move(pos)

    def moveRB(self):
        screen = QtWidgets.QApplication.primaryScreen()
        pos = screen.availableGeometry().bottomRight() - QtCore.QPoint(self.width(), self.height())
        self.move(pos)

    def moveWindow(self):
        x = self.spinBoxX.value()
        y = self.spinBoxY.value()
        self.move(x, y)

    def getScreenInfo(self):

        screens = QtWidgets.QApplication.screens()
        current_screen = QtWidgets.QApplication.screenAt(self.geometry().center())
        geometry = self.geometry()
        center = geometry.center()

        state = ("Свернуто" if self.isMinimized() else
                 "Развернуто" if self.isMaximized() else
                 "Активно" if self.isActiveWindow() else
                 "Отображено" if self.isVisible() else
                 "Не определено")

        # Формируем информацию
        info = []
        info.append(f'=== Информация о системе [{datetime.now().strftime("%H:%M:%S")}] ===')
        info.append(f'Количество экранов: {len(screens)}')

        if current_screen:
            info.append(f'Текущий экран: {current_screen.name()}')
            info.append(f'Разрешение: {current_screen.size().width()}x{current_screen.size().height()}')
            info.append(f'\nРазмер окна: {self.width()}x{self.height()}')
            info.append((f'Минимальные размеры окна: {self.minimumWidth()}x{self.minimumHeight()}'))
            info.append(f'Позиция: {self.x()}, {self.y()}')
            screen_relative = center - current_screen.geometry().topLeft()
            info.append(f"Центр относительно экрана: ({screen_relative.x()}, {screen_relative.y()})")
            info.append(f'Состояние окна: {state}')
        self.plainTextEdit.setPlainText('\n'.join(info))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
