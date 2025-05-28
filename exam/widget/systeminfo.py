from PySide6 import QtWidgets, QtCore

import sys
import psutil



class SystemInfoWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Информация о системе")
        self.setGeometry(100, 100, 400, 300)

        self.layout = QtWidgets.QVBoxLayout()

        # ComboBox для выбора интервала обновления
        self.interval_combo = QtWidgets.QComboBox()
        self.interval_combo.addItems(["1 сек", "5 сек", "10 сек", "30 сек"])
        self.layout.addWidget(self.interval_combo)

        # Метка для отображения информации
        self.info_label = QtWidgets.QLabel()
        self.layout.addWidget(self.info_label)

        self.setLayout(self.layout)

        # Таймер для обновления информации
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateInfo)

        # Запуск таймера с начальным интервалом
        self.interval_combo.currentIndexChanged.connect(self.updateInterval)
        self.updateInterval()
        self.updateInfo()  # Обновляем информацию сразу при старте

    def updateInterval(self):
        interval = int(self.interval_combo.currentText().split()[0]) * 1000
        self.timer.start(interval)

    def updateInfo(self):
        cpu_info = psutil.cpu_stats()
        cpu_count = psutil.cpu_count(logical=True)
        cpu_load = psutil.cpu_percent(interval=1)

        memory_info = psutil.virtual_memory()
        total_memory = memory_info.total / (1024 ** 2)  # MB
        used_memory = memory_info.used / (1024 ** 2)    # MB
        memory_usage = memory_info.percent

        disk_info = psutil.disk_usage('/')
        total_disk = disk_info.total / (1024 ** 3)  # GB
        used_disk = disk_info.used / (1024 ** 3)    # GB
        disk_usage = disk_info.percent

        info_text = (
            f"Процессор: {cpu_count} ядер\n"
            f"Текущая загрузка процессора: {cpu_load}%\n\n"
            f"Оперативная память: {total_memory:.2f} MB (используется: {used_memory:.2f} MB, {memory_usage}%)\n\n"
            f"Жесткий диск: {total_disk:.2f} GB (используется: {used_disk:.2f} GB, {disk_usage}%)"
        )

        self.info_label.setText(info_text)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = SystemInfoWidget()
    window.show()

    app.exec()

