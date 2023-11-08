# Get number of images from ./data/ears folder. They are saved in format XXXX.png
# Use a filter to get only the png files and not other files

import os
import sys

DATA_PATH = "./data/ears"

def main():
    # Get images
    images = [file for file in os.listdir(DATA_PATH) if file.endswith(".png")]

    # Split the images in train and test
    train_images = images[:int(len(images) * 0.8)]
    test_images = images[int(len(images) * 0.8):]


    for image in train_images[:5]:
        name = image.split(".")[0]

        # Get the connected labels in the same folder with same name and txt extension
        labels = [file for file in os.listdir(DATA_PATH) if file.startswith(name) and file.endswith(".txt")]

        if not len(labels):
            print("No metadata found for image {}".format(image))
            continue

        line = ""
        # Read the file
        with open(os.path.join(DATA_PATH, labels[0]), "r") as f:
            line = f.readlines()[0]

        # Get the labels
        labels = line.split(" ")


if __name__ == "__main__":
    main()

