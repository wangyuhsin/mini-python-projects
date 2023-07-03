from simpleimage import SimpleImage


def shrink(filename):
    """
    Creates a new image that is half the width and height of the original image.
    Sets pixels at x=0, 1, 2, 3 in the new image from x=0, 2, 4, 6 in the original image, and likewise in the y direction.
    :param filename: The filename of the original image.
    :return: The shrunk image.
    """
    old_img = SimpleImage(filename)
    new_img = SimpleImage.blank(old_img.width // 2, old_img.height // 2)

    for x in range(new_img.width):
        for y in range(new_img.height):
            if (old_img.width % 2 == 0) and (old_img.height % 2 == 0):
                new_img.get_pixel(x, y).red = old_img.get_pixel(
                    x * 2, y * 2).red
                new_img.get_pixel(x, y).green = old_img.get_pixel(
                    x * 2, y * 2).green
                new_img.get_pixel(x, y).blue = old_img.get_pixel(
                    x * 2, y * 2).blue
            elif (old_img.width % 2 == 1) and (old_img.height % 2 == 1):
                new_img.get_pixel(x, y).red = old_img.get_pixel(
                    x * 2 + 1, y * 2 + 1
                ).red
                new_img.get_pixel(x, y).green = old_img.get_pixel(
                    x * 2 + 1, y * 2 + 1
                ).green
                new_img.get_pixel(x, y).blue = old_img.get_pixel(
                    x * 2 + 1, y * 2 + 1
                ).blue
            elif (old_img.width % 2 == 0) and (old_img.height % 2 == 1):
                new_img.get_pixel(x, y).red = old_img.get_pixel(
                    x * 2, y * 2 + 1).red
                new_img.get_pixel(x, y).green = old_img.get_pixel(
                    x * 2, y * 2 + 1
                ).green
                new_img.get_pixel(x, y).blue = old_img.get_pixel(
                    x * 2, y * 2 + 1).blue
            elif (old_img.width % 2 == 1) and (old_img.height % 2 == 0):
                new_img.get_pixel(x, y).red = old_img.get_pixel(
                    x * 2 + 1, y * 2).red
                new_img.get_pixel(x, y).green = old_img.get_pixel(
                    x * 2 + 1, y * 2
                ).green
                new_img.get_pixel(x, y).blue = old_img.get_pixel(
                    x * 2 + 1, y * 2).blue

    return new_img


def main():
    """
    Main function to run the image shrinking process.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == "__main__":
    main()
