"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide6 import QtWidgets
from b_systeminfo_widget import SystemInfoWidget
from c_weatherapi_widget import WeatherWidget

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Мониторинг погоды и системы')
        self.setGeometry(100, 100, 600, 400)

        self.tab_widget = QtWidgets.QTabWidget()
        self.setCentralWidget(self.tab_widget)

        self.system_tab = SystemInfoWidget()
        self.weather_tab = WeatherWidget()

        self.tab_widget.addTab(self.system_tab, 'Информация о системе')
        self.tab_widget.addTab(self.weather_tab, 'Информация о погоде')

    def closeEvent(self, event, /):
        self.system_tab.systemInfoThread.quit()
        self.weather_tab.stopThread()
        event.accept()


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = MainWindow()
    window.show()

    app.exec()