import pyperclip
import eel
import os
import webbrowser
from datetime import datetime
from config import BASE_DIR_FILE


@eel.expose
def set_data(value):
    print(f"set up {value}")
    pyperclip.copy(value)


@eel.expose
def telegram_connection():
    webbrowser.open("https://t.me/cv_project_bot")


@eel.expose
def archive_show():
    os.system(f"start {BASE_DIR_FILE}")


@eel.expose
def reload_list():
    open(BASE_DIR_FILE, 'w').close()


class Core:
    def __init__(self):
        self.prev_text = None

    @staticmethod
    def get_data():
        return pyperclip.paste(), datetime.now().strftime("%I:%M%p %d/%B/%Y")

    def share_history(self):
        data = self._open_data()
        eel.share_data(data)

    @classmethod
    def _open_data(cls):
        total = []
        with open(BASE_DIR_FILE, "r") as file:
            for element in file:
                total.append(element.replace("\n", ""))
        return total

    @classmethod
    def _save_data(cls, value, curr_time):
        if value or value != "" or value != "\n" or value != " ":
            with open(BASE_DIR_FILE, "a") as file:
                file.write(value.replace("\n", "") + "---" + curr_time)
                file.write("\n")

    def start_core(self):
        value, _ = self.get_data()
        self.prev_text = value
        while True:
            value, current_time = self.get_data()
            if value != self.prev_text:
                self._save_data(value, current_time)
                eel.push_data((value, current_time))
                self.prev_text = value
            eel.sleep(1)
