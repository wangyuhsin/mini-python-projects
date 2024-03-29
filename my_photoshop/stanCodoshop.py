"""
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    dist = (
        (red - pixel.red) ** 2 +
        (green - pixel.green) ** 2 + (blue - pixel.blue) ** 2
    ) ** 0.5
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]
    """
    sum_r = 0
    sum_g = 0
    sum_b = 0
    for i in range(len(pixels)):
        sum_r += pixels[i].red
        sum_g += pixels[i].green
        sum_b += pixels[i].blue
    avg_r = sum_r // len(pixels)
    avg_g = sum_g // len(pixels)
    avg_b = sum_b // len(pixels)
    return [avg_r, avg_g, avg_b]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    avg_r = get_average(pixels)[0]
    avg_g = get_average(pixels)[1]
    avg_b = get_average(pixels)[2]
    best_pixel_dist = ((255**2) * 3) ** 0.5
    best_pixel = (0, 0)
    for i in range(len(pixels)):
        pixel_dist = get_pixel_dist(pixels[i], avg_r, avg_g, avg_b)
        if pixel_dist <= best_pixel_dist:
            best_pixel_dist = pixel_dist
            best_pixel = pixels[i]
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    for i in range(width):
        for j in range(height):
            pixels = []
            for k in range(len(images)):
                pixels += [images[k].get_pixel(i, j)]
            best_pixel = get_best_pixel(pixels)
            img = pixels.index(best_pixel)
            result.get_pixel(i, j).red = images[img].get_pixel(i, j).red
            result.get_pixel(i, j).green = images[img].get_pixel(i, j).green
            result.get_pixel(i, j).blue = images[img].get_pixel(i, j).blue

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith(".jpg"):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == "__main__":
    main()
