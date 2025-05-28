"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатии на кнопку
"""

from PySide6 import QtWidgets
from a_threads import WeatherHandler
from ui.WeatherMonitor import Ui_WeatherMonitor
from datetime import datetime

class WeatherWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_WeatherMonitor()
        self.ui.setupUi(self)

        self.ui.weather_info.setReadOnly(True)
        self.weather_thread = None

        self.ui.control_button.clicked.connect(self.toggleThread)


    def toggleThread(self):
        """Переключает состояние потока (старт/стоп)"""
        if self.weather_thread is not None:
            self.stopThread()
        else:
            self.startThread()

    def startThread(self):
        """Запускает поток сбора данных о погоде"""
        try:
            lat = float(self.ui.lat_input.text())
            lon = float(self.ui.lon_input.text())
            delay = int(self.ui.delay_input.text())
        except ValueError:
            QtWidgets.QMessageBox.warning(
                self,
                "Ошибка",
                "Пожалуйста, введите корректные числовые значения"
            )
            return

        self.weather_thread = WeatherHandler(lat, lon)
        self.weather_thread.setDelay(delay)
        self.weather_thread.setStatus(True)
        self.weather_thread.weatherDataReceived.connect(self.updateWeather)
        self.weather_thread.errorOccurred.connect(self.showError)
        self.weather_thread.start()

        self.ui.control_button.setText("Стоп")
        self.ui.lat_input.setEnabled(False)
        self.ui.lon_input.setEnabled(False)
        self.ui.delay_input.setEnabled(False)

    def stopThread(self):
        """Останавливает поток сбора данных"""
        if self.weather_thread:
            self.weather_thread.setStatus(False)
            self.weather_thread.quit()
            self.weather_thread.wait()
            self.weather_thread = None

            self.ui.control_button.setText("Старт")
            self.ui.lat_input.setEnabled(True)
            self.ui.lon_input.setEnabled(True)
            self.ui.delay_input.setEnabled(True)

            self.ui.weather_info.clear()

    def updateWeather(self, data):
        weather = data.get('current_weather', {})
        text = f"""
        Температура: {weather.get('temperature')}°C
        Скорость ветра: {weather.get('windspeed')} км/ч
        Направление ветра: {weather.get('winddirection')}°
        Время: {datetime.now().strftime("%d.%m.%Y %H:%M:%S")}
        """

        self.ui.weather_info.setText(text)

    def showError(self, error_msg):
        """Метод для отображения ошибок"""
        self.ui.weather_info.append(f"Ошибка: {error_msg}")

    def closeEvent(self, event, /):
        self.stopThread()
        event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = WeatherWidget()
    window.show()

    app.exec()