"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings_form.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),+
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber+
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),+
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""


from PySide6 import QtWidgets, QtCore
from d_eventfilter_settings_form import Ui_Form

class Window(QtWidgets.QWidget, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.comboBox.addItems(["oct", "hex", "bin", "dec"])
        self.comboBox.currentTextChanged.connect(self.updateLcdNuber)

        self.dial.valueChanged.connect(self.updateControll)
        self.horizontalSlider.valueChanged.connect(self.updateControll)


    def keyPressEvent(self, event, /):
        if event.key() == QtCore.Qt.Key.Key_Plus:
            self.dial.setValue(self.dial.value() + 1)
            print(f"Новое значение: {self.dial.value()}")
            return True
        elif event.key() == QtCore.Qt.Key.Key_Minus:
            self.dial.setValue(self.dial.value() - 1)
            print(f"Новое значение: {self.dial.value()}")
            return True
        return super().keyPressEvent(event)

    def updateControll(self, value):
        sender = self.sender()
        if sender != self.dial:
            self.dial.setValue(value)
        if sender != self.horizontalSlider:
            self.horizontalSlider.setValue(value)
        if sender != self.lcdNumber:
            self.lcdNumber.display(value)

    def updateLcdNuber(self, obj):
        if obj == 'oct':
            self.lcdNumber.setOctMode()
        elif obj == 'hex':
            self.lcdNumber.setOctMode()
        elif obj == 'bin':
            self.lcdNumber.setBinMode()
        elif obj == 'dec':
            self.lcdNumber.setDecMode()
        self.lcdNumber.display(obj)



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
