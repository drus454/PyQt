import json
from datetime import datetime

from PySide6 import QtWidgets, QtCore
from notes import Ui_Note


class Window(QtWidgets.QWidget, Ui_Note):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initSignals()

        self.notes_dict = {}
        self.last = None

        # Загрузка данных при старте
        self.load_data()


    def initSignals(self):
        self.plainTextEdit_head.textChanged.connect(self.note_changed)
        self.plainTextEdit_text.textChanged.connect(self.note_changed)
        self.pushButton_new.clicked.connect(self.new_note)
        self.pushButton_save.clicked.connect(self.save_changes)
        self.pushButton_del.clicked.connect(self.del_note)
        self.treeWidget.currentItemChanged.connect(self.load_note)

    def load_data(self):
        """
        Метод загрузки данных из файла
        :return:
        """
        with open("users/data.json", "r", encoding="utf8") as file:
            data = json.load(file)
            self.notes_dict = data.get("notes_dict", {})
            self.last = data.get("last")
            self.redraw_list_menu()
            if self.last:
                self.item_select(self.last)
            self.save_data()

    def save_data(self):
        """
        Метод сохранения данных в файл
        :return:
        """
        data = {
            "notes_dict": self.notes_dict,
            "last": self.last
        }
        with open("users/data.json", "w", encoding="utf8") as file:
            json.dump(data, file, indent=4)

    def new_note(self):
        """
        Метод создания новой заметки
        :return:
        """
        self.plainTextEdit_head.setPlainText("")
        self.plainTextEdit_text.setPlainText("")
        self.dateTimeEdit.setDateTime(datetime.now())
        self.pushButton_save.setEnabled(False)
        self.pushButton_del.setEnabled(False)

    def save_changes(self):
        """
        Метод сохранения изменений заметки
        :return:
        """
        title = self.get_note_title().strip()
        if not title:
            title = "untitled"

        note_data = {
            'title': title,
            'date': datetime.now().strftime("%H:%M %d.%m.%Y"),
            'text': self.get_note_text(),
            'date_to_seconds': datetime.now().timestamp(),
            'due_date': self.get_due_date()
        }

        self.notes_dict[title] = note_data
        self.last = title
        self.save_data()
        self.redraw_list_menu()
        self.pushButton_save.setDisabled(True)

    def del_note(self):
        """
        Метод удаления заметки
        :return:
        """
        if not self.treeWidget.selectedItems():
            return

        item = self.treeWidget.selectedItems()[0]
        note_name = item.text(0).strip() or "untitled"

        if note_name in self.notes_dict:
            self.notes_dict.pop(note_name)
            self.treeWidget.takeTopLevelItem(self.treeWidget.indexOfTopLevelItem(item))

            if self.last == note_name:
                self.last = None

            self.save_data()
            self.new_note()
            self.redraw_list_menu()

    def note_changed(self):
        """
        Метод обработки изменения текста заметки
        :return:
        """
        title = self.get_note_title().strip()
        self.pushButton_save.setEnabled(bool(title))

    def redraw_list_menu(self):
        """
        Метод обновления списка заметок
        :return:
        """
        self.treeWidget.clear()
        for note_name, note_data in self.notes_dict.items():
            item = QtWidgets.QTreeWidgetItem(self.treeWidget)
            item.setText(0, note_data['title'])
            item.setText(1, note_data['date'])
            item.setText(2, note_data['due_date'])

        if self.last and self.last in self.notes_dict:
            self.item_select(self.last)

    def item_select(self, item_name):
        """
        Метод выбора заметки по имени
        :param item_name:
        :return:
        """
        items = self.treeWidget.findItems(item_name, QtCore.Qt.MatchExactly, 0)
        if items:
            self.treeWidget.setCurrentItem(items[0])


    def load_note(self, item, last_item):
        """
        Метод загрузки заметки для просмотра/редактирования
        :param item:
        :param last_item:
        :return:
        """
        if item and item != last_item:
            note_name = item.text(0).strip() or "untitled"
            if note_name in self.notes_dict:
                note = self.notes_dict[note_name]
                self.last = note_name
                self.plainTextEdit_head.setPlainText(note['title'])
                self.plainTextEdit_text.setPlainText(note['text'])
                self.setWindowTitle(f"Note - {note_name}")
                self.pushButton_del.setEnabled(True)
                self.pushButton_save.setDisabled(True)

    def get_note_title(self):
        return self.plainTextEdit_head.toPlainText()

    def get_note_text(self):
        return self.plainTextEdit_text.toPlainText()

    def get_due_date(self):
        return self.dateTimeEdit.text()


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()