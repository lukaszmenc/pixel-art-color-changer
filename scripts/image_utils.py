import io

from PIL import Image
from PIL.ImageQt import ImageQt

from PyQt5 import QtWidgets, QtGui, QtCore


def display_image(label, image):
    pixmap = QtGui.QPixmap.fromImage(ImageQt(image))
    label.setPixmap(pixmap)


def get_color():
    color = QtWidgets.QColorDialog.getColor()
    if color.isValid():
        return color.name()


def rgb_to_hex(color_rgb):
    r, g, b, a = color_rgb
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def hex_to_rgb(color_hex):
    return tuple(int(color_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))


def change_color(button, label):
    image_temp = label.pixmap()
    buffer = QtCore.QBuffer()
    buffer.open(QtCore.QBuffer.ReadWrite)
    image_temp.save(buffer, "PNG")

    image = Image.open(io.BytesIO(buffer.data())).convert("RGBA")

    previous_color = button.palette().color(QtGui.QPalette.Background).name()

    new_color = get_color()
    r_p, g_p, b_p = hex_to_rgb(previous_color)
    r_n, g_n, b_n = hex_to_rgb(new_color)

    if new_color:
        button.setStyleSheet(f"background-color:{new_color}")

        for y in range(image.size[1]):
            for x in range(image.size[0]):
                r_c, g_c, b_c, a_c = image.load()[x, y]
                if r_c == r_p and g_c == g_p and b_c == b_p:
                    image.load()[x, y] = (r_n, g_n, b_n, a_c)
        display_image(label, image)
