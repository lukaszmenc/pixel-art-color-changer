from PyQt5 import QtWidgets, QtGui, QtCore
from scripts.interface_utils import open_image, save_image


class Interface(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.appname = "PACC"
        self.resize(640, 480)

        self.color_box_scroll = QtWidgets.QScrollArea()
        self.color_box_scroll.setWidgetResizable(True)

        self.color_box = QtWidgets.QFrame(self.color_box_scroll)
        self.color_box.setLayout(QtWidgets.QVBoxLayout())
        self.color_box.layout().setAlignment(
            QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter
        )

        self.color_box_scroll.setWidget(self.color_box)

        self.image_label = QtWidgets.QLabel(self)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)

        self.main_window()

    def main_window(self):

        menu = QtWidgets.QHBoxLayout()

        button_open_file = QtWidgets.QPushButton("Open file")
        button_open_file.clicked.connect(
            lambda: open_image(self.image_label, self.color_box.layout())
        )
        button_open_file.setShortcut("Ctrl+O")

        button_save_image = QtWidgets.QPushButton("Save image")
        button_save_image.clicked.connect(lambda: save_image(self.image_label))
        button_save_image.setShortcut("Ctrl+S")

        menu.addWidget(button_open_file)
        menu.addWidget(button_save_image)

        main_view = QtWidgets.QHBoxLayout()

        label_colors_font = QtGui.QFont()
        label_colors_font.setBold(True)
        label_colors = QtWidgets.QLabel("Colors")
        label_colors.setFont(label_colors_font)
        label_colors.setAlignment(QtCore.Qt.AlignHCenter)

        colors_menu_layout = QtWidgets.QVBoxLayout()
        colors_menu_layout.addWidget(label_colors)
        colors_menu_layout.addWidget(self.color_box_scroll)

        colors_menu_widget = QtWidgets.QWidget()
        colors_menu_widget.setLayout(colors_menu_layout)
        colors_menu_widget.setFixedWidth(160)

        main_view.addWidget(self.image_label)
        main_view.addWidget(colors_menu_widget)

        window = QtWidgets.QVBoxLayout()
        window.addLayout(menu)
        window.addLayout(main_view)

        self.setLayout(window)
        self.setWindowTitle(self.appname)
        self.show()
