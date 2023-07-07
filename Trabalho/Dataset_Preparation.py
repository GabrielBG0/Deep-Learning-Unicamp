import os
import random
import cv2


def readAndResizeImage(oldPath, newPath):
    img = cv2.imread(oldPath)
    cv2.imwrite(newPath, img)


with os.scandir("Trabalho/Dataset/organized_dataset") as subFolders:
    for id, imageClass in enumerate(subFolders):
        with os.scandir(imageClass.path) as classes:
            for igmId, img in enumerate(classes):
                # if image name dont contain "mask" then resize
                if "mask" not in img.name:
                    newPath = (
                        "Trabalho/Dataset/Compiled/Classification/"
                        + "{:0>3}".format(id)
                        + "_"
                        + "{:0>5}".format(int(img.name.split(".")[0]) - 1)
                        + "."
                        + img.name.split(".")[1]
                    )
                    readAndResizeImage(img.path, newPath)
