import os
from PyQt5 import QtWidgets, QtGui, QtCore
from scripts.image import Img
from PIL.ImageQt import ImageQt


def get_file_path():
    file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Wybór pliku", os.path.expanduser("~/Desktop"), "PNG (*.png);;JPG (*.jpg, *.jpeg)")
    return file_path


def display_image(label, image):
    pixmap = QtGui.QPixmap.fromImage(ImageQt(image.image))
    label.setPixmap(pixmap)


def get_color():
    color = QtWidgets.QColorDialog.getColor()
    if color.isValid():
        return color.name()


def hex_to_rgb(color_hex):
    return tuple(int(color_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))


def change_color(color, button, image, label):
    new_color = get_color()
    r_o, g_o, b_o = hex_to_rgb(color)
    r_n, g_n, b_n = hex_to_rgb(new_color)

    if new_color:
        button.setStyleSheet(f"background-color:{new_color}")

        for y in range(image.height):
            for x in range(image.width):
                r_c, g_c, b_c, a_c = image.pixels[x, y]
                if r_c == r_o and g_c == g_o and b_c == b_o:
                    image.pixels[x, y] = (r_n, g_n, b_n, a_c)

        display_image(label, image)


def create_button(color, image, label):
    button = QtWidgets.QPushButton()
    button.setStyleSheet(f"background-color:{color}")
    button.clicked.connect(lambda: change_color(color, button, image, label))
    return button


def remove_buttons(layout):
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().setParent(None)


def open_image(label, layout):
    file_path = get_file_path()
    if file_path:
        image = Img(file_path)
        display_image(label, image)
        remove_buttons(layout)
        for color in image.colors_hex():
            button = create_button(color, image, label)
            layout.addWidget(button)


def save_image():
    pass
