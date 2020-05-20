from PIL import Image


def rgb_to_hex(color_rgb):
    r, g, b, a = color_rgb
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


class Img:
    def __init__(self, path):
        self.image = Image.open(path).convert("RGBA")
        self.colors = self.colors_rgba()
        self.height = self.image.size[1]
        self.width = self.image.size[0]
        self.pixels = self.image.load()

    def colors_rgba(self):
        colors = self.image.getcolors()
        return [color[1] for color in colors]

    def colors_hex(self):
        return [rgb_to_hex(color) for color in self.colors]


