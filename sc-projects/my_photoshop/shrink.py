"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str,
    :return img: SimpleImage,
    """
    old_img = SimpleImage("images/poppy.png")
    new_img = SimpleImage.blank(old_img.width//2, old_img.height//2)

    for x in range(new_img.width):
        for y in range(new_img.height):
            if (old_img.width % 2 == 0) and (old_img.height % 2 == 0):
                new_img.get_pixel(x, y).red = old_img.get_pixel(x*2, y*2).red
                new_img.get_pixel(x, y).green = old_img.get_pixel(x*2, y*2).green
                new_img.get_pixel(x, y).blue = old_img.get_pixel(x*2, y*2).blue
            elif (old_img.width % 2 == 1) and (old_img.height % 2 == 1):
                new_img.get_pixel(x, y).red = old_img.get_pixel(x*2+1, y*2+1).red
                new_img.get_pixel(x, y).green = old_img.get_pixel(x * 2 + 1, y * 2 + 1).green
                new_img.get_pixel(x, y).blue = old_img.get_pixel(x * 2 + 1, y * 2 + 1).blue
            elif (old_img.width % 2 == 0) and (old_img.height % 2 == 1):
                new_img.get_pixel(x, y).red = old_img.get_pixel(x * 2, y * 2 + 1).red
                new_img.get_pixel(x, y).green = old_img.get_pixel(x * 2, y * 2 + 1).green
                new_img.get_pixel(x, y).blue = old_img.get_pixel(x * 2, y * 2 + 1).blue
            elif (old_img.width % 2 == 1) and (old_img.height % 2 == 0):
                new_img.get_pixel(x, y).red = old_img.get_pixel(x * 2 + 1, y * 2).red
                new_img.get_pixel(x, y).green = old_img.get_pixel(x * 2 + 1, y * 2).green
                new_img.get_pixel(x, y).blue = old_img.get_pixel(x * 2 + 1, y * 2).blue

    return new_img


def main():
    """
    TODO:
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
