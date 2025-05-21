from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QSettings
from d_eventfilter_settings_form import Ui_Form


class Window(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # 1. Настройка QDial для управления с клавиатуры
        self.dial.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.dial.installEventFilter(self)

        # 2. Связывание QDial, QSlider и QLCDNumber
        self.dial.valueChanged.connect(self.update_controls)
        self.horizontalSlider.valueChanged.connect(self.update_controls)

        # 3. Настройка ComboBox с системами счисления
        self.comboBox.addItems(["DEC", "HEX", "OCT", "BIN"])
        self.comboBox.currentTextChanged.connect(self.update_lcd_format)

        # 4. Загрузка сохраненных настроек
        self.settings = QSettings("MyCompany", "DialApp")
        self.load_settings()

    def eventFilter(self, obj, event):
        if obj == self.dial and event.type() == QtCore.QEvent.Type.KeyPress:
            if event.key() == QtCore.Qt.Key.Key_Plus:
                self.dial.setValue(self.dial.value() + 1)
                print(f"New dial value: {self.dial.value()}")
                return True
            elif event.key() == QtCore.Qt.Key.Key_Minus:
                self.dial.setValue(self.dial.value() - 1)
                print(f"New dial value: {self.dial.value()}")
                return True
        return super().eventFilter(obj, event)

    def update_controls(self, value):
        sender = self.sender()
        if sender != self.dial:
            self.dial.setValue(value)
        if sender != self.horizontalSlider:
            self.horizontalSlider.setValue(value)
        if sender != self.lcdNumber:
            self.lcdNumber.display(value)

    def update_lcd_format(self, fmt):
        fmt = fmt.lower()
        if fmt == "dec":
            self.lcdNumber.setDecMode()
        elif fmt == "hex":
            self.lcdNumber.setHexMode()
        elif fmt == "oct":
            self.lcdNumber.setOctMode()
        elif fmt == "bin":
            self.lcdNumber.setBinMode()
        self.settings.setValue("display_format", fmt)

    def load_settings(self):
        if self.settings.contains("value"):
            val = self.settings.value("value", type=int)
            self.dial.setValue(val)
            self.horizontalSlider.setValue(val)
            self.lcdNumber.display(val)
        if self.settings.contains("display_format"):
            fmt = self.settings.value("display_format")
            index = self.comboBox.findText(fmt.upper())
            if index >= 0:
                self.comboBox.setCurrentIndex(index)

    def closeEvent(self, event):
        self.settings.setValue("value", self.dial.value())
        self.settings.setValue("display_format", self.comboBox.currentText().lower())
        super().closeEvent(event)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    QtCore.QCoreApplication.setOrganizationName("MyCompany")
    QtCore.QCoreApplication.setApplicationName("DialApp")

    window = Window()
    window.show()
    sys.exit(app.exec())