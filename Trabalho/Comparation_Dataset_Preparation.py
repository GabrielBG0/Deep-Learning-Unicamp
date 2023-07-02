import os
import cv2
import random

# Trabalho\Dataset\Compiled\Classification
# Trabalho\Dataset\Compiled\Comparation


def readAndSave(oldPath, newPath):
    img = cv2.imread(oldPath)
    cv2.imwrite(newPath, img)


random.seed(1234)
img_list = []
ids = set()
with os.scandir("Dataset/Compiled/Classification") as subFolders:
    for img in subFolders:
        img_list.append(img.path)
i = 0
while i < 9000:
    rand_idx = random.randint(0, 8999)
    rand_idx2 = random.randint(0, 8999)
    img_1 = img_list[rand_idx]
    img_2 = img_list[rand_idx2]
    if (img_1, img_2) not in ids and (img_2, img_1) not in ids:
        ids.add((img_1, img_2))
        ids.add((img_2, img_1))
        img_1_name = img_1.split("\\")[-1]
        img_2_name = img_2.split("\\")[-1]
        img_1_class = img_1_name.split("_")[0]
        img_2_class = img_2_name.split("_")[0]
        if img_1_class == img_2_class:
            new_path_1 = (
                "Dataset/Compiled/Comparation/"
                + "000"
                + "_"
                + "{:0>5}".format(i)
                + "_"
                + "a"
                + ".jpg"
            )
            new_path_2 = (
                "Dataset/Compiled/Comparation/"
                + "000"
                + "_"
                + "{:0>5}".format(i)
                + "_"
                + "b"
                + ".jpg"
            )
            readAndSave(img_1, new_path_1)
            readAndSave(img_2, new_path_2)
        else:
            new_path_1 = (
                "Dataset/Compiled/Comparation/"
                + "001"
                + "_"
                + "{:0>5}".format(i)
                + "_"
                + "a"
                + ".jpg"
            )
            new_path_2 = (
                "Dataset/Compiled/Comparation/"
                + "001"
                + "_"
                + "{:0>5}".format(i)
                + "_"
                + "b"
                + ".jpg"
            )
            readAndSave(img_1, new_path_1)
            readAndSave(img_2, new_path_2)
        i += 1

print(i)
print(len(ids))
