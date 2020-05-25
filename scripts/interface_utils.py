import os

from PIL import Image

from PyQt5 import QtWidgets

from scripts.image_utils import rgb_to_hex, change_color, display_image


class ColorButton(QtWidgets.QPushButton):
    def __init__(self, color, label):
        super(ColorButton, self).__init__()
        self.setStyleSheet(f"background-color:{color}")
        self.clicked.connect(lambda: change_color(self, label))


def get_file_path():
    file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Wybór pliku", os.path.expanduser("~/Desktop"), "PNG (*.png);;JPG (*.jpg, *.jpeg)")
    return file_path


def remove_buttons(layout):
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().setParent(None)


def open_image(label, layout):
    file_path = get_file_path()
    if file_path:
        image = Image.open(file_path).convert("RGBA")
        display_image(label, image)

        colors = image.getcolors()
        colors_rgba = [color[1] for color in colors]
        colors_hex = [rgb_to_hex(color) for color in colors_rgba]

        remove_buttons(layout)
        for color in colors_hex:
            button = ColorButton(color, label)
            layout.addWidget(button)


def save_image(label):
    path = QtWidgets.QFileDialog.getSaveFileName(None, 'Save as...', "name.png", '*.png')
    label.pixmap().save(path[0])
