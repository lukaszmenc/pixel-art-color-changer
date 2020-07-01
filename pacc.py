import sys
from scripts.interface import Interface
from PyQt5.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Interface()
    sys.exit(app.exec_())
