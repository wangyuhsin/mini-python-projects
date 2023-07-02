# Mini Python Projects

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This repository contains a collection of 6 mini Python projects. Each project is a standalone script that demonstrates different aspects of Python programming. The projects included are:

1. [Breakout Game](#breakout-game)
2. [Hangman Game](#hangman-game)
3. [Name Popularity Searching System](#name-popularity-searching-system)
4. [My Photoshop](#my-photoshop)
5. [Find Anagrams](#find-anagrams)
6. [Boggle Game Solver](#boggle-game-solver)

## Breakout Game

The "Breakout Game" program is a Python implementation of the classic game Breakout. The game consists of a paddle, a ball, and a set of bricks. The goal is to use the paddle to bounce the ball and destroy all the bricks on the screen. The main game logic is implemented in the `breakout.py` file, and the game graphics are implemented in the `breakoutgraphics.py` file. This file defines a class `BreakoutGraphics` that handles the creation of the game window, paddle, ball, bricks, and collision detection.

To run the Breakout Game, execute the following command:
```python
python3 breakout.py
```

https://github.com/wangyuhsin/sc-projects/assets/76431031/37b0ded1-3f30-48d2-a93d-616b6d57a9b9

## Hangman Game

This program allows you to play the classic Hangman game. You will be presented with a dashed word, and your task is to guess the correct letters one by one. If your guess is correct, the program will reveal the corresponding letters. However, you only have a limited number of chances to guess the word correctly. Use your keyboard to input a single character for each guess. The program will provide visual feedback on your progress, and you will either win or lose depending on your ability to guess the word within the given chances.

To run the Hangman game, simply execute the following command:
```
python3 hangman.py
```

https://github.com/wangyuhsin/sc-projects/assets/76431031/5f1d85cf-679e-4960-96b7-da7bef429cfb

## Name Popularity Searching System

This project is a graphical system that allows you to search and visualize the popularity trends of baby names over the years. The `babygraphics.py` file contains functions to read baby name data from files and plot the trends on a canvas. The `babygraphicsgui.py` file provides a graphical user interface (GUI) to interact with the program.

To run the Name Popularity Searching System, execute the following command:
```
python3 babygraphics.py
```
This will launch the GUI window, where you can enter names in the search field to see their popularity trends over the years. The system will display graphs indicating the ranks of the given names in different decades.

https://github.com/wangyuhsin/sc-projects/assets/76431031/44574227-63c3-4359-a2bc-82dc325a71ae

## My Photoshop

"My Photoshop" is a collection of scripts that perform various image manipulation tasks. Each script can be run independently to achieve a specific effect on an input image. The scripts included in this project are:

1. `blur.py`: This script applies a blurring effect to an image using an algorithm that calculates the average RGB values of a pixel's nearest neighbors.
2. `mirror_lake.py`: This script creates a mirror lake effect by placing an inverted image below the original image.
3. `shrink.py`: This script shrinks an image to half its width and height, creating a new image.
4. `simpleimage.py`: This script provides a simple interface to create and manipulate images. It supports functions to create a new image, access the size of an image, get and set pixel values, and display an image on the screen.
5. `stanCodoshop.py` (Pedestrian Removing Application): The script processes a collection of images to create a "ghost" effect. By analyzing the average red, green, and blue values across all the pixels in the input images, the script selects the pixel from each image that has the smallest color distance to the average RGB values. These selected pixels are then used to generate a composite image with a ghostly appearance. The script repeats this process for all pixels in the output image, ensuring that each pixel contributes to the overall "ghost" effect.

To run the Pedestrian Removing Application, execute the following command:
```python
python3 stanCodoshop.py <folder containing all the images>
```

https://github.com/wangyuhsin/sc-projects/assets/76431031/3496c0c8-8465-43bd-965b-7120106e1525

## Find Anagrams

The `anagram.py` is a recursive Python script that generates anagrams for a given word input by the user. The program reads from an English dictionary file and uses it to validate the anagrams. The user can enter words to find their anagrams until they enter the EXIT constant, which terminates the program. The script uses a helper function to recursively find all possible combinations of letters from the input word and checks if they exist in the dictionary. If a valid anagram is found, it is added to a list of anagrams. The program displays the number of anagrams found for each word entered by the user.

To run the Find Anagrams program, execute the following command:
```python
python3 anagram.py
```

https://github.com/wangyuhsin/sc-projects/assets/76431031/9739d9a6-692e-4867-b344-52a98f04ccf9

## Boggle Game Solver

The "Boggle Game Solver" program is designed to solve the Boggle word game. The user is prompted to input a 4x4 grid of letters, and the program reads from an English dictionary file to validate the words found in the grid. The script uses a recursive helper function to explore all possible paths in the grid to form valid words. It checks if the current combination of letters forms a prefix of any word in the dictionary to optimize the search. If a valid word is found, it is added to a list of found words. The program displays the total number of words found in the grid. The input is validated for the correct format and legality before processing.

To run the Boggle Game Solver, execute the following command:
```python
python3 boggle.py
```

https://github.com/wangyuhsin/sc-projects/assets/76431031/e1c15552-cce5-4627-8f99-6a4419f84d69

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
The initial codebase and project structures are adapted from the stanCode SC001 & SC101 course materials. Special thanks to the course instructors for the inspiration.
