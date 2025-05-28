"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""

from PySide6 import QtWidgets
from a_threads import SystemInfo

from ui.SystemInfoMonitor import Ui_SystemInfoWindow

class SystemInfoWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SystemInfoWindow()
        self.ui.setupUi(self)

        self.ui.delaySpinBox.valueChanged.connect(self.onDelayChanged)

        self.initThread()

    def initThread(self):
        self.systemInfoThread = SystemInfo()
        self.systemInfoThread.systemInfoReceived.connect(self.updateSystemInfo)
        self.systemInfoThread.start()

    def updateSystemInfo(self, info):
        """
        Обновление информации о система
        :param info:
        :return:
        """
        cpu, ram = info
        self.ui.cpuValue.setText(f"{cpu}%")
        self.ui.ramValue.setText(f"{ram}%")

    def onDelayChanged(self, value):
        """
        Обработка изменения задержки
        :param value:
        :return:
        """
        self.systemInfoThread.delay = value


    def closeEvent(self, event):
        self.systemInfoThread.quit()
        event.accept()



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = SystemInfoWidget()
    window.show()

    app.exec()
