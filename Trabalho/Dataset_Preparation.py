import os
import random
import cv2

random.seed(1234)


# read and resize a image to 256x256 and save to the same path
def readAndResizeImage(oldPath, newPath):
    img = cv2.imread(oldPath)
    img = cv2.resize(img, (341, 256))
    cv2.imwrite(newPath, img)


with os.scandir("Dataset/organized_dataset") as subFolders:
    for id, imageClass in enumerate(subFolders):
        with os.scandir(imageClass.path) as classes:
            for igmId, img in enumerate(classes):
                if "_mask" in img.name:
                    newPath = (
                        "Dataset\Compiled\Classification\Mask\\"
                        + "{:0>3}".format(id)
                        + "_"
                        + "{:0>5}".format(int(img.name.split("_")[0]) - 1)
                        + "."
                        + img.name.split(".")[1]
                    )
                    readAndResizeImage(img.path, newPath)

                else:
                    newPath = (
                        "Dataset\Compiled\Classification\Image\\"
                        + "{:0>3}".format(id)
                        + "_"
                        + "{:0>5}".format(int(img.name.split(".")[0]) - 1)
                        + "."
                        + img.name.split(".")[1]
                    )
                    readAndResizeImage(img.path, newPath)
