"""
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(old_img):
    """
    Applies a blur effect to the given image.
    :param old_img: The original image.
    :return: The blurred image.
    """
    new_img = SimpleImage.blank(old_img.width, old_img.height)

    for x in range(old_img.width):
        for y in range(old_img.height):
            if (
                (x > 0)
                and (x < (old_img.width - 1))
                and (y > 0)
                and (y < (old_img.height - 1))
            ):
                new_pixel = new_img.get_pixel(x, y)
                red = 0
                green = 0
                blue = 0
                for i in range(x - 1, x + 2):
                    for j in range(y - 1, y + 2):
                        red += old_img.get_pixel(i, j).red
                        green += old_img.get_pixel(i, j).green
                        blue += old_img.get_pixel(i, j).blue
                new_pixel.red = red // 9
                new_pixel.green = green // 9
                new_pixel.blue = blue // 9
            elif (x == 0) and (y > 0) and (y < (old_img.height - 1)):
                new_pixel = new_img.get_pixel(x, y)
                red = 0
                green = 0
                blue = 0
                for i in range(2):
                    for j in range(y - 1, y + 2):
                        red += old_img.get_pixel(i, j).red
                        green += old_img.get_pixel(i, j).green
                        blue += old_img.get_pixel(i, j).blue
                new_pixel.red = red // 6
                new_pixel.green = green // 6
                new_pixel.blue = blue // 6
            elif (x == (old_img.width - 1)) and (y > 0) and (y < (old_img.height - 1)):
                new_pixel = new_img.get_pixel(x, y)
                red = 0
                green = 0
                blue = 0
                for i in range(x - 1, x + 1):
                    for j in range(y - 1, y + 2):
                        red += old_img.get_pixel(i, j).red
                        green += old_img.get_pixel(i, j).green
                        blue += old_img.get_pixel(i, j).blue
                new_pixel.red = red // 6
                new_pixel.green = green // 6
                new_pixel.blue = blue // 6
            elif (x > 0) and (x < (old_img.width - 1)) and y == 0:
                new_pixel = new_img.get_pixel(x, y)
                red = 0
                green = 0
                blue = 0
                for i in range(x - 1, x + 2):
                    for j in range(2):
                        red += old_img.get_pixel(i, j).red
                        green += old_img.get_pixel(i, j).green
                        blue += old_img.get_pixel(i, j).blue
                new_pixel.red = red // 6
                new_pixel.green = green // 6
                new_pixel.blue = blue // 6
            elif (x > 0) and (x < old_img.width - 1) and (y == old_img.height - 1):
                new_pixel = new_img.get_pixel(x, y)
                red = 0
                green = 0
                blue = 0
                for i in range(x - 1, x + 2):
                    for j in range(y - 1, y + 1):
                        red += old_img.get_pixel(i, j).red
                        green += old_img.get_pixel(i, j).green
                        blue += old_img.get_pixel(i, j).blue
                new_pixel.red = red // 6
                new_pixel.green = green // 6
                new_pixel.blue = blue // 6
            elif (x == 0) and (y == 0):
                new_pixel = new_img.get_pixel(x, y)
                red = 0
                green = 0
                blue = 0
                for i in range(2):
                    for j in range(2):
                        red += old_img.get_pixel(i, j).red
                        green += old_img.get_pixel(i, j).green
                        blue += old_img.get_pixel(i, j).blue
                new_pixel.red = red // 4
                new_pixel.green = green // 4
                new_pixel.blue = blue // 4
            elif (x == 0) and (y == old_img.height - 1):
                new_pixel = new_img.get_pixel(x, y)
                red = 0
                green = 0
                blue = 0
                for i in range(2):
                    for j in range(y - 1, y + 1):
                        red += old_img.get_pixel(i, j).red
                        green += old_img.get_pixel(i, j).green
                        blue += old_img.get_pixel(i, j).blue
                new_pixel.red = red // 4
                new_pixel.green = green // 4
                new_pixel.blue = blue // 4
            elif (x == old_img.width - 1) and (y == 0):
                new_pixel = new_img.get_pixel(x, y)
                red = 0
                green = 0
                blue = 0
                for i in range(x - 1, x + 1):
                    for j in range(2):
                        red += old_img.get_pixel(i, j).red
                        green += old_img.get_pixel(i, j).green
                        blue += old_img.get_pixel(i, j).blue
                new_pixel.red = red // 4
                new_pixel.green = green // 4
                new_pixel.blue = blue // 4
            elif (x == old_img.width - 1) and (y == old_img.height - 1):
                new_pixel = new_img.get_pixel(x, y)
                red = 0
                green = 0
                blue = 0
                for i in range(x - 1, x + 1):
                    for j in range(y - 1, y + 1):
                        red += old_img.get_pixel(i, j).red
                        green += old_img.get_pixel(i, j).green
                        blue += old_img.get_pixel(i, j).blue
                new_pixel.red = red // 4
                new_pixel.green = green // 4
                new_pixel.blue = blue // 4

    return new_img


def main():
    """
    Main function to run the image blurring process.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(9):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == "__main__":
    main()
