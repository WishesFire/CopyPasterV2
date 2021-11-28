from view.core import Core
from config import WINDOW_X, WINDOW_Y
import eel

eel.init('web')


def main():
    try:
        while True:
            c = Core()
            c.share_history()
            c.start_core()
    except Exception as error:
        print(error)


eel.start('templates/base.html', size=(WINDOW_X, WINDOW_Y), jinja_templates='templates', block=False)

if __name__ == '__main__':
    main()
